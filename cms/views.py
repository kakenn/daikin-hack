# coding=utf-8
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Answer
import re


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
            'id': select.id
        }

    return JsonResponse(select)