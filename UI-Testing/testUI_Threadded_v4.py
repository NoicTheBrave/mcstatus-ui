import tkinter as tk
from tkinter import messagebox, simpledialog
import threading
import time

from mcstatus import JavaServer

def create_buttons(num_buttons):
    global button_window
    button_window = tk.Toplevel()
    button_window.title("Button Selector")
    button_window.protocol("WM_DELETE_WINDOW", close_program)
    
    #Top Lable added - Exsessive spaces are there to help expand the window out more artificially VS setting an acutal window size :P 
    label = tk.Label(button_window, text="                     Press a Button to get started:                     ")
    label.pack()

    with open("iplist.txt", "r") as file:
        lines = file.readlines()[1:]  # Skip the first line
        for i in range(num_buttons):
            if i < len(lines):
                ip_address = lines[i].strip()
            else:
                ip_address = ""
            button = tk.Button(button_window, text=ip_address, command=lambda idx=i: on_button_press(idx))
            button.pack()

    # Add "Add Server IP" button
    add_button = tk.Button(button_window, text="Add Server IP", command=add_server_ip)
    add_button.pack()

def on_button_press(button_index):
    threading.Thread(target=show_popup, args=(button_index,)).start()

def show_popup(button_index):
    ip_address = get_ip_address(button_index)
    popup_window = tk.Toplevel()
    popup_window.title("Button Pressed")

    # Label to display the IP address
    ip_label = tk.Label(popup_window, text=f"IP Address: {ip_address}")
    ip_label.pack()

    # Checkbutton to toggle querying for players
    query_var = tk.BooleanVar(value=True)  # Default: Querying enabled
    query_button = tk.Checkbutton(popup_window, text="Enable Quere", variable=query_var)
    query_button.pack()

    # Text box to display the running count of seconds
    time_text = tk.Text(popup_window, height=10, state='disabled')
    time_text.pack()

    # Function to update the time display
    def update_time():
        seconds = 0
        test = ip_address  # Didn't want to update two legacy vars, lol

        def lockUnlockTextBox(message):  # This publishes the text to the location: Allows text box to be edited long enough for pgm to update box - but prevents users from editing text box (they dont need to edite it, if they did it doesnt matter, just looks better this way )
            time_text.config(state='normal')
            time_text.insert(tk.END, f"{message}")  # and replied in {status.latency} ms")
            time_text.config(state='disabled')

        while True:
            time_text.config(state='normal')
            time_text.delete(1.0, tk.END)  # Clears the contents of the text field

            server = JavaServer.lookup(test)
            status = server.status()

            lockUnlockTextBox(f"The server has the following number players online: {status.players.online}")

            if query_var.get():  # Check if querying is enabled
                lockUnlockTextBox(f"\nAttempting to pull active player names...")
                try:
                    query = server.query()
                    lockUnlockTextBox(f"The server has the following players online: {', '.join(query.players.names)}")
                except:
                    lockUnlockTextBox(f"\nERR: Cannot get name of players. please enable 'quere' in server.properties")
                    time.sleep(5)  # let ppl read the msg
            else:
                lockUnlockTextBox(f"\nQuere Skipped!")

            time.sleep(1)  # Time delay for the counter

    # Start a thread to update the time display
    threading.Thread(target=update_time, daemon=True).start()


def close_program():
    root.destroy()

# Read the number of buttons from the "iplist.txt" file
def read_num_buttons():
    try:
        with open("iplist.txt", "r") as file:
            lines = file.readlines()
            output = len(lines)
            return output - 2  # First row is reserved for the "Type '0' to add an IP" message, final row is reserved for fomatting
    except FileNotFoundError:
        messagebox.showerror("File Not Found", "The file 'iplist.txt' was not found.")
        return 0

# Get the IP address corresponding to the button index
def get_ip_address(button_index):
    with open("iplist.txt", "r") as file:
        lines = file.readlines()[1:]  # Skip the first line       
        if button_index < len(lines):
            return lines[button_index].strip()
        else:
            return ""

# Add a new server IP
def add_server_ip():
    new_ip = simpledialog.askstring("Add Server IP", "Enter the new IP address:")
    if new_ip is not None:
        try:
            with open("iplist.txt", "r+") as file:
                lines = file.readlines()
                if lines[-1][-1] != '\n': #Edge case being compendated for when writing to text file 
                    file.write("\n")
                file.write(new_ip + "\n")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add IP: {e}")
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
