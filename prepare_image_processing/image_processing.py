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


    def draw_crosshair(self, pos_x, pos_y):
        pass


    def scale_by_target_size(self):
        pass