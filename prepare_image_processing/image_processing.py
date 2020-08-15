from PIL import Image, ImageDraw

class ImageProcessing():


    def open_image(self, path):
        img = Image.open(path)
        return img


    def export_image(self, img, path):
        img.save(path, quality=100)
        print("Export : {}".format(path))


    def binarize_image(self, img, th):

        gray = img.convert("L")# グレイスケールに変換
        gray.point(lambda x: 0 if x < th else x) # 値が230以下は0になる

        return gray


    def draw_crosshair(self, img, pt):
        draw = ImageDraw.Draw(img)
        posx, posy = pt
        draw.line((posx, 0, posx, img.height), fill=(0, 255, 0))
        draw.line((0, posy, img.width, posy), fill=(0, 0, 255))
        return img


    def draw_x_line(self, img, pt0, pt1):
        draw = ImageDraw.Draw(img)
        posx0, posy0 = pt0
        posx1, posy1 = pt1
        draw.line((posx0, posy0, posx1, posy1), fill=(0, 255, 0))
        draw.line((posx0, posy1, posx1, posy0), fill=(0, 0, 255))
        return img


    def trim_w_offset(self, paste_img, canvas_size, off):
        new = Image.new("RGBA", (canvas_size, canvas_size), (0, 0, 0, 0))
        off_x, off_y = off
        new.paste(paste_img, (off_x * (-1), off_y * (-1)))
        return new


    def change_scale(self, img, target_size):
        img_resize = img.resize((target_size, target_size), Image.LANCZOS)
        return img_resize