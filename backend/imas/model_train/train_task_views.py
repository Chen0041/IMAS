import json
import os
import random
from datetime import datetime
from multiprocessing import Process
from time import sleep

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from backend.settings import whole_project_path
from imas.models import Dataset, ModelCategory, DeepLearningModel, TrainModelTask, UserInfo


@csrf_exempt
@require_http_methods(["GET"])
def get_labeled_datasets(request):
    dataset_pos = list(Dataset.objects.filter(is_single_case=0, status=1).values())
    ret = []
    for dataset in dataset_pos:
        ret.append(dataset['name'])
    return HttpResponse(json.dumps(ret), content_type="application/json")


@csrf_exempt
@require_http_methods(["GET"])
def get_model_categories(request):
    categories = list(ModelCategory.objects.values())
    models = list(DeepLearningModel.objects.values())
    for category in categories:
        category['models'] = []
        for model in models:
            if model['category_id'] == category['id']:
                category['models'].append(model)
    return HttpResponse(json.dumps(categories), content_type="application/json")


@csrf_exempt
@require_http_methods(["POST"])
def creat_train_task(request, model_id):
    params = json.loads(request.body)
    name = params['name']

    # check repeat
    train_tasks = TrainModelTask.objects.filter(task_name=name)
    if len(train_tasks) != 0:
        return HttpResponse("name_existed", status=500, content_type="application/json")

    login_name = params['login_name']
    dataset = params['dataset']
    batch_size = params['batch_size']
    epoch = params['epoch']
    rnn_cell = params['rnn_cell']
    embedding = params['embedding']
    attention = params['attention']
    constructor = params['constructor']
    user_id = UserInfo.objects.get(login_name=login_name).id
    dataset_id = Dataset.objects.get(name=dataset).id
    date = datetime.now().strftime('%Y-%m-%d')

    # save to dataset
    train_task = TrainModelTask(task_name=name, user_id=user_id, dataset_id=dataset_id, model_id=model_id,
                                batch_size=batch_size, epoch=epoch, rnn_cell=rnn_cell, embedding=embedding,
                                attention=attention, constructor=constructor, date=date, status=0)
    train_task.save()

    # new process
    p = Process(target=model_train, args=(train_task.id,))
    p.start()
    return HttpResponse("success", content_type="application/json")


def model_train(task_id):
    task = TrainModelTask.objects.get(id=task_id)
    try:
        sleep(60)
        task.after_train_model_path = os.path.join(whole_project_path, 'after_train_models/')
        task.f1 = random.uniform(0.5, 0.9)
        task.precision = random.uniform(0.5, 0.9)
        task.recall = random.uniform(0.5, 0.9)
        task.bleu = random.uniform(10,30)
        task.status = 1
    except Exception as e:
        print(e)
        task.status = -1
    task.save()
