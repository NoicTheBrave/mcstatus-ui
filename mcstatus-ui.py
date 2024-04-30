import tkinter as tk
from tkinter import messagebox, simpledialog
import threading
import time

from trackPlayerActivity import * #Custom thing for logging python data :) 

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
    query_var = tk.BooleanVar(value=False)  # Default: Querying Disabled
    query_button = tk.Checkbutton(popup_window, text="Enable Query", variable=query_var)
    query_button.pack()
    
    logData_var = tk.BooleanVar(value=False)  # Default: Logging Disabled
    logData_button = tk.Checkbutton(popup_window, text="Enable Player Data Logging", variable=logData_var)
    logData_button.pack()
    

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

            toggleQuery = query_var.get()
            if toggleQuery:  # Check if querying is enabled
                lockUnlockTextBox(f"\nAttempting to pull active player names...")
                try:
                    query = server.query()
                    lockUnlockTextBox(f"The server has the following players online: {', '.join(query.players.names)}")
                except:
                    lockUnlockTextBox(f"\nERR: Cannot get name of players. please enable 'query' in server.properties")
                    time.sleep(3)  # let ppl read the msg
            else:
                lockUnlockTextBox(f"\nQuery Skipped!")

            
            if logData_var.get():  # Check if querying is enabled
                lockUnlockTextBox("\n-----------------------")
                lockUnlockTextBox(f"\nLogging Player Data...")
                
                # Smart Data Logging
                data = smartLogPlayerActivity(ip_address,toggleQuery)
                
                # (Default) Data Logging - Log everything once per second
                #data = logPlayerActivity(ip_address,toggleQuery)
                
                lockUnlockTextBox("\nIP Address: " + str(data[0]))
                lockUnlockTextBox("\nenableQuere: " + str(data[1]))
                lockUnlockTextBox("\nPlayersOnline: " + str(data[2]))
                lockUnlockTextBox("\nPlayerNames: " + str(data[3]))
                lockUnlockTextBox("\nTime(Epoch): " + str(data[4]))
                lockUnlockTextBox("\nTime(Human Readable): " + str(data[5]))
                #for i in data:
                #    lockUnlockTextBox("\n" + str(i))
            else:
                lockUnlockTextBox(f"\nData is Not being logged.")



            time.sleep(1)  # Time delay for the counter
    # Start a thread to update the time display
    threading.Thread(target=update_time, daemon=True).start()

    

    # Function to set background color based on the number of players online
    def set_background_color(num_players):
        if num_players == 0:
            popup_window.configure(bg="SystemWindow")
        elif num_players <= 8:
            # Define a color palette
            color_palette = ["#FF0000", #RED
                             "#FFA500", #ORANGE
                             "#FFFF00", #YELLOW
                             "#008000", #GREEN
                             "#0000FF", #BLUE
                             "#900C3F", #Purple
                             "#00FFFF", #CYAN
                             "#00FF00"] #Lime Green
                             

            # Set background color based on the number of players
            popup_window.configure(bg=color_palette[num_players - 1])

    # Function to update the background color based on the number of players online
    def update_background_color():
        while True:
            server = JavaServer.lookup(ip_address)
            status = server.status()
            num_players = status.players.online
            set_background_color(num_players)
            time.sleep(1)

    # Start a thread to update the background color
    threading.Thread(target=update_background_color, daemon=True).start()
    

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
