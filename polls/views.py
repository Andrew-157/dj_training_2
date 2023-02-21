from django.http import HttpResponse
from .models import Question
from django.shortcuts import render, get_object_or_404


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    return HttpResponse(f'You are looking at the results of the question {question_id}')


def vote(request, question_id):
    return HttpResponse(f'You are voting for the question {question_id}')
