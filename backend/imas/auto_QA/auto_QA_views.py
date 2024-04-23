import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from imas.models import TrainModelTask


# 获取训练完成的模型
@csrf_exempt
@require_http_methods(["GET"])
def get_trained_models(request):
    model_entity = TrainModelTask.objects.filter(status=1).values()
    models = []
    for model in model_entity:
        models.append(model.task_name)
    return HttpResponse(json.dumps(models), content_type="application/json")


# 上传问题描述和图片，返回答案
@csrf_exempt
@require_http_methods(["POST"])
def upload_medical_archive(request):
    entity = json.loads(request.body)
    print(entity)
    answer = ''
    # TODO 深度学习模型预测
    return HttpResponse(json.dumps(answer), content_type="application/json")