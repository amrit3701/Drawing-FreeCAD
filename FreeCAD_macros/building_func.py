from building_specs import *
import string
import FreeCAD, Part#, PartGui
from FreeCAD import Base
ac_doc = FreeCAD.ActiveDocument

# Process span input (from config file).
def span_process(span_string):
    print 234
    # Remove leading and trailing whitespaces, and put in "span_st" variable.
    span_st=string.strip(span_string)
    # Split string contained in "span_st", where the "+" is encountered and put in span_sp array.
    span_sp=string.split(span_st, '+')
    index=0
    # Empty Array.
    list=[]
    while index < len(span_sp):

        # Find "@" recursively in span_sp array. If not found, append the index value to "list" array.
        if string.find(span_sp[index], '@')==-1:
            list.append(float(span_sp[index]))
        else:

        # If found, split the index value, where "@" is encountered, and put in in_sp array.
            in_sp=string.split(span_sp[index], '@')

            # Append the value written after "@" to "list" array for no. of times equal to the value written before "@".
            count=0
            while count < int(in_sp[0]):
                list.append(float(in_sp[1]))
                count+=1
        index+=1

    # Following statement will return the list of span inputs.
    return list

# Common function to create "box" shape that will be used for columns and beams.
def make_box(name, length, width, height, base_vector, base_rotation):
    ac_doc = FreeCAD.ActiveDocument
    ac_doc.addObject("Part::Box",name)
    getattr(ac_doc, name).Length = length
    getattr(ac_doc, name).Width = width
    getattr(ac_doc, name).Height = height
    getattr(ac_doc, name).Placement=Base.Placement(Base.Vector(base_vector[0],base_vector[1],base_vector[2]),Base.Rotation(base_rotation[0],base_rotation[1],base_rotation[2],base_rotation[3]))

# Function to create circular columns.
def make_cylinder(name, radius, height, base_vector, base_rotation):
    ac_doc = FreeCAD.ActiveDocument
    ac_doc.addObject("Part::Cylinder",name)
    getattr(ac_doc, name).Radius = radius
    getattr(ac_doc, name).Height= height
    getattr(ac_doc, name).Placement=Base.Placement(Base.Vector(base_vector[0],base_vector[1],base_vector[2]),Base.Rotation(base_rotation[0],base_rotation[1],base_rotation[2],base_rotation[3]))

# "dis_span_len" array contains list of "spans" length wise.
dis_span_len = span_process(rep_span_len)

# "dis_span_wid" array contains list of "spans" length wise.
dis_span_wid = span_process(rep_span_wid)

clear_height = span_process(cclear_height)

# Number of spans building's length wise.
no_spans_len = len(dis_span_len)

# Number of spans building's width wise.
no_span_wid = len(dis_span_wid)

# Function to show ground level and plinth level. It takes three inputs: 4 corners coordinates, length and breadth
def plane(start, l, w):
    p1 = FreeCAD.Vector(start[0],start[1],start[2])
    p2 = FreeCAD.Vector(start[0]+l,start[1],start[2])
    p3 = FreeCAD.Vector(start[0]+l,start[1]+w,start[2])
    p4 = FreeCAD.Vector(start[0],start[1]+w,start[2])
    pointslist = [p1, p2, p3, p4, p1]
    mywire = Part.makePolygon(pointslist)
    myface = Part.Face(mywire)
    Part.show(myface)

def z_sum(i):
    zsum = 0
    index = 0
    while index < i:
        # zsum = zsum + clear_height[index] + dep_slab - dep_beam/2.0 + ((dep_beam/2.0) * index)
        # zsum = zsum + clear_height[index]
                zsum = zsum + clear_height[index] + dep_beam
                if(index == 0):
                    zsum = zsum - dep_beam/2.0
                index = index + 1
    return zsum

# Sums the total length of all spans, building's length wise.
def x_sum(i):
    xsum = 0
    index = 0
    while index <= i-1 and i!=0:
        xsum = xsum + dis_span_len[index]
        index = index + 1
    return xsum

# Sums the total length of all spans, building's width wise.
def y_sum(i):
    ysum = 0
    index = 0
    while index <= i-1 and i!=0:
        ysum = ysum + dis_span_len[index]
        index = index + 1
    return ysum

