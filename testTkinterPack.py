import tkinter as tk

# Create the main window
root = tk.Tk()

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Create three buttons inside the button frame
button1 = tk.Button(button_frame, text="Button 1")
button2 = tk.Button(button_frame, text="Button 2")
button3 = tk.Button(button_frame, text="Button 3")

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
