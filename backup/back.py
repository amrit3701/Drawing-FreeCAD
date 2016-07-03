stories=8                       #Number of stories

dep_of_foun=6.0                 #Depth of Foundation

plinth_lev=4.0                  #Plinth level of building

cclear_height="3@10+30+6+3@8"            #Clear Height of each story

dep_slab=1                    #Depth of Slab

#rep_span_len="2@8+9+1@10+2@12"  #Representation of span length
rep_span_len="4@8"

#rep_span_wid="2@7+6+1@5"       #Representation of span width
rep_span_wid="4@8"

col_type=1                      #Column type 0 for cylindrical and 1 for rectangular

len_col=1                       #Length of Column (for column type 1)

wid_col=1                       #Width of Column (for column type 1)

radius_col=.5                   #Radius of column (for column type 0)

dep_beam=2                      #Depth of Beam

wid_beam=1                      #Width of Beam


import string
import FreeCAD, Part#, PartGui
from FreeCAD import Base
ac_doc = FreeCAD.ActiveDocument

App.newDocument("project")
App.setActiveDocument("project")

# Process span input (from config file).
def span_process(span_string):

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


i = 0
j = 0
k = 0
nodes = []
z = 0
#Drawing ground plane to depict ground level
plane([-3, -3, plinth_lev - 2 * plinth_lev], x_sum(no_spans_len) + 6, y_sum(no_span_wid) + 6)

#Drawing plinth plane to depict plinth level
plane([0, 0, 0], x_sum(no_spans_len), y_sum(no_span_wid))

while z <= stories:
	x = 0
	while x <= no_spans_len:
		y = 0
		while y <= no_span_wid:
			coords = [x_sum(x), y_sum(y), z_sum(z)]
			nodes.append(coords)

			# If building is 0 storey, height will be equal to ground level
			if z == 0:
				col_name = "Column" + str(i)
				i = i + 1

				# If column is rectangular
				if col_type == 1:
				 	make_box(col_name, len_col, wid_col, dep_of_foun + plinth_lev, [coords[0] - len_col / 2.0, coords[1] - wid_col / 2.0, dep_of_foun + plinth_lev - 2 * (dep_of_foun + plinth_lev)], [0.00, 0.00, 0.00, 1.00])

				# If column is cylinderical
				else:
				 	make_cylinder(col_name, radius_col, dep_of_foun + plinth_lev, [coords[0], coords[1], dep_of_foun + plinth_lev - 2 * (dep_of_foun + plinth_lev)], [0.00, 0.00, 0.00, 1.00])
			else:
				col_name = "Column" + str(i)
				i = i + 1
				if col_type == 1:
                                        # make_box(name, length, width, height, base_vector, base_rotation)
					make_box(col_name, len_col, wid_col, z_sum(z) -  z_sum(z-1), [coords[0] - len_col/2.0, coords[1] - wid_col/2.0, z_sum(z-1)], [0.00, 0.00, 0.00, 1.00])
				else:
					make_cylinder(col_name, radius_col, z_sum(z) - z_sum(z-1), [coords[0], coords[1], z_sum(z-1)], [0.00, 0.00, 0.00, 1.00])

			# Creating beams width wise.
			if y != 0 and z != 0:
				beam_name = "Beam" + str(j)
				j = j + 1
				make_box(beam_name, wid_beam, y_sum(y) - y_sum(y - 1), dep_beam, [coords[0] - wid_beam / 2.0, y_sum(y - 1), z_sum(z) - dep_beam / 2.0], [0.00, 0.00, 0.00, 1.00])

			# Creating beams length wise.
			if x != 0 and z != 0:
				beam_name = "Beam" + str(j)
				j = j + 1
				make_box(beam_name, x_sum(x) - x_sum(x - 1), wid_beam, dep_beam, [x_sum(x - 1), coords[1] - wid_beam / 2.0, z_sum(z) - dep_beam / 2.0], [0.00, 0.00, 0.00, 1.00])

			y = y + 1
		x = x + 1

	# If building has some height, i.e. "z != 0", only then slab can come into existance.
	if z != 0:
		slab_name = "Slab" + str(k)
		k = k + 1
		make_box(slab_name, x_sum(no_spans_len), y_sum(no_span_wid), dep_slab, [0, 0, z_sum(z) + dep_beam / 2.0 - dep_slab], [0.00, 0.00, 0.00, 1.00])

	z = z + 1
#FreeCAD.Gui.SendMsgToActiveView("ViewFit")
#FreeCAD.Gui.activeDocument().activeView().viewAxometric()
FreeCAD.Console.PrintMessage("fdfffdf\n")
print z_sum
#App.getDocument("Unnamed").saveAs("/home/ambu/Desktop/delete.fcstd")
#print nodes[1][1]

import Arch, Draft, Drawing

# Storing all objects (i.e parts of building like column, beams and slabs)
# in obj_list
obj_list = FreeCAD.ActiveDocument.Objects

# Adding object 'Compound' in active document. The Compound object stores
# all parts of the building
App.activeDocument().addObject("Part::Compound","Compound")
App.activeDocument().Compound.Links = obj_list
# Links all the objects present in obj_list to Compound
#App.activeDocument().Compound.Links = obj_list
#App.getDocument("projecting").saveAs("/home/ambu/Documents/Drawing-FreeCAD/projecting.fcstd")

# Adding the object 'Page' in active document
# App.ActiveDocument.addObject('Drawing::FeaturePage','Page')

# Choose the specific template
# App.ActiveDocument.Page.Template = App.getResourceDir()+'Mod/Drawing/Templates/A3_Landscape.svg'

########################################################################
# This class stores all the information which is require to draw the
# drawing of different objects on the drawing sheet.
#
# name: It represent the name of the view.
#
# obj: It store the name of the object which can be draw on drawing sheet
#
# x_dir y_dir z_dir: These are the axis like (x_dir, y_dir, z_dir) from
# which point source can see the object.
#
# x_pos y_pos: It represents position of the drawing to be drawn on a
# drawing sheet.
#
# hid_lines: If it is 'True' then all hidden lines is drawn on the drawing
# sheet.
#
# scale_size: It represent the size to be draw on the drawing sheet.
#
# rotation: If it is 90 then the view on the drawing sheet is rotate
# 90 degree.
########################################################################
"""class obj_view_specs:
    # Declaring a constructor
    def __init__(self, name, obj, x_dir, y_dir, z_dir, x_pos, y_pos, hid_lines,
            scale_size, rotation, page):
        self.name = name
        self.obj = obj
        self.x_dir = x_dir
        self.y_dir = y_dir
        self.z_dir = z_dir
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.hid_lines = hid_lines
        self.scale_size = scale_size
        self.rotation = rotation
        self.page = page

    ########################################################################
    # The draw function projects the projections of the object on the
    # drawing sheet. It takes the object of 'view_Specs' as argument, which
    # stores all the detail which are require to draw the drawing of the
    # object on the drawing sheet.
    ########################################################################
    def draw_obj_view(view):
        App.ActiveDocument.addObject('Drawing::FeaturePage',view.page)
        page_ref = App.ActiveDocument.getObject(view.page)
# Choose the specific template
        page_ref.Template = App.getResourceDir()+'Mod/Drawing/Templates/A3_Landscape.svg'


        # Add the object in the active document of specific name
        App.ActiveDocument.addObject('Drawing::FeatureViewPart',view.name)
        # view_ref stores the object having name view.name
        view_ref = App.ActiveDocument.getObject(view.name)
        # obj_ref stores the object having name view.obj
        obj_ref = App.ActiveDocument.getObject(view.obj)
        view_ref.Source = obj_ref
        view_ref.Direction = (view.x_dir, view.y_dir, view.z_dir)
        view_ref.X = view.x_pos
        view_ref.Y = view.y_pos
        view_ref.ShowHiddenLines = view.hid_lines
        view_ref.Scale = view.scale_size
        view_ref.Rotation = view.rotation
        #page_ref = App.ActiveDocument.getObject(page_name)
        page_ref.addObject(view_ref)
        App.ActiveDocument.recompute()



view = obj_view_specs("view", "Compound", 0, 0, 1, 30, 100, False, 2, 0, "page")
obj_view_specs.draw_obj_view(view)
"""
#App.activeDocument().Compound.Links = obj_list
App.getDocument("project").saveAs("/home/ambu/Documents/Drawing-FreeCAD/project.fcstd")

