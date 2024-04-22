import json
import jwt

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from imas.models import UserInfo


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
            "role": user.role,
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
