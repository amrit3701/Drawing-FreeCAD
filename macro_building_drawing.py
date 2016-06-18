# Storing all objects (i.e parts of building like column, beams and slabs)
# in obj_list
obj_list = FreeCAD.ActiveDocument.Objects

# Adding object 'Compound' in active document. The Compound object stores
# all parts of the building
App.activeDocument().addObject("Part::Compound","Compound")

# Links all the objects present in obj_list to Compound
App.activeDocument().Compound.Links = obj_list

# Adding the object 'Page' in active document
App.ActiveDocument.addObject('Drawing::FeaturePage','Page')

# Choose the specific template
App.ActiveDocument.Page.Template = App.getResourceDir()+'Mod/Drawing/Templates/A3_Landscape.svg'

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
class view_Specs:
    # Declaring a constructor
    def __init__(self, name, obj, x_dir, y_dir, z_dir, x_pos, y_pos, hid_lines, scale_size, rotation):
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

########################################################################
# The draw function projects the projections of the object on the
# drawing sheet. It takes the object of 'view_Specs' as argument, which
# stores all the detail which are require to draw the drawing of the
# object on the drawing sheet.
########################################################################
def draw(view):
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
    App.ActiveDocument.Page.addObject(view_ref)
    App.ActiveDocument.recompute()


view = view_Specs("view", "Compound", 0, 0, 1, 30, 100, False, 2, 0)
draw(view)

viewIso = view_Specs("viewIso", "Compound", 1, 1, 1, 335, 60, True, 2, 120)
draw(viewIso)
