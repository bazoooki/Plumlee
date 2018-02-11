from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
from app.models import *
import datetime
from pprint import pprint


@csrf_exempt
def logout_view(request):
    ret = {'status': 1}
    logout(request)   
    return JsonResponse(ret)         

@csrf_exempt
def login_view(request):

    ret = {'status': 0}
    try:
        data = json.loads(request.body)
    except:
        return JsonResponse(ret)
    
    user = authenticate(username = data['user'], password = data['password'])
    if user is not None:
        login(request, user)
        ret['status'] = 1
    else:
        return JsonResponse(ret)           
    return JsonResponse(ret)


@csrf_exempt
def register_view(request):
    ret = {'status': 0}
    try:
        data = json.loads(request.body)
    except:
        return JsonResponse(ret)
    userName = data['user']    
    userPass = data['password']
    if User.objects.filter(username=userName).exists():
        ret['error'] = 'already exists'
        return JsonResponse(ret)
    else:
        user = User.objects.create_user(username=userName, password=userPass)

    ret['user'] = user.username
    ret['status'] = 1
    pprint(data)
    return JsonResponse(ret)

def whoami(request):
    ret = {'status': 0}
    user = request.user.username
    if user is not None:
        ret['status'] = 1
        ret['user'] = user
    return JsonResponse(ret)







