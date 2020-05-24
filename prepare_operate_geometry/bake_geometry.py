import Rhino
import scriptcontext as sc


class Bake_Geometry():

    def bake_breps(self, ghdoc_, breps):    
    
        ### Set Default
        sc.doc = ghdoc_
        
        ### Bake Brep
        sc.doc = Rhino.RhinoDoc.ActiveDoc
        for i in xrange(len(breps)):
            sc.doc.Objects.AddBrep(breps[i])
        
        ### Set Default
        sc.doc = ghdoc_
