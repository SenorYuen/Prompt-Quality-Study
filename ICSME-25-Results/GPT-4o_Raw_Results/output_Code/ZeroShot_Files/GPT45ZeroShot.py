from PIL import Image, ImageEnhance

class ImageProcessor:
    def __init__(self):
        """
        Initialize self.image to None, indicating no image is loaded initially.
        """
        self.image = None

    def load_image(self, image_path):
        """
        Use Image util in PIL to open an image and store it in self.image.
        """
        self.image = Image.open(image_path)

    def save_image(self, save_path):
        """
        Save the image to a path if an image has been opened.
        """
        if self.image:
            self.image.save(save_path)
        else:
            raise ValueError("No image loaded to save.")

    def resize_image(self, width, height):
        """
        Resize the image to the given width and height if an image has been opened.
        """
        if self.image:
            self.image = self.image.resize((width, height))
        else:
            raise ValueError("No image loaded to resize.")

    def rotate_image(self, degrees):
        """
        Rotate the image by a specified number of degrees if an image has been opened.
        """
        if self.image:
            self.image = self.image.rotate(degrees)
        else:
            raise ValueError("No image loaded to rotate.")

    def adjust_brightness(self, factor):
        """
        Adjust the brightness of the image by a specified factor if an image has been opened.
        A factor > 1 increases brightness, while a factor < 1 decreases it.
        """
        if self.image:
            enhancer = ImageEnhance.Brightness(self.image)
            self.image = enhancer.enhance(factor)
        else:
            raise ValueError("No image loaded to adjust brightness.")