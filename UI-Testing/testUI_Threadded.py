import tkinter as tk
from tkinter import messagebox
import threading
import time

def create_buttons(num_buttons):
    button_window = tk.Toplevel(root)
    button_window.title("Button Selector")

    for i in range(num_buttons):
        button = tk.Button(button_window, text=f"Button {i+1}", command=lambda idx=i+1: on_button_press(idx))
        button.pack()

def on_button_press(button_number):
    threading.Thread(target=show_popup, args=(button_number,)).start()

def show_popup(button_number):
    messagebox.showinfo("Button Pressed", f"Button {button_number} was pressed!")
    time.sleep(2)  # Simulating some work

def get_num_buttons():
    num_buttons = int(entry.get())
    if num_buttons > 0:
        create_buttons(num_buttons)
        root.withdraw()  # Hide the initial window
    else:
        messagebox.showwarning("Invalid Input", "Please enter a positive number of buttons.")

# Main window
root = tk.Tk()
root.title("Button Counter")

label = tk.Label(root, text="Enter the number of buttons to create:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Create Buttons", command=get_num_buttons)
button.pack()

root.mainloop()
