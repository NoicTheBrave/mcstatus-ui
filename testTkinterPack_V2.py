import tkinter as tk

def open_menu():
    # Create a new window for the menu
    menu_window = tk.Toplevel(root)
    
    # Create a frame for the menu buttons
    menu_frame = tk.Frame(menu_window)
    menu_frame.pack()
    
    # Create three buttons inside the menu frame
    menu_button1 = tk.Button(menu_frame, text="Menu Button 1")
    menu_button2 = tk.Button(menu_frame, text="Menu Button 2")
    menu_button3 = tk.Button(menu_frame, text="Menu Button 3")
    
    # Pack the buttons to position them vertically within the menu frame
    menu_button1.pack()
    menu_button2.pack()
    menu_button3.pack()

# Create the main window
root = tk.Tk()

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Create three buttons inside the button frame
button1 = tk.Button(button_frame, text="Button 1", command=open_menu)
button2 = tk.Button(button_frame, text="Button 2", command=open_menu)
button3 = tk.Button(button_frame, text="Button 3", command=open_menu)

# Pack the buttons to position them horizontally within the button frame
button1.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT)
button3.pack(side=tk.LEFT)

# Create a frame for the text widget
text_frame = tk.Frame(root)
text_frame.pack()

# Create a text widget inside the text frame
text_widget = tk.Text(text_frame, height=5, width=30)
text_widget.pack()

# Start the main event loop
root.mainloop()
