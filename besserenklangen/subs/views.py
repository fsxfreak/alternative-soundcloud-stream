from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render

from django.template import RequestContext, loader

from .forms import UserForm
from .sndapi import *

from models import Feed
from models import Track

def index(request):
    context = { "message":  request }
    return render(request, 'subs/index.html', context)

def about(request):
    return render(request, 'subs/about.html')

def track(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.cleaned_data['username']
            raw_feed = build_feed(user, 5, 2)

            f = Feed(username = user)
            f.save()

            i = 0
            for track in raw_feed:
                art_url = 'http://i.imgur.com/BNBFGfg.jpg'
                if track[5] != None:
                    art_url = track[5]

                t = Track(id = track[0]
                        , date = track[1]
                        , title = track[2]
                        , artist = track[3]
                        , uri = track[4]
                        , art = art_url)
                t.save()

                f.tracks.add(t)
                i = i + 1
            print i

            return HttpResponseRedirect('track.html')
    else:
        form = UserForm()

    return render(request, 'subs/track.html', { 'form': form })

def list(request):
    template = loader.get_template('subs/list.html')
    context = RequestContext(request, {
        'userid': 'nobody'
    })

    if request.method == 'POST':
        form = UserForm(request.POST)
        userid = ''
        if form.is_valid():
            userid = form.cleaned_data['username']

        tracks = Feed.objects.get(username=userid).tracks.all().order_by('-date')
        context = RequestContext(request, {
            'form': form,
            'userid': userid,
            'tracks': tracks
        })

    else:
        form = UserForm()

        context = RequestContext(request, {
            'form': form,
            'userid': 'nobody'
        })

    print context

    return HttpResponse(template.render(context))
