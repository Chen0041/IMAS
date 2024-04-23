import json
import jwt

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from imas.models import UserInfo


# 登录
@csrf_exempt
@require_http_methods(["POST"])
def login(request):
    login_vo = json.loads(request.body)
    print(login_vo)
    if login_vo is None or login_vo['login_name'] == '' or login_vo['password'] == '':
        return HttpResponse('error username or password', status=401, content_type='application/json')
    else:
        user = UserInfo.objects.get(login_name=login_vo['login_name'])
        if user is None or user.password != login_vo['password']:
            return HttpResponse('error username or password', status=401, content_type='application/json')
        token = jwt.encode({"login_name": login_vo['login_name']}, "secret", algorithm="HS256")
        user_info = {
            "username": user.login_name,
            "name": user.name,
            "type": user.role,
            "phone": user.phone,
            "age": user.age,
            "gender": user.gender,
            "email": user.email,
        }
        info = json.dumps({"info": user_info})
        print(info)
        response = HttpResponse(info, status=200, content_type='application/json')
        response.headers['token'] = token
        return response


# 注册
@csrf_exempt
@require_http_methods(["POST"])
def user_register(request):
    user_entity = remove_privacy(request)
    new_user = UserInfo(login_name=user_entity['login_name'], name=user_entity['name'],
                        password=user_entity['password'], age=user_entity['age'], gender=user_entity['gender'],
                        phone=user_entity['phone'], role=user_entity['type'], email=user_entity['email'],
                        marriage=user_entity['marriage'])
    new_user.save()
    return HttpResponse('success', status=200, content_type='application/json')


# 修改个人信息
@csrf_exempt
@require_http_methods(["POST"])
def user_modify(request):
    user_entity = remove_privacy(request)
    user = UserInfo.objects.get(login_name=user_entity['login_name'])
    user.name = user_entity['name']
    user.password = user_entity['password']
    user.age = user_entity['age']
    user.gender = user_entity['gender']
    user.phone = user_entity['phone']
    user.email = user_entity['email']
    user.marriage = user_entity['marriage']
    user.save()
    return HttpResponse('success', status=200, content_type='application/json')


# 去隐私
def remove_privacy(request):
    user_entity = json.loads(request.body)
    if len(user_entity['name']) > 1:
        user_entity['name'] = user_entity['name'][:1] + '*' + user_entity['name'][2:]
    if len(user_entity['phone']) == 11:
        user_entity['phone'] = user_entity['phone'][:9] + '**'
    return user_entity
