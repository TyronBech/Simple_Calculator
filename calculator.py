import tkinter as tk
from Calculator_Images import resized_images

# The pressed function is used to get every character to the button
# once pressed and display it to the label
def pressed(character):
    global input_text
    input_text = input_text + str(character)
    input_var.set(input_text)
# The result function will display the result of the
# input equation and also displays error if any errors encountered
def result():
    global input_text
    try:
        total = str(eval(input_text))
        input_var.set(total)
        input_text = total
    except ZeroDivisionError:
        input_var.set('arithmetic error')
        input_text = ''
    except SyntaxError:
        input_var.set('Syntax Error')
        input_text = ''
# The delete_input function will delete the input
# based on the given flag
# if flag is 0 then it will delete all the input
# if flag is not 0 then it will delete the last character
def delete_input(flag):
    global input_text
    if flag == 0:
        input_var.set('')
        input_text = ''
    else:
        input_var.set(input_text[:-1])
        input_text = input_text[:-1]


if __name__ == '__main__':
    # Creating an instance o the window and create all necessary
    # components for the application
    window = tk.Tk()
    window.title('Calculator')
    window.geometry("280x430")
    window.config(background='black')
    icon = tk.PhotoImage(file='Images\\Calculator_logo.png')
    window.iconphoto(True, icon)
    Buttons_img = resized_images()
    x_padding = 3
    y_padding = 3
    # this inputs and label is for the input of the user
    # also to display the character based on the button used
    input_text = ''
    input_var = tk.StringVar()
    input_label = tk.Label(window, textvariable=input_var, font=(
        'Arial', 25, 'bold'), bg='black', fg='white', width=310, height=2)
    input_label.pack()
    # This frame is where the buttons are stored
    Button_Frame = tk.Frame(window, bg='black')
    Button_Frame.pack()
    # This part are all button that will be used for the calculator
    bg_act_color = 'black'
    Button_clear = tk.Button(Button_Frame, image=Buttons_img[11], borderwidth=0,
                             bg=bg_act_color, activebackground=bg_act_color, command=lambda: delete_input(0))
    Button_clear.grid(row=1, column=0, padx=x_padding, pady=y_padding)
    Button_percent = tk.Button(
        Button_Frame, image=Buttons_img[15], borderwidth=0, bg=bg_act_color, activebackground=bg_act_color, command=lambda: pressed('%'))
    Button_percent.grid(row=1, column=1, padx=x_padding, pady=y_padding)
    Button_remove = tk.Button(
        Button_Frame, image=Buttons_img[18], borderwidth=0, bg=bg_act_color, activebackground=bg_act_color, command=lambda: delete_input(1))
    Button_remove.grid(row=1, column=2, padx=x_padding, pady=y_padding)
    Button_divide = tk.Button(
        Button_Frame, image=Buttons_img[17], borderwidth=0, bg=bg_act_color, activebackground=bg_act_color, command=lambda: pressed('/'))
    Button_divide.grid(row=1, column=3, padx=x_padding, pady=y_padding)
    Button_seven = tk.Button(
        Button_Frame, image=Buttons_img[8], borderwidth=0, bg=bg_act_color, activebackground=bg_act_color, command=lambda: pressed(7))
    Button_seven.grid(row=2, column=0, padx=x_padding, pady=y_padding)
    Button_eight = tk.Button(
        Button_Frame, image=Buttons_img[9], borderwidth=0, bg=bg_act_color, activebackground=bg_act_color, command=lambda: pressed(8))
    Button_eight.grid(row=2, column=1, padx=x_padding, pady=y_padding)
    Button_nine = tk.Button(
        Button_Frame, image=Buttons_img[10], borderwidth=0, bg=bg_act_color, activebackground=bg_act_color, command=lambda: pressed(9))
    Button_nine.grid(row=2, column=2, padx=x_padding, pady=y_padding)
    Button_multiply = tk.Button(
        Button_Frame, image=Buttons_img[16], borderwidth=0, bg=bg_act_color, activebackground=bg_act_color, command=lambda: pressed('*'))
    Button_multiply.grid(row=2, column=3, padx=x_padding, pady=y_padding)
    Button_four = tk.Button(
        Button_Frame, image=Buttons_img[5], borderwidth=0, bg=bg_act_color, activebackground=bg_act_color, command=lambda: pressed(4))
    Button_four.grid(row=3, column=0, padx=x_padding, pady=y_padding)
    Button_five = tk.Button(
        Button_Frame, image=Buttons_img[6], borderwidth=0, bg=bg_act_color, activebackground=bg_act_color, command=lambda: pressed(5))
    Button_five.grid(row=3, column=1, padx=x_padding, pady=y_padding)
    Button_six = tk.Button(
        Button_Frame, image=Buttons_img[7], borderwidth=0, bg=bg_act_color, activebackground=bg_act_color, command=lambda: pressed(6))
    Button_six.grid(row=3, column=2, padx=x_padding, pady=y_padding)
    Button_subtract = tk.Button(
        Button_Frame, image=Buttons_img[12], borderwidth=0, bg=bg_act_color, activebackground=bg_act_color, command=lambda: pressed('-'))
    Button_subtract.grid(row=3, column=3, padx=x_padding, pady=y_padding)
    Button_one = tk.Button(
        Button_Frame, image=Buttons_img[2], borderwidth=0, bg=bg_act_color, activebackground=bg_act_color, command=lambda: pressed(1))
    Button_one.grid(row=4, column=0, padx=x_padding, pady=y_padding)
    Button_two = tk.Button(
        Button_Frame, image=Buttons_img[3], borderwidth=0, bg=bg_act_color, activebackground=bg_act_color, command=lambda: pressed(2))
    Button_two.grid(row=4, column=1, padx=x_padding, pady=y_padding)
    Button_three = tk.Button(
        Button_Frame, image=Buttons_img[4], borderwidth=0, bg=bg_act_color, activebackground=bg_act_color, command=lambda: pressed(3))
    Button_three.grid(row=4, column=2, padx=x_padding, pady=y_padding)
    Button_add = tk.Button(Button_Frame, image=Buttons_img[19], borderwidth=0,
                           bg=bg_act_color, activebackground=bg_act_color, command=lambda: pressed('+'))
    Button_add.grid(row=4, column=3, padx=x_padding, pady=y_padding)
    Button_00 = tk.Button(Button_Frame, image=Buttons_img[1], borderwidth=0,
                          bg=bg_act_color, activebackground=bg_act_color, command=lambda: pressed('00'))
    Button_00.grid(row=5, column=0, padx=x_padding, pady=y_padding)
    Button_0 = tk.Button(Button_Frame, image=Buttons_img[0], borderwidth=0,
                         bg=bg_act_color, activebackground=bg_act_color, command=lambda: pressed(0))
    Button_0.grid(row=5, column=1, padx=x_padding, pady=y_padding)
    Button_dec = tk.Button(Button_Frame, image=Buttons_img[13], borderwidth=0,
                           bg=bg_act_color, activebackground=bg_act_color, command=lambda: pressed('.'))
    Button_dec.grid(row=5, column=2, padx=x_padding, pady=y_padding)
    Button_equal = tk.Button(
        Button_Frame, image=Buttons_img[14], borderwidth=0, bg=bg_act_color, activebackground=bg_act_color, command=result)
    Button_equal.grid(row=5, column=3, padx=x_padding, pady=y_padding)

    window.mainloop()