from django.shortcuts import render
from django.http import HttpResponse
import os, threading, csv, tempfile
#from django.core.servers.basehttp import FileWrapper
from wsgiref.util import FileWrapper


# Create your views here.

def index(request):
    return render(request, 'web_app/index.html')

lists = {'stories':'','dep_of_foun':'','plinth_lev':'','cclear_height':'',
    'dep_slab':'','rep_span_len':'','rep_span_wid':'','col_type':'',
        'len_col':'','wid_col':'',  'radius_col':'','dep_beam':'',
            'wid_beam':''}

def specs(request):
    global lists
    for var in lists.keys():
        lists[var] = request.POST.get(var)
    print lists['wid_col']
    print lists['rep_span_len']

    f = open('some.csv', 'w')
    ww = csv.writer(f, delimiter=' ')
    a = []
    for i in lists.keys():
        print lists[i]
        if lists[i] == None:
            a.append(0)
        else:
            a.append(lists[i])
    ww.writerow(a)
    f.close()
    os.system('rm box.fcstd')
    l = os.system('freecadcmd free_model.py')
    print l
    print request.POST
    print len(request.POST)
    return render(request, 'web_app/specs.html', {'lists': lists})



def download(request):
    command = "box.fcstd"
    f = open(command)
    response = HttpResponse(f, content_type='application/fcstd')
    response['Content-Disposition'] = 'attachment; filename="box.fcstd"'
    return response
