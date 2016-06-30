from django.shortcuts import render
from django.http import HttpResponse
import os, threading, csv, tempfile
#from django.core.servers.basehttp import FileWrapper
#from wsgiref.util import FileWrapper


# Create your views here.

def index(request):
    return render(request, 'web_app/index.html')

lists = {'stories':'','dep_of_foun':'','plinth_lev':'','cclear_height':'',
    'dep_slab':'','rep_span_len':'','rep_span_wid':'','col_type':'',
        'len_col':'','wid_col':'',  'radius_col':'','dep_beam':'',
            'wid_beam':''}
lis = ['stories','dep_of_foun','plinth_lev','cclear_height','dep_slab','rep_span_len','rep_span_wid','col_type','len_col','wid_col','radius_col','dep_beam','wid_beam']

#bb = []

def specs(request):
    global lists
    global lis
    bb = list()
    for var in lists.keys():
        request.session[var] = request.POST.get(var)
        print("session  %s"  %request.session[var])
    print lists
#    print lists['rep_span_len']

    for i in lis:
        bb.append(request.POST.get(i))
    print("list is : %s" %bb)
    f = open('some.csv', 'w')
    ww = csv.writer(f, delimiter=' ')
    a = []
    for i in bb:
        a.append(i)
    ww.writerow(a)
    f.close()
    os.system('rm box.fcstd')
    l = os.system('freecadcmd macro_building_drawing.FCMacro')
#    print l
#    print request.POST
#    print len(request.POST)
    return render(request, 'web_app/specs.html', {'lists': lists})



def download(request):
    command = "project.fcstd"
    f = open(command)
    response = HttpResponse(f, content_type='application/fcstd')
    response['Content-Disposition'] = 'attachment; filename="project.fcstd"'
    return response
