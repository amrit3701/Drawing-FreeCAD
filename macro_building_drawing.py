a = FreeCAD.ActiveDocument.Objects
App.activeDocument().addObject("Part::Compound","Compound")
App.activeDocument().Compound.Links = a

App.ActiveDocument.addObject('Drawing::FeaturePage','Page')
App.ActiveDocument.Page.Template = App.getResourceDir()+'Mod/Drawing/Templates/A3_Landscape.svg'

App.ActiveDocument.addObject('Drawing::FeatureViewPart','View')
App.ActiveDocument.View.Source = App.ActiveDocument.Compound
App.ActiveDocument.View.Direction = (0.0,0.0,1.0)
App.ActiveDocument.View.X = 30.0
App.ActiveDocument.View.Y = 100.0
App.ActiveDocument.View.ShowHiddenLines = False
App.ActiveDocument.View.Scale = 2.0
App.ActiveDocument.Page.addObject(App.ActiveDocument.View)
App.ActiveDocument.recompute()

App.ActiveDocument.addObject('Drawing::FeatureViewPart','ViewIso')
App.ActiveDocument.ViewIso.Source = App.ActiveDocument.Compound
App.ActiveDocument.ViewIso.Direction = (1, 1, 1)
App.ActiveDocument.ViewIso.X = 335.0
App.ActiveDocument.ViewIso.Y = 60.0
App.ActiveDocument.ViewIso.ShowHiddenLines = True
App.ActiveDocument.ViewIso.Rotation = 120
App.ActiveDocument.ViewIso.Scale = 2.0
App.ActiveDocument.Page.addObject(App.ActiveDocument.ViewIso)
App.ActiveDocument.recompute()
