# Importing the tkinter library


from tkinter import *

# Creating the main window


root = Tk()
root.title("Happy Calculator")
root.configure(bg="lightgrey")

# Creating an entry widget for displaying and inputting numbers


e = Entry(root, width=35, borderwidth=8, bg="white", fg="black")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# Initializing the global variables


f_num = 0      # to store the first number in a math operation. Initially set to 0.
math = ""      # initially set to an empty string ""

# Function to handle button clicks


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

# Clearing the entry field


def button_clear():
    e.delete(0, END)

# Addition


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

# Equal to perform calculation and display result


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        result = f_num + int(second_number)
        e.insert(0, str(result))
    elif math == "multiplication":
        result = f_num * int(second_number)
        e.insert(0, str(result))
    elif math == "division":
        result = f_num / int(second_number)
        e.insert(0, str(result))
    elif math == "substraction":
        result = f_num - int(second_number)
        e.insert(0, str(result))

# Multiplication


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

# Division


def button_division():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

# Substraction


def button_substraction():
    first_number = e.get()
    global f_num
    global math
    math = "substraction"
    f_num = int(first_number)
    e.delete(0, END)

# Creating buttons for numbers and operations


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1), bg="lightpink", fg="black")
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2), bg="lightpink", fg="black")
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), bg="lightpink", fg="black")
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4), bg="lightblue", fg="black")
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5), bg="lightblue", fg="black")
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6), bg="lightblue", fg="black")
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7), bg="lightgrey", fg="black")
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8), bg="lightgrey", fg="black")
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9), bg="lightgrey", fg="black")
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=button_add, bg="orange", fg="black")
button_equal = Button(root, text="=", padx=90, pady=20, command=button_equal, bg="orange", fg="black")
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear, bg="orange", fg="black")
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply, bg="orange", fg="black")
button_division = Button(root, text="/", padx=41, pady=20, command=button_division, bg="orange", fg="black")
button_substraction = Button(root, text="-", padx=41, pady=20, command=button_substraction, bg="orange", fg="black")

# Put the buttons on the screen, grid (rows and column)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_multiply.grid(row=6, column=0)
button_division.grid(row=6, column=1)
button_substraction.grid(row=6, column=2)

# Starting the main loop
root.mainloop()
