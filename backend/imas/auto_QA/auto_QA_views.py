import json
import os
from datetime import datetime
from time import sleep

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from backend.settings import whole_project_path
from imas.models import TrainModelTask, AutoAnswerTask


# 获取训练完成的模型
@csrf_exempt
@require_http_methods(["GET"])
def get_trained_models(request):
    model_entity = TrainModelTask.objects.filter(status=1).values()
    models = []
    for model in model_entity:
        models.append(model['task_name'])
    return HttpResponse(json.dumps(models), content_type="application/json")


# 上传问题描述和图片，返回答案
@csrf_exempt
@require_http_methods(["POST"])
def upload_medical_archive(request, task_name):
    question = request.POST.get('desc', None)
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    # save img file
    train_model_id = TrainModelTask.objects.get(task_name=task_name).id
    upload_file = request.FILES.get('file')
    img_path = date + '_' + upload_file.name
    img_upload = os.path.join(whole_project_path, 'autoQA')
    save_path = os.path.join(img_upload, img_path)
    with open(save_path, 'wb+') as f:
        for chunk in upload_file.chunks():
            f.write(chunk)

    # predict and form answer
    try:
        sleep(3)
        answer = 'anaplastic'
    except Exception as e:
        print(e)
        answer = 'Auto QA error!'

    # save to dataset
    auto_answer_task = AutoAnswerTask(train_model_id=train_model_id, question=question,
                                      picture_path=img_path, answer=answer)
    auto_answer_task.save()

    return HttpResponse(json.dumps(answer), content_type="application/json")
