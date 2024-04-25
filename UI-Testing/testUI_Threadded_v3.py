import tkinter as tk
from tkinter import messagebox, simpledialog
import threading
import time

def create_buttons(num_buttons):
    global button_window
    button_window = tk.Toplevel()
    button_window.title("Button Selector")
    button_window.protocol("WM_DELETE_WINDOW", close_program)

    for i in range(num_buttons):
        button = tk.Button(button_window, text=f"Button {i+1}", command=lambda idx=i+1: on_button_press(idx))
        button.pack()

    # Add "Add Server IP" button
    add_button = tk.Button(button_window, text="Add Server IP", command=add_server_ip)
    add_button.pack()

def on_button_press(button_number):
    threading.Thread(target=show_popup, args=(button_number,)).start()

def show_popup(button_number):
    messagebox.showinfo("Button Pressed", f"Button {button_number} was pressed!")
    time.sleep(2)  # Simulating some work

def close_program():
    root.destroy()

# Read the number of buttons from the "iplist.txt" file
def read_num_buttons():
    try:
        with open("iplist.txt", "r") as file:
            lines = file.readlines()
            return len(lines) - 1  # First row is reserved for the "Type '0' to add an IP" message
    except FileNotFoundError:
        messagebox.showerror("File Not Found", "The file 'iplist.txt' was not found.")
        return 0

# Add a new server IP
def add_server_ip():
    new_ip = simpledialog.askstring("Add Server IP", "Enter the new IP address:")
    if new_ip is not None:
        try:
            with open("iplist.txt", "r+") as file:
                lines = file.readlines()
                if lines[-1][-1] != '\n':# Edge-case for the text file - Check if the "final row" has a newline @ the end of it (aka, blank final row)
                    file.write("\n")  # Add a new blank row if not empty
                file.write(new_ip + "\n")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add IP: {e}")
    # Close the current window and re-launch Button Selector window
    button_window.destroy()
    main()

# Main function to create buttons
def main():
    num_buttons = read_num_buttons() + 1  # Add one more button for "Add Server IP"
    if num_buttons > 0:
        create_buttons(num_buttons)
    else:
        close_program()

# Main window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Call the main function
main()

root.mainloop()

