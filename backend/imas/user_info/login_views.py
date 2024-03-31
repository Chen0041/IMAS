from django.http import HttpResponse

from imas.models import UserInfo


def login(request):
    users = UserInfo.objects.all()
    return HttpResponse(users)