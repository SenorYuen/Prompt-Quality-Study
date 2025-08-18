'''
# This is a class to process image, including loading, saving, resizing, rotating, and adjusting the brightness of images.

from PIL import Image, ImageEnhance

class ImageProcessor:
    def __init__(self):
        """
        Initialize self.image
        """

    def load_image(self, image_path):
        """
        Use Image util in PIL to open a image
        """

    def save_image(self, save_path):
        """
        Save image to a path if image has opened
        """

    def resize_image(self, width, height):
        """
        Risize the image if image has opened.
        """

    def rotate_image(self, degrees):
        """
        rotate image if image has opened
        """

    def adjust_brightness(self, factor):
        """
        Adjust the brightness of image if image has opened.
        """
'''

from PIL import Image, ImageEnhance, ImageChops


class ImageProcessor:
    def __init__(self):
        self.image = None

    def load_image(self, image_path):
        self.image = Image.open(image_path)

    def save_image(self, save_path):
        if self.image:
            self.image.save(save_path)

    def resize_image(self, width, height):
        if self.image:
            self.image = self.image.resize((width, height))

    def rotate_image(self, degrees):
        if self.image:
            self.image = self.image.rotate(degrees)

    def adjust_brightness(self, factor):
        if self.image:
            enhancer = ImageEnhance.Brightness(self.image)
            self.image = enhancer.enhance(factor)
