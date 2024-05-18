import base64
import csv
import json
import os
import re
import urllib
import zipfile
from multiprocessing import Process
import en_ner_bc5cdr_md
from flashtext import KeywordProcessor
import requests

from django.http import HttpResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from backend.settings import whole_project_path
from imas.models import Dataset, SingleDiseaseCaseInfo, UserInfo


@csrf_exempt
@require_http_methods(["GET"])
def download_dataset(request, dataset):
    dataset_id = Dataset.objects.get(name=dataset).id
    cases = SingleDiseaseCaseInfo.objects.filter(dataset_id=dataset_id)
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="Preprocessed_data.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(['dataset_name', 'txt_name', 'img_name', 'description', 'disease', 'medicine'])
    for case in cases:
        writer.writerow([dataset, case.patient_name, case.picture_name, case.whole_desc, case.disease, case.medicine])
    return response


# 获取所有上传的数据集
@csrf_exempt
@require_http_methods(["GET"])
def get_datasets(request):
    datasets = list(Dataset.objects.values())
    for dataset in datasets:
        if dataset['status'] == 0:
            dataset['status'] = 'processing'
        elif dataset['status'] == 1:
            dataset['status'] = 'success'
        else:
            dataset['status'] = 'failed'
    return HttpResponse(json.dumps(datasets), content_type="application/json")


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_dataset(request, dataset):
    login_vo = json.loads(request.body)
    login_name = login_vo['login_name']
    dataset = Dataset.objects.get(name=dataset)
    user_id = UserInfo.objects.get(login_name=login_name).id
    if dataset.user_id != user_id:
        return HttpResponse("fail", status=500, content_type="application/json")
    # 批量删除single_case_info中的对应记录
    SingleDiseaseCaseInfo.objects.filter(dataset_id=dataset.id).delete()
    dataset.delete()
    return HttpResponse("success", content_type="application/json")


@csrf_exempt
@require_http_methods(["POST"])
def upload_dataset(request):
    # save dataset record
    login_name = request.POST.get('login_name', None)
    name = request.POST.get('name', None)
    description = request.POST.get('description', None)
    is_single_case = request.POST.get('is_single_case', None)
    is_labeled = request.POST.get('is_labeled', None)
    need_OCR = request.POST.get('need_OCR', None)
    train = request.POST.get('train', None)
    valid = request.POST.get('valid', None)
    test = request.POST.get('test', None)
    # check repeat dataset name
    datasets = Dataset.objects.filter(name=name)
    if len(datasets) != 0:
        return HttpResponse("Already have dataset with this name", status=500, content_type="application/json")
    # change frontend bool to int
    if is_single_case == 'false':
        is_single_case = 0
    else:
        is_single_case = 1
    if is_labeled == 'false':
        is_labeled = 0
    else:
        is_labeled = 1
    if need_OCR == 'false':
        need_OCR = 0
    else:
        need_OCR = 1
    # save to database
    user_id = UserInfo.objects.get(login_name=login_name).id
    dataset = Dataset(user_id=user_id,
                      name=name,
                      description=description,
                      is_single_case=is_single_case,
                      is_labeled=is_labeled,
                      need_OCR=need_OCR,
                      status=0)
    if not is_single_case:
        dataset.train_set_proportion = int(train)
        dataset.test_set_proportion = int(test)
        dataset.valid_set_proportion = int(valid)
    dataset.save()

    # save dataset file
    upload_file = request.FILES.get('file')
    dataset_upload = os.path.join(whole_project_path, 'datasets/')
    save_path = os.path.join(dataset_upload, upload_file.name)
    with open(save_path, 'wb+') as f:
        for chunk in upload_file.chunks():
            f.write(chunk)
    # unzip upload file
    r = zipfile.is_zipfile(save_path)
    if r:
        fz = zipfile.ZipFile(save_path, 'r')
        dst_path = os.path.join(dataset_upload, name)
        for file in fz.namelist():
            fz.extract(file, dst_path)
    else:
        return HttpResponse('Upload file is not zip', status=500, content_type="application/json")

    # new process
    p = Process(target=auto_preprocess, args=(dst_path, is_labeled, is_single_case, need_OCR, dataset))
    p.start()
    return HttpResponse("success", content_type="application/json")


def auto_preprocess(dst_path, is_labeled, is_single_case, need_OCR, dataset):
    """
    1.zip文件中包含医学图像和对应病例描述，分别用图片（*.jpg,*.jpeg,*.png）和文本（*.txt,*.csv等）表示。
    2.用relationship.csv文件标示图片和文本的对应。
    3.若选中is_labeled，relationship.csv文件每列分别为：图片文件名、病例名、图片描述、疾病、药物，不再上传文本。反之，每列分别为：图片文件名、文本文件名。含扩展名，不含表头。
    4.若选中is_single_case，则图片、文本（如有需要）、对应关系三个文件均置于根目录下。否则创建两个文件夹，分别命名为img和txt，存放图片和文本文件。
    5.若选中need_OCR，则文本描述可以用图片形式表示。
    """
    relationship_file = os.path.join(dst_path, 'relationship.csv')
    try:
        if is_labeled:
            with open(relationship_file, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    picture_name = row[0]
                    patient_name = row[1]
                    whole_desc = row[2]
                    disease = row[3]
                    medicine = row[4]
                    # save single_case_info
                    single_case_info = SingleDiseaseCaseInfo(dataset_id=dataset.id,
                                                             picture_name=picture_name,
                                                             patient_name=patient_name,
                                                             whole_desc=whole_desc,
                                                             disease=disease,
                                                             medicine=medicine)
                    single_case_info.save()
        else:
            with open(relationship_file, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    img_name = row[0]
                    txt_name = row[1]
                    if not is_single_case:
                        txt_path = os.path.join(dst_path, 'txt/')
                    else:
                        txt_path = dst_path
                    if need_OCR:
                        txt_path = os.path.join(txt_path, txt_name)
                        whole_desc = call_OCR(txt_path)
                    else:
                        txt_path = os.path.join(txt_path, txt_name)
                        with open(txt_path, 'r', encoding='utf-8') as f:
                            whole_desc = f.read()
                    whole_desc = remove_privacy(whole_desc)
                    entities = ner(whole_desc)
                    disease = []
                    medicine = []
                    for entity in entities:
                        if entity[1] == 'DISEASE':
                            disease.append(entity[0])
                        elif entity[1] == 'CHEMICAL':
                            medicine.append(entity[0])
                    # remove repeat
                    disease = list(set(disease))
                    disease = ','.join(disease)
                    medicine = list(set(medicine))
                    medicine = ','.join(medicine)
                    # save single_case_info
                    single_case_info = SingleDiseaseCaseInfo(dataset_id=dataset.id,
                                                             picture_name=img_name,
                                                             patient_name=txt_name,
                                                             whole_desc=whole_desc,
                                                             disease=disease,
                                                             medicine=medicine)
                    single_case_info.save()
        dataset.status = 1
        dataset.save()
    except Exception as e:
        print(e)
        dataset.status = -1
        dataset.save()


def remove_privacy(text):
    # view this for detail:
    # https://developer.chat/remove-personal-information-text-python
    # https://github.com/lmeulen/PrivacyFilter
    # replace telephone number .etc
    text = re.sub(r'\d{3}\d*', ' ', text).strip()
    # replace email
    text = re.sub(r'\w*@\w*', ' ', text).strip()
    # replace date
    text = re.sub("\d{2}[- /.]\d{2}[- /.]\d{,4}", " ", text)
    # replace name and place
    keyword_processor = KeywordProcessor(case_sensitive=False)
    for name in file_to_list(os.path.join(whole_project_path, 'privacy_datasets/firstnames.csv')):
        keyword_processor.add_keyword(name, " ")
    for name in file_to_list(os.path.join(whole_project_path, 'privacy_datasets/lastnames.csv')):
        keyword_processor.add_keyword(name, " ")
    for name in file_to_list(os.path.join(whole_project_path, 'privacy_datasets/places.csv')):
        keyword_processor.add_keyword(name, " ")
    text = keyword_processor.replace_keywords(text)
    return text


def file_to_list(filename):
    items = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f.readlines():
            items.append(line.rstrip())
    return items

def call_OCR(file_path):
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=" + get_access_token()
    file_code = get_file_content_as_base64(file_path, False)
    payload = 'image=' + file_code + '&detect_direction=false&detect_language=false&paragraph=false&probability=false'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    result = json.loads(response.text)
    res = result['words_result'][0]['words']
    return res


def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    API_KEY = "ETi3Z6xunyLonkb7aqDc3m82"
    SECRET_KEY = "wsPq1m52nxz25ekTX9mIY6u3GTOpDUw2"
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


def ner(text):
    nlp = en_ner_bc5cdr_md.load()
    doc = nlp(str(text))
    res = []
    for entity in doc.ents:
        res.append([str(entity), str(entity.label_)])
    return res
