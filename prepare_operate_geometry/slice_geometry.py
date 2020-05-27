import Rhino
import Rhino.Geometry as rg
import rhinoscriptsyntax as rs


import bake_geometry
reload(bake_geometry)

import create_geometry
reload(create_geometry)

import rs_command
reload(rs_command)

bg = bake_geometry.Bake_Geometry()
cg = create_geometry.Create_Geometry()
cmd = rs_command.rs_Command()


class Slice_Geometry():


    def slice_plane(self, target, plane):
        
        ### Slice
        p = rs.coerceplane(plane)
        
        ### Geomrtry Type
        if rs.IsMesh(target):
            # print("Mesh!!")
            m = rs.coercemesh(target)
            # print(m)
            polylines = rg.Intersect.Intersection.MeshPlane(m, p)
        
        elif rs.IsBrep(target):
            # print("Brep!")
            b = rs.coercebrep(target)
            mp = rg.MeshingParameters.QualityRenderMesh
            m = rg.Mesh.CreateFromBrep(b, mp)
            # print(m[0])
            polylines = rg.Intersect.Intersection.MeshPlane(m[0], p)
        
        else:
            # print("N/A")
            polylines = None
        
        return polylines


    def slicing(self, ghdoc_, path_, geometries, geometry_index, layer_height, whd):
        
        pic_size = 1000

        #######################################################################
        ### Base Size
        ### Create and Bake 
        rect_ = cg.create_rect(whd)
        bg.bake_breps(ghdoc_, rect_)

        ### Capture and Delete
        file_name = path_ + "size\\size.png"
        cmd.capture_image_size_w_all_option(file_name, pic_size, pic_size)

        ### Create and Bake
        rect_ = cg.create_rect(whd)
        bg.bake_breps(ghdoc_, rect_)

        ### Capture and Delete
        file_name = path_ + "size\\size.png"
        cmd.capture_image_size_w_all_option(file_name, pic_size, pic_size)
        #######################################################################

        slice_count = int(whd / layer_height) + 1
        # print(slice_count)

        ### Select geometry
        target = geometries[geometry_index]
        
        
        ### Slicing Loop
        sliced_surface = []
        v = []
        for i in xrange(slice_count):
            
            current_height = layer_height * i
            v.append(current_height)
            
            ### Mesh x Plane Intersection
            p = rs.MovePlane(rs.WorldXYPlane(), [0, 0, current_height])
            pl = self.slice_plane(target, p)
            
            ### Polyline to Surface
            if pl != None:
                # print(pl)
                surfaces = cg.create_surface_from_polylines(pl)
                # print(surfaces)
                # sliced_surface.append(surfaces)

                ### Bake Geometry
                bg.bake_breps(ghdoc_, surfaces)

            ### Capture and Delete
            gi_pad = "%03d"%geometry_index
            i_pad = "%05d"%i
            file_name = path_ + "{}\\{}.png".format(gi_pad, i_pad)
            cmd.capture_image_size(file_name, pic_size, pic_size)


        # return sliced_surface
        return v
        