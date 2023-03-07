from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hi(request):
    return HttpResponse("<h1>Namaste condry<h1>")

def hi1(request):
    return HttpResponse("<h1> En macha en madtha edhiya</h1>")
