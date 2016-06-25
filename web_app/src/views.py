from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'web_app/index.html')

def specs(request):
    #list = {'length_of_box':'','width_of_box':'','height_of_box':''}
    ll = request.session.get('length')
    return render(request, 'web_app/specs.html', {'ll':ll})
