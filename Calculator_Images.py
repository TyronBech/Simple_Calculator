from PIL import Image, ImageTk

# The function resize_and_load_image is going to resize the image
# based on the given length ang height
def resize_and_load_image(image_path, image_length=60, image_height=60):
    image = Image.open(image_path)
    resized_image = image.resize((image_length, image_height))
    photo_image = ImageTk.PhotoImage(resized_image)
    return photo_image

# The functio resized_images is the function to be used in the main
# modul, it contains the file of the images and used list comprehension
# to resize each images
def resized_images():
    image_paths = [
        'Images/clear.png',     #0
        'Images/percent.png',   #1
        'Images/remove.png',    #2
        'Images/quotient.png',  #3
        'Images/7.png',         #4
        'Images/8.png',         #5
        'Images/9.png',         #6
        'Images/product.png',   #7
        'Images/4.png',         #8
        'Images/5.png',         #9
        'Images/6.png',         #10
        'Images/difference.png',#11
        'Images/1.png',         #12
        'Images/2.png',         #13
        'Images/3.png',         #14
        'Images/sum.png',       #15
        'Images/00.png',        #16
        'Images/0.png',         #17
        'Images/dot.png',       #18
        'Images/equal.png',     #19
    ]
    images = [resize_and_load_image(image_path) for image_path in image_paths]
    return images