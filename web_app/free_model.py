import csv, FreeCAD, Part
#from FreeCAD import Base

import sys, os
#sys.path.insert(0, './src')

#from views import lists

#
#total = len(sys.argv)
#cmdargs = str(sys.argv)
#
#print total
#print cmdargs
#
#print "listsjdsljsldjldjljj"
#print lists
#

for arg in sys.argv:
    print arg


"""
f = open('some.csv')
sp = csv.reader(f, delimiter=' ')

for i in sp:
    lists = i

length = lists[0]
width = lists[1]
height = lists[2]

print length
print width
print height

FreeCAD.newDocument()
App.ActiveDocument=App.getDocument("Unnamed")

def box(name, l, w, h):
    App.ActiveDocument.addObject("Part::Box",name)
    box_ref = App.ActiveDocument.getObject(name)
    box_ref.Length = l
    box_ref.Width = w
    box_ref.Height = h

box("name", length, width, height)
App.getDocument("Unnamed").saveAs("./box.fcstd")
"""
