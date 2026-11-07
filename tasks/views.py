from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('welcome to rask managemnt project')

def contact(request):
    return HttpResponse('<h1>This is contact page</h1>')

def show_task(request):
    return HttpResponse("This is our task page")

def show_specific_task(request,id):
    print(f'id --> {id}')
    print(f'id type {type(id)}')
    return HttpResponse('This is specific task page')