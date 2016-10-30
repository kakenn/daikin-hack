# coding=utf-8
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Answer
import requests
import re

cold_list = [42, 72]
hot_list = [52]


def index(request):
    answers = Answer.objects.order_by('-id')
    select = None
    print answers
    for answer in answers:

        keyword = u"(" + answer.keyword.replace(" ", "|") + u")"
        print keyword
        if re.search(keyword, request.GET["text"]):
            if answer.parent == int(request.GET['id']):
                select = answer
                break
            else:
                select = answer

    if select is None:
        select = {
            'text': u"すいません。わかりません。",
            'id': 9999
        }
    else:
        select = {
            'text': select.text,
            'id': int(select.id)
        }
    if select["id"] in cold_list:
        cold(1)
    if select["id"} in hot_list:
        hit(1)
    return JsonResponse(select)


def cold(_id):
    data = '{"id":'+ str(_id) +',"status":{"power":1,"operation_mode":2,"set_temperature":15,"fan_speed":2,"fan_direction":0}}'
    requests.post('https://api-01.daikin.ishikari-dc.net/equipments/'+ str(_id) +'/', data=data)


def hot(_id):
    data = '{"id":'+ str(_id) +',"status":{"power":1,"operation_mode":2,"set_temperature":28,"fan_speed":2,"fan_direction":0}}'
    requests.post('https://api-01.daikin.ishikari-dc.net/equipments/'+ str(_id) +'/', data=data)