from http.client import responses
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hellosss")

def detail(request,question_id):
    return HttpResponse("you are looking at question %s"% question_id)

def results(request,question_id):
    response="you are looking for this %s"
    return HttpResponse(response % question_id)
   
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)