# This very simple calculator was made using chatGPT to test it. 

# The question was: "Can you make a calculator in python with a user interface?""


from tkinter import *

# Define functions for calculator operations
def add():
    result.set(float(num1.get()) + float(num2.get()))

def subtract():
    result.set(float(num1.get()) - float(num2.get()))

def multiply():
    result.set(float(num1.get()) * float(num2.get()))

def divide():
    result.set(float(num1.get()) / float(num2.get()))

# Create the main window
root = Tk()
root.title("Calculator")

# Create the input fields
num1 = Entry(root, width=10)
num1.grid(row=0, column=0, padx=5, pady=5)

num2 = Entry(root, width=10)
num2.grid(row=0, column=2, padx=5, pady=5)

# Create the operation buttons
add_button = Button(root, text="+", width=5, command=add)
add_button.grid(row=1, column=0)

subtract_button = Button(root, text="-", width=5, command=subtract)
subtract_button.grid(row=1, column=1)

multiply_button = Button(root, text="*", width=5, command=multiply)
multiply_button.grid(row=1, column=2)

divide_button = Button(root, text="/", width=5, command=divide)
divide_button.grid(row=1, column=3)

# Create the result field
result = StringVar()
result.set("0")

result_field = Label(root, textvariable=result, width=10)
result_field.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()