import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from imas.models import Dataset


@csrf_exempt
@require_http_methods(["GET"])
def get_labeled_datasets(request):
    dataset_pos = list(Dataset.objects.filter(is_single_case=0, status=1).values())
    ret = []
    for dataset in dataset_pos:
        ret.append(dataset['name'])
    # print(ret)
    return HttpResponse(json.dumps(ret), content_type="application/json")


def get_model_categories(request):
    return None


def creat_train_task(request):
    return None