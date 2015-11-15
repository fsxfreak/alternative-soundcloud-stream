from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render

from .forms import UserForm

def index(request):
    context = { "message":  request}
    return render(request, 'subs/index.html', context)

def about(request):
    return render(request, 'subs/about.html')

def track(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            
            
            return HttpResponseRedirect('track.html')
    else:
        form = UserForm()

    return render(request, 'subs/track.html', { 'form': form })