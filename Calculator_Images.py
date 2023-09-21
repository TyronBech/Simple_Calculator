from PIL import Image, ImageTk

def resize_and_load_image(image_path, image_length=80, image_height=80):
    image = Image.open(image_path)
    resized_image = image.resize((image_length, image_height))
    photo_image = ImageTk.PhotoImage(resized_image)
    return photo_image

def resized_images():
    image_paths = [
        'Images/0.png',
        'Images/00.png',
        'Images/1.png',
        'Images/2.png',
        'Images/3.png',
        'Images/4.png',
        'Images/5.png',
        'Images/6.png',
        'Images/7.png',
        'Images/8.png',
        'Images/9.png',
        'Images/clear.png',
        'Images/difference.png',
        'Images/dot.png',
        'Images/equal.png',
        'Images/percent.png',
        'Images/product.png',
        'Images/quotient.png',
        'Images/remove.png',
        'Images/sum.png',
    ]

    images = [resize_and_load_image(image_path) for image_path in image_paths]
    return images