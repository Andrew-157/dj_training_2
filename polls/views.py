from django.http import HttpResponse
from .models import Question


def index(request):
    return HttpResponse(f"Hello, this is polls index page")


def detail(request, question_id):
    return HttpResponse(f'You are looking at question {question_id}')


def results(request, question_id):
    return HttpResponse(f'You are looking at the results of the question {question_id}')


def vote(request, question_id):
    return HttpResponse(f'You are voting for the question {question_id}')
