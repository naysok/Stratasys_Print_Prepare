import Rhino.Geometry as rg
import rhinoscriptsyntax as rs


class rs_Command():


    def delete_all(self):
        query = "SelAll Delete"
        rs.Command(query)
    

    def capture_image_size_w_all_option(self, file_name, ww, hh):
        
        ### Change Viewport
        rs.CurrentView("Top")
        rs.ViewDisplayMode("Top", 'Rendered')
        
        ### Capture
        query = "-ViewCaptureToFile W={} H={} S=1 D=_No R=_No A=_No T=_Yes {}" \
            .format(ww, hh, file_name)
        rs.Command(query)
        
        ### Delete ALL
        self.delete_all()
        
        ### Change Viewport
        rs.CurrentView("Perspective")


    def capture_image_size(self, file_name, ww, hh):
        
        ### Change Viewport
        rs.CurrentView("Top")
        rs.ViewDisplayMode("Top", 'Rendered')
        
        ### Capture
        query = "-ViewCaptureToFile W={} H={} {}" \
            .format(ww, hh, file_name)
        rs.Command(query)
        
        ### Delete ALL
        self.delete_all()
        
        ### Change Viewport
        rs.CurrentView("Perspective")