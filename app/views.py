from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>hello this is home page....</h1>')

def a12(request):
    return HttpResponse('<h1>hello this is a page....</h1>')

def b12(request):
    return HttpResponse('<h1>hello this is b page....</h1>')

def error_404_view(request,exception):
    return HttpResponse('<h1>hello this is error heandler page....</h1>')