from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render

from .forms import UserForm
from .sndapi import *

from models import Feed
from models import Track

def index(request):
    context = { "message":  request}
    return render(request, 'subs/index.html', context)

def about(request):
    return render(request, 'subs/about.html')

def track(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            raw_feed = build_feed(form.cleaned_data['username'])

            for track in raw_feed:
                t = Track.objects.create(id = track[0], date = track[1])
                print t
                f = Feed.objects.get_or_create(username = 'fsxfreak')
                f.tracks.add(t)

            print(feed.objects.all())

            return HttpResponseRedirect('track.html')
    else:
        form = UserForm()

    return render(request, 'subs/track.html', { 'form': form })

def list(request):
    return render(request, 'subs/list.html')
    pass
