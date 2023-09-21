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
        'Images/0.png',         #0
        'Images/00.png',        #1
        'Images/1.png',         #2
        'Images/2.png',         #3
        'Images/3.png',         #4
        'Images/4.png',         #5
        'Images/5.png',         #6
        'Images/6.png',         #7
        'Images/7.png',         #8
        'Images/8.png',         #9
        'Images/9.png',         #10
        'Images/clear.png',     #11
        'Images/difference.png',#12
        'Images/dot.png',       #13
        'Images/equal.png',     #14
        'Images/percent.png',   #15
        'Images/product.png',   #16
        'Images/quotient.png',  #17
        'Images/remove.png',    #18
        'Images/sum.png',       #19
    ]
    images = [resize_and_load_image(image_path) for image_path in image_paths]
    return images