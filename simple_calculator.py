from tkinter import *

# Create main window and title
root = Tk()
root.title("Simple Calculator")

# Create and place the number display for the calculator inside the main root window
e = Entry(root, width=41, justify=RIGHT, borderwidth=5)
e.grid(row=0, columnspan=5)

# Define button functions	
def button_click(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def button_click_dot():
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + ".")

def button_clear():
	e.delete(0, END)

def button_add():
	first_number = e.get()
	global f_num
	global math
	math = "addition"
	f_num = first_number
	e.delete(0, END)

def button_subtract():
	first_number = e.get()
	global f_num
	global math
	math = "subtraction"
	f_num = first_number
	e.delete(0, END)

def button_multiply():
	first_number = e.get()
	global f_num
	global math
	math = "multiply"
	f_num = first_number
	e.delete(0, END)

def button_divide():
	first_number = e.get()
	global f_num
	global math
	math = "divide"
	f_num = first_number
	e.delete(0, END)

def button_equals():
	second_number = e.get()
	e.delete(0, END)
	if math == "addition":
		answer = float(f_num) + float(second_number)
	elif math == "subtraction":
		answer = float(f_num) - float(second_number)
	elif math == "multiply":
		answer = float(f_num) * float(second_number)
	elif math == "divide":
		answer = float(f_num) / float(second_number)
	e.insert(0, float(answer))
	
# Create and place buttons on the calculator in the main root window	

button1 = Button(root, text="1", padx=30, pady=20, command=lambda: button_click(1)).grid(row=1, column=0)
button2 = Button(root, text="2", padx=30, pady=20, command=lambda: button_click(2)).grid(row=1, column=1)
button3 = Button(root, text="3", padx=30, pady=20, command=lambda: button_click(3)).grid(row=1, column=2)

button4 = Button(root, text="4", padx=30, pady=20, command=lambda: button_click(4)).grid(row=2, column=0)
button5 = Button(root, text="5", padx=30, pady=20, command=lambda: button_click(5)).grid(row=2, column=1)
button6 = Button(root, text="6", padx=30, pady=20, command=lambda: button_click(6)).grid(row=2, column=2)

button7 = Button(root, text="7", padx=30, pady=20, command=lambda: button_click(7)).grid(row=3, column=0)
button8 = Button(root, text="8", padx=30, pady=20, command=lambda: button_click(8)).grid(row=3, column=1)
button9 = Button(root, text="9", padx=30, pady=20, command=lambda: button_click(9)).grid(row=3, column=2)

button0 = Button(root, text="0", padx=69, pady=20, command=lambda: button_click(0)).grid(row=4, column=0, columnspan=2)

button_dot = Button(root, text=".", padx=32, pady=20, command=button_click_dot).grid(row=4, column=2)
	
buttonClear = Button(root, text="Clear", padx=55, pady=20, command=button_clear).grid(row=4, column=3, columnspan=2)	

button_add = Button(root, text="+", padx=30, pady=20, command=button_add).grid(row=1, column=3)
button_subtract = Button(root, text="-", padx=31, pady=20, command=button_subtract).grid(row=2, column=3)
button_multiply = Button(root, text="*", padx=29, pady=20, command=button_multiply).grid(row=1, column=4)
button_divide = Button(root, text="/", padx=30, pady=20, command=button_divide).grid(row=2, column=4)

button_equals = Button(root, text="=", padx=68, pady=20, command=button_equals).grid(row=3, column=3, columnspan=2)

# Run the main program loop
root.mainloop()

















