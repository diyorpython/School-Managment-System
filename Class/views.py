from django.shortcuts import render
from django.http import HttpResponse

def response(request):
    return HttpResponse("Hello world")