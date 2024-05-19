import csv
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from imas.models import TrainModelTask, DeepLearningModel, Dataset, UserInfo


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
    return HttpResponse(json.dumps(ret), content_type="application/json")


@csrf_exempt
@require_http_methods(["GET"])
def download_reports(request):
    reports = TrainModelTask.objects.filter(status=1)
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="Reports.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(['task_name', 'dataset_name', 'model_name', 'date', 'f1', 'recall', 'precision', 'bleu', 'epoch',
                     'batch_size', 'rnn_cell', 'embedding', 'attention', 'constructor'])
    for report in reports:
        model_name = DeepLearningModel.objects.get(id=report.model_id).name
        dataset_name = Dataset.objects.get(id=report.dataset_id).name
        writer.writerow([report.task_name, dataset_name, model_name, report.date, report.f1, report.recall,
                         report.precision, report.bleu, report.epoch, report.batch_size, report.rnn_cell,
                         report.embedding, report.attention, report.constructor])
    return response


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_task(request, task_name):
    login_name = json.loads(request.body)['login_name']
    task = TrainModelTask.objects.get(task_name=task_name)
    user_id = UserInfo.objects.get(login_name=login_name).id
    if task.user_id != user_id:
        return HttpResponse("fail", status=500, content_type="application/json")
    task.delete()
    return HttpResponse("success", content_type="application/json")


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_failed_task(request):
    TrainModelTask.objects.filter(status=-1).delete()
    return HttpResponse("success", content_type="application/json")