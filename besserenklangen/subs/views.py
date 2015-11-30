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
    context = { "message":  request}
    return render(request, 'subs/index.html', context)

def about(request):
    return render(request, 'subs/about.html')

def track(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.cleaned_data['username']
            raw_feed = build_feed(user)

            f = Feed(username = user)
            f.save()

            for track in raw_feed:
                t = Track(id = track[0]
                        , date = track[1]
                        , title = track[2]
                        , artist = track[3]
                        , uri = track[4])
                t.save()

                f.tracks.add(t)

            return HttpResponseRedirect('track.html')
    else:
        form = UserForm()

    return render(request, 'subs/track.html', { 'form': form })

def list(request):
    tracks = Feed.objects.get(username='meepokid').tracks.all().order_by('-date')
    template = loader.get_template('subs/list.html')
    context = RequestContext(request, {
        'tracks': tracks,
    })
    return HttpResponse(template.render(context))
