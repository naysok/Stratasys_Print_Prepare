import Rhino.Geometry as rg
import rhinoscriptsyntax as rs


class Create_Geometry():

    def create_rect(self, size_):
        
        geo = []
        
        size_ = float(size_)
        
        p0 = rg.Point3d(0, 0, 0)
        p1 = rg.Point3d(size_, 0, 0)
        p2 = rg.Point3d(size_, size_, 0)
        p3 = rg.Point3d(0, size_, 0)
        
        rc = rg.Brep.CreateFromCornerPoints(p0, p1, p2, p3, 0)
        
        geo.append(rc)
        
        return geo
    

    def create_box(self, size_):
        
        w = float(size_)
        h = float(size_)
        d = float(size_)
        
        p0 = rg.Point3d(0, 0, 0)
        p1 = rg.Point3d(w, 0, 0)
        p2 = rg.Point3d(w, d, 0)
        p3 = rg.Point3d(0, d, 0)
        p4 = rg.Point3d(0, 0, h)
        p5 = rg.Point3d(w, 0, h)
        p6 = rg.Point3d(w, d, h)
        p7 = rg.Point3d(0, d, h)
        
        
        box_ = rg.Brep.CreateFromBox([p0, p1, p2, p3, p4, p5, p6, p7])
        
        return box_
