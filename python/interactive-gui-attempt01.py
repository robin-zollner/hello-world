import tkinter as tk
from tkinter import *
from tkinter import messagebox

global input_text

def displayText(event):
	l1.configure(text="Enetered Text: {}".format(e1.get()))

def recordData():
	input_text = e1.get()
	msg = messagebox.showinfo("Entered Info", input_text)
	return input_text


# varA = tk.StringVar()


def print_variable(*args):
	print(varA.get())


root = tk.Tk()
l1 = tk.Label(text="First Name: ")
l1.grid(row=0, column=0)
e1 = tk.Entry(root, textvariable="StringVar")
e1.grid(row=0, column=1, columnspan=1)
e1.bind("<Return>", displayText)
b1 = tk.Button(text='Submit', command=recordData)
b1.grid(row=1, column=5, columnspan=3)
b2 = tk.Button(text='Quit..motherfucker', command=root.quit)
b2.grid(row=1, column=1, columnspan=3)


# varA.trace("root", print_variable)
root.mainloop()