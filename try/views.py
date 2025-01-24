from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'index.html')

def none(request):
    return render(request,'layout.html')

def about(request):
    return render(request,'about.html')