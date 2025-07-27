from PIL import Image, ImageEnhance

class ImageProcessor:
    """
    This is a class to process image, including loading, saving, resizing, rotating, and adjusting the brightness of images.
    """

    def __init__(self):
        # Initialize self.image
        self.image = None

    def load_image(self, image_path):
        # Use Image util in PIL to open a image
        try:
            self.image = Image.open(image_path)
        except Exception as e:
            print(f"Failed to load image: {e}")

    def save_image(self, save_path):
        # Save image to a path if image has opened
        if self.image:
            try:
                self.image.save(save_path)
            except Exception as e:
                print(f"Failed to save image: {e}")
        else:
            print("No image loaded")

    def resize_image(self, width, height):
        # Resize the image if image has opened
        if self.image:
            try:
                self.image = self.image.resize((width, height))
            except Exception as e:
                print(f"Failed to resize image: {e}")
        else:
            print("No image loaded")

    def rotate_image(self, degrees):
        # Rotate image if image has opened
        if self.image:
            try:
                self.image = self.image.rotate(degrees)
            except Exception as e:
                print(f"Failed to rotate image: {e}")
        else:
            print("No image loaded")

    def adjust_brightness(self, factor):
        # Adjust the brightness of image if image has opened
        if self.image:
            try:
                enhancer = ImageEnhance.Brightness(self.image)
                self.image = enhancer.enhance(factor)
            except Exception as e:
                print(f"Failed to adjust brightness: {e}")
        else:
            print("No image loaded")