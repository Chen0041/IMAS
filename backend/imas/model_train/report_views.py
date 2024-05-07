import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from imas.models import TrainModelTask, DeepLearningModel, Dataset


@csrf_exempt
@require_http_methods(["GET"])
def get_report(request):
    report_pos = list(TrainModelTask.objects.all().values())
    ret = []
    for report in report_pos:
        model_name = DeepLearningModel.objects.get(id=report['model_id']).name
        dataset_name = Dataset.objects.get(id=report['dataset_id']).name
        ret.append({
            'classification': model_name,
            'f1': report['f1'],
            'recall': report['recall'],
            'prec': report['precision'],
            'bleu': report['bleu'],
            'name': report['task_name'],
            'date': report['date'],
            'state': report['status'],
            'data': dataset_name,
            'epoch': report['epoch'],
            'batchsize': report['batch_size']
        })
    print(ret)
    return HttpResponse(json.dumps(ret), content_type="application/json")


def download_reports(request):
    return None


def delete_task(request):
    return None


def delete_failed_task(request):
    return None