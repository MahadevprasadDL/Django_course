from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def greet(request):
    return HttpResponse ("Hi this is my first project")

def func2 (request):
    return HttpResponse (" <h1>Welcome to django Project<h1>")
