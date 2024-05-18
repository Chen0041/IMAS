import json
import os

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from backend.settings import whole_project_path
from imas.models import Dataset, SingleDiseaseCaseInfo


@csrf_exempt
@require_http_methods(["GET"])
def get_preprocessed_datasets(request):
    dataset_pos = list(Dataset.objects.all())
    ret = []
    for dataset in dataset_pos:
        if dataset.status == 1:
            ret.append(dataset.name)
    # print(ret)
    return HttpResponse(json.dumps(ret), content_type="application/json")


@csrf_exempt
@require_http_methods(["GET"])
def get_cases(request, dataset):
    dataset_id = Dataset.objects.get(name=dataset).id
    cases = list(SingleDiseaseCaseInfo.objects.filter(dataset_id=dataset_id).values())
    # print(cases)
    if len(cases) == 0:
        return HttpResponse('No cases', status=500, content_type="application/json")
    else:
        return HttpResponse(json.dumps(cases), content_type="application/json")


@csrf_exempt
@require_http_methods(["POST"])
def modify_case(request, dataset, patient_name):
    dataset_id = Dataset.objects.get(name=dataset).id
    single_case = SingleDiseaseCaseInfo.objects.get(dataset_id=dataset_id, patient_name=patient_name)
    single_case.whole_desc = request.POST.get("description")
    single_case.disease = request.POST.get("disease")
    single_case.medicine = request.POST.get("medicine")
    single_case.save()
    return HttpResponse("success", content_type="application/json")


@csrf_exempt
@require_http_methods(["GET"])
def get_picture(request, dataset, picture_name):
    is_single_case = Dataset.objects.get(name=dataset).is_single_case
    if is_single_case == 0:
        picture_name = 'img/' + picture_name
    img_path = 'datasets/' + dataset + '/' + picture_name
    img_path = os.path.join(whole_project_path, img_path)
    image_data = open(img_path, "rb").read()
    return HttpResponse(image_data, content_type="image/png")
