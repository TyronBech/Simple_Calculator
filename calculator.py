import tkinter as tk
from Calculator_Images import resized_images

def create_button(frame, image_index, command_type, b_row, b_column):
    button = tk.Button(
        frame,
        image=image_index,
        borderwidth=0,
        bg='black',
        activebackground='black',
        command=command_type
    )
    button.grid(row=b_row, column=b_column, padx=3, pady=3)
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
    Button_commands = [
        # Tuple indexing(index of the image, command per button, row, column)
        (0, lambda: delete_input(0), 0, 0),
        (1, lambda: pressed('%'), 0, 1),
        (2, lambda: delete_input(1), 0, 2),
        (3, lambda: pressed('/'), 0, 3),
        (4, lambda: pressed('7'), 1, 0),
        (5, lambda: pressed('8'), 1, 1),
        (6, lambda: pressed('9'), 1, 2),
        (7, lambda: pressed('*'), 1, 3),
        (8, lambda: pressed('4'), 2, 0),
        (9, lambda: pressed('5'), 2, 1),
        (10, lambda: pressed('6'), 2, 2),
        (11, lambda: pressed('-'), 2, 3),
        (12, lambda: pressed('1'), 3, 0),
        (13, lambda: pressed('2'), 3, 1),
        (14, lambda: pressed('3'), 3, 2),
        (15, lambda: pressed('+'), 3, 3),
        (16, lambda: pressed('00'), 4, 0),
        (17, lambda: pressed('0'), 4, 1),
        (18, lambda: pressed('.'), 4, 2),
        (19, result, 4, 3)
    ]
    # Creating a for loop to iterate the tuples and pass it as argument
    # to create a button
    for button_command in Button_commands:
        create_button(
            Button_Frame,
            Buttons_img[button_command[0]],
            button_command[1],
            button_command[2],
            button_command[3]
        )

    window.mainloop()