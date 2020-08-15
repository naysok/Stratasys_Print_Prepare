import sys
sys.path.append('C:\\Users\\ysoky\\Documents\\Digital_Artisan\\Stratasys_Print_Prepare')


##############################



from prepare_image_processing import image_processing, util

im = image_processing.ImageProcessing()
ut = util.Utill()


##############################


### TEST
path_ex = "C:\\Users\\ysoky\\Documents\\Digital_Artisan\\Stratasys_Print_Prepare\\images\\test\\{}.png".format(ut.get_current_time())

# path_0 = "C:\\Users\\ysoky\\Documents\\Digital_Artisan\\Stratasys_Print_Prepare\\images\\size_bu\\size.png"
path_0 = "C:\\Users\\ysoky\\Documents\\Digital_Artisan\\Stratasys_Print_Prepare\\images\\size_bu\\size_edit.png"


##############################


##################################
###                            ###
###   DEFINE IMAGE SIZE TOOL   ###
###                            ###
##################################


### OPEN
base_img = im.open_image(path_0)
# base_img.show()


### GET SIZE
point0 = [106, 121]
point1 = [918, 933]
new_size = [point1[0] - point0[0], point1[1] - point0[1]]
# print(new_size)

# draw_img = im.draw_crosshair(base_img, point0)
# draw_img = im.draw_crosshair(base_img, point1)
# draw_img = im.draw_x_line(base_img, point0, point1)
# draw_img.show()


### TRIM
trim_img = im.trim_w_offset(base_img, new_size[0], point0)
# trim_img.show()


### BINARIZE
bin_img = im.binarize_image(trim_img, 230)
bin_img.show()


### SCALE
resize_img = im.change_scale(bin_img, 800)


export_img = resize_img
im.export_image(export_img, path_ex)