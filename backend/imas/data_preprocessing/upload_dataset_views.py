import json
import os

from django.http import HttpResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from backend.settings import whole_project_path
from imas.models import Dataset


@csrf_exempt
@require_http_methods(["GET"])
def download_dataset(request, dataset):
    file_path = os.path.join(whole_project_path, 'datasets/')
    file_path = os.path.join(file_path, dataset)
    file_path = os.path.join(file_path, 'Preprocessed_data.csv')
    response = FileResponse(open(file_path, "rb"))
    response['Content-Type'] = 'application/octet-stream'
    # 注意filename不支持中文
    response['Content-Disposition'] = "attachment;filename=Preprocessed_data.csv"
    return response


# 获取所有上传的数据集
@csrf_exempt
@require_http_methods(["GET"])
def get_datasets(request):
    datasets = list(Dataset.objects.values())
    # print(datasets)
    return HttpResponse(json.dumps(datasets), content_type="application/json")


@csrf_exempt
@require_http_methods(["POST"])
def upload_dataset(request):
    # save dataset desc
    name = request.POST.get('name', None)
    description = request.POST.get('description', None)
    is_single_case = request.POST.get('is_single_case', None)
    is_labeled = request.POST.get('is_labeled', None)
    need_OCR = request.POST.get('need_OCR', None)
    # train = request.POST.get('train', None)
    # valid = request.POST.get('valid', None)
    # test = request.POST.get('test', None)

    if is_single_case == 'false':
        is_single_case = 0
    else:
        is_single_case = 1

    if is_labeled == 'false':
        is_labeled = 0
    else:
        is_labeled = 1
        need_OCR = request.POST.get('need_OCR', None)

    if need_OCR == 'false':
        need_OCR = 0
    else:
        need_OCR = 1

    dataset = Dataset(name=name,
                      description=description,
                      is_single_case=is_single_case,
                      is_labeled=is_labeled,
                      need_OCR=need_OCR,
                      status=0)
    # if not is_single_case:
    #     dataset.train_set_proportion = 4,
    #     dataset.test_set_proportion = 4,
    #     dataset.valid_set_proportion = 2,
    # print(dataset.train_set_proportion)
    dataset.save()

    # save dataset file
    upload_file = request.FILES.get('file')
    dataset_upload = os.path.join(whole_project_path, 'datasets/')
    save_path = os.path.join(dataset_upload, upload_file.name)
    with open(save_path, 'wb+') as f:
        for chunk in upload_file.chunks():
            f.write(chunk)

    # deal with data
    if is_single_case and is_labeled:
        pass
    elif is_single_case and not is_labeled:
        pass
    elif not is_single_case and is_labeled:
        pass
    else:
        pass

    return HttpResponse("success", content_type="application/json")


def remove_privacy(data):
    return None


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_dataset(request, dataset):
    dataset = Dataset.objects.get(name=dataset)
    dataset.delete()
    return HttpResponse("success", content_type="application/json")