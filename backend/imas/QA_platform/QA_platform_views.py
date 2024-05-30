import json
import os
from datetime import datetime

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from backend.settings import whole_project_path
from imas.models import Department, Question, UserInfo


@csrf_exempt
@require_http_methods(["GET"])
def get_departments(request):
    departments = list(Department.objects.values())
    return HttpResponse(json.dumps(departments), content_type="application/json")


@csrf_exempt
@require_http_methods(["POST"])
def get_questions(request):
    ret = []
    status = int(request.POST.get('status', 2))
    department_id = int(request.POST.get('department_id', 0))
    search_content = request.POST.get('search_content', '')
    questions = list(Question.objects.values())
    print(status)
    print(department_id)
    print(search_content)
    print(questions)
    for question in questions:
        if status == 2 or question['status'] == status:
            if department_id == 0 or question['department_id'] == department_id:
                if search_content == '' or search_content in question['content']:
                    print('yes')
                    department = Department.objects.get(id=question['department_id']).department
                    if question['status'] == 1:
                        question_status = 'answered'
                    else:
                        question_status = 'not_answered'
                    ret.append({
                        'id': question['id'],
                        'date': question['date'],
                        'content': question['content'],
                        'department': department,
                        'status': question_status,
                        'answer': question['answer']
                    })
    print(ret)
    return HttpResponse(json.dumps(ret), content_type="application/json")


@csrf_exempt
@require_http_methods(["POST"])
def new_question(request):
    login_name = request.POST.get('login_name', None)
    content = request.POST.get('content', None)
    department_id = request.POST.get('department_id', None)
    upload_file = request.FILES.get('file')
    user_id = UserInfo.objects.get(login_name=login_name).id

    # save img file
    date = datetime.now().strftime('%Y-%m-%d')
    img_path = date + '_' + upload_file.name
    img_upload = os.path.join(whole_project_path, 'QA_platform')
    save_path = os.path.join(img_upload, img_path)
    with open(save_path, 'wb+') as f:
        for chunk in upload_file.chunks():
            f.write(chunk)

    question = Question(user_id=user_id, department_id=department_id, content=content, date=date,
                        status=0, picture_path=img_path)
    question.save()
    return HttpResponse('success', content_type="application/json")


@csrf_exempt
@require_http_methods(["POST"])
def answer_question(request, question_id):
    login_name = request.POST.get('login_name', None)
    answer = request.POST.get('answer', '')
    user = UserInfo.objects.get(login_name=login_name)
    if user.role != 1:
        return HttpResponse('not doctor', status=500, content_type="application/json")
    question = Question.objects.get(id=question_id)
    if question.status == 1:
        question.answer = question.answer + ' | ' + answer
    else:
        question.status = 1
        question.answer = answer
    question.save()
    return HttpResponse('success', content_type="application/json")


@csrf_exempt
@require_http_methods(["GET"])
def get_picture(request, question_id):
    question = Question.objects.get(id=question_id)
    picture_name = question.picture_path
    img_path = 'QA_platform/' + picture_name
    img_path = os.path.join(whole_project_path, img_path)
    image_data = open(img_path, "rb").read()
    return HttpResponse(image_data, content_type="image/png")


@csrf_exempt
@require_http_methods(["POST"])
def delete_question(request, question_id):
    login_name = request.POST.get('login_name', None)
    user = UserInfo.objects.get(login_name=login_name)
    question = Question.objects.get(id=question_id)
    if question.user_id != user.id:
        return HttpResponse('delete error', status=500, content_type="application/json")
    else:
        question.delete()
        return HttpResponse('success', content_type="application/json")
