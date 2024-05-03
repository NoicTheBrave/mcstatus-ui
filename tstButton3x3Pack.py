import tkinter as tk

def button_click():
    print("Button clicked")

def create_popup():
    popup = tk.Toplevel(root)

    for i in range(3):
        button_frame = tk.Frame(popup)
        button_frame.pack()
        for j in range(3):
            button = tk.Button(button_frame, text=f"Button {i*3 + j + 1}", command=button_click, width=10, height=2)
            button.pack(side=tk.LEFT, padx=5, pady=5)

root = tk.Tk()
root.title("Pop-up with Buttons")

popup_button = tk.Button(root, text="Create Pop-up", command=create_popup)
popup_button.pack(pady=10)

root.mainloop()
