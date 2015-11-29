from django.conf.urls import patterns, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^track', views.track, name='track'),
    url(r'^list', views.list, name='list')
]