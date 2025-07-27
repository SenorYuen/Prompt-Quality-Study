# This is a class to process image, including loading, saving, resizing, rotating, and adjusting the brightness of images.
from PIL import Image, ImageEnhance

class ImageProcessor:
    def __init__(self):
        # Initialize self.image as None
        self.image = None

    def load_image(self, image_path):
        # Use Image util in PIL to open a image
        try:
            self.image = Image.open(image_path)
        except FileNotFoundError:
            print("File not found. Please check the image path.")

    def save_image(self, save_path):
        # Save image to a path if image has opened
        if self.image is not None:
            self.image.save(save_path)
        else:
            print("No image has been loaded.")

    def resize_image(self, width, height):
        # Resize the image if image has opened
        if self.image is not None:
            self.image = self.image.resize((width, height))
        else:
            print("No image has been loaded.")

    def rotate_image(self, degrees):
        # Rotate image if image has opened
        if self.image is not None:
            self.image = self.image.rotate(degrees)
        else:
            print("No image has been loaded.")

    def adjust_brightness(self, factor):
        # Adjust the brightness of image if image has opened
        if self.image is not None:
            enhancer = ImageEnhance.Brightness(self.image)
            self.image = enhancer.enhance(factor)
        else:
            print("No image has been loaded.")


# Example usage:
if __name__ == "__main__":
    processor = ImageProcessor()
    processor.load_image("path_to_your_image.jpg")
    processor.resize_image(800, 600)
    processor.rotate_image(45)
    processor.adjust_brightness(1.5)
    processor.save_image("processed_image.jpg")