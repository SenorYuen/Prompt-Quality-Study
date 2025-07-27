from PIL import Image, ImageEnhance

class ImageProcessor:
    def __init__(self):
        self.image = None

    def load_image(self, image_path):
        self.image = Image.open(image_path)

    def save_image(self, save_path):
        if self.image is not None:
            self.image.save(save_path)
        else:
            raise ValueError("No image loaded")

    def resize_image(self, width, height):
        if self.image is not None:
            self.image = self.image.resize((width, height))
        else:
            raise ValueError("No image loaded")

    def rotate_image(self, degrees):
        if self.image is not None:
            self.image = self.image.rotate(degrees)
        else:
            raise ValueError("No image loaded")

    def adjust_brightness(self, factor):
        if self.image is not None:
            enhancer = ImageEnhance.Brightness(self.image)
            self.image = enhancer.enhance(factor)
        else:
            raise ValueError("No image loaded")