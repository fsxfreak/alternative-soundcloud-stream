from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

def index(request):
    context = { "message":  request}
    return render(request, 'subs/index.html', context)

def about(request):
    return render(request, 'subs/about.html')