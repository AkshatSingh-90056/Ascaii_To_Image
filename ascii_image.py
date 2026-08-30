import numpy as np
from PIL import Image


ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)  
    resized_image = image.resize((new_width, new_height))
    return resized_image

def to_grayscale(image):
    return image.convert("L")

def map_pixels_to_ascii(image):
    pixels = np.array(image)
    ascii_str = ""
    scale = len(ASCII_CHARS) - 1
    for row in pixels:
        for pixel in row:
            ascii_str += ASCII_CHARS[int(pixel / 255 * scale)]
        ascii_str += "\n"
    return ascii_str

def image_to_ascii(image_path, width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print("Error opening image:", e)
        return
    image = resize_image(image, width)
    image = to_grayscale(image)
    ascii_art = map_pixels_to_ascii(image)
    return ascii_art

if __name__ == "__main__":
    image_path = "website.jpg"  
    ascii_output = image_to_ascii(image_path, width=100)
    print(ascii_output)

