from http.client import responses
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Question,Choice
from django.template import loader


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request,"polls/index.html",context)

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question': question})


    #d1=Choice.objects.filter(question__question_text__startswith="IK")
    #return HttpResponse(d1)

def results(request,question_id):
    response="you are looking for this %s"
    return HttpResponse(response % question_id)
   
def vote(request, question_id):

    return HttpResponse("You're voting on question %s." % question_id)