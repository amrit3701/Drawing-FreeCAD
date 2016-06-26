from django.shortcuts import render
from django.http import HttpResponse
import os, threading, csv, tempfile
#from django.core.servers.basehttp import FileWrapper
from wsgiref.util import FileWrapper


# Create your views here.

def index(request):
    return render(request, 'web_app/index.html')

def specs(request):
    #lists = {'length':'','width':'','height':''}
    #ll = request.POST['length']

    """for var in lists.keys():
        #print var
        lists[var] = request.POST.get(var)
        print request.session[var]
        print lists"""
    #ll = lists
    length = request.POST.get('length_box')
    width = request.POST.get('width_box')
    height = request.POST.get('height_box')

    f = open('some.csv', 'w')
    ww = csv.writer(f, delimiter=' ')
    ww.writerow([length, width, height])
    f.close()
    os.system('rm box.fcstd')
    l = os.system('freecadcmd free_model.py')
    print l
    print request.POST
    print len(request.POST)
    return render(request, 'web_app/specs.html', {'length': length, 'width': width, 'height': height})


def download(request):
    command = "box.fcstd"
    f = open(command)
    response = HttpResponse(f, content_type='application/fcstd')
    response['Content-Disposition'] = 'attachment; filename="box.fcstd"'
    return response
