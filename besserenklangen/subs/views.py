from django.http import HttpResponse
from django.template import loader

def index(request):
    context = { 'message': 'generated message' }
    template = loader.get_template('subs/index.html')
    return HttpResponse(template.render(context))

def about(request):
    return HttpResponse("<h1>besserenklangen</h1><a href='/subs'>index</a>")