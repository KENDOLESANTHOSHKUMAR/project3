from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("<h1> Hi  EveryOne</h1>")


def hello1(request):
    return HttpResponse("<h1> Hi Guys </h1>")