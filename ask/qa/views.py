from django.shortcuts import render
from django.http import HttpResponse


def home(request, *args, **kwargs):
    response = "Project AskPupkin homepage"
    return HttpResponse(response)


def stub(request, *args, **kwargs):
    return HttpResponse('OK')


def question(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
