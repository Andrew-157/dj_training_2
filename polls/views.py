from django.http import HttpResponse
from .models import Question


def index(request):
    queryset = Question.objects.order_by('pub_date')[:5]
    recent_questions = ', '.join([q.question_text for q in queryset])
    return HttpResponse(recent_questions)


def detail(request, question_id):
    return HttpResponse(f'You are looking at question {question_id}')


def results(request, question_id):
    return HttpResponse(f'You are looking at the results of the question {question_id}')


def vote(request, question_id):
    return HttpResponse(f'You are voting for the question {question_id}')
