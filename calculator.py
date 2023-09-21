import tkinter as tk
from PIL import Image, ImageTk
from Calculator_Images import resized_images

if __name__ == '__main__':
    window = tk.Tk()
    window.title('Calculator')
    window.geometry("360x520")
    Buttons_img = resized_images()
    icon = tk.PhotoImage(file='Images\\Calculator_logo.png')
    window.iconphoto(True, icon)
    Button_one = tk.Button(window, image=Buttons_img[3], borderwidth=0)
    Button_one.grid(row=1, column=0)

    window.mainloop()