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

    # Text box to display the running count of seconds
    time_text = tk.Text(popup_window, height=1, state='disabled')
    time_text.pack()

    # Function to update the time display
    def update_time():
        #seconds = 0
        test = ip_address #didnt wanna update 2 legacy vars, lol
        
        def lockUnlockTextBox(message): #This publishes the text to the location: Allows text box to be edited long enough for pgm to update box - but prevents users from editing text box (they dont need to edite it, if they did it doesnt matter, just looks better this way )
            time_text.config(state='normal')
            time_text.insert(tk.END, f"{message}") #and replied in {status.latency} ms")
            time_text.config(state='disabled')
        while True:
            #time_text.config(state='normal')
            time_text.config(state='normal')
            time_text.delete(1.0, tk.END)#Clears the contents of the text field
            
            time_text.config(state='disabled')
            server = JavaServer.lookup(test)# "tu-ece.playit.gg"))
            '''
                'status' is supported by all Minecraft servers that are version 1.7 or higher.
                Don't expect the player list to always be complete, because many servers run
                plugins that hide this information or limit the number of players returned or even
                alter this list to contain fake players for purposes of having a custom message here.
            '''
            status = server.status()

            lockUnlockTextBox(f"The server has the following number players online: {status.players.online}")
            
            """
                # 'ping' is supported by all Minecraft servers that are version 1.7 or higher.
                # It is included in a 'status' call, but is also exposed separate if you do not require the additional info.
                #latency = server.ping()
                #print(f"The server replied in {latency} ms")

                # 'query' has to be enabled in a server's server.properties file!
                # It may give more information than a ping, such as a full player list or mod information.
            """
            if (status.players.online != 0):
                lockUnlockTextBox(f"\nAttempting to pull active player names...")
                try:
                    query = server.query()
                    lockedunlockTextBox(f"The server has the following players online: {', '.join(query.players.names)}")
                except:
                    lockUnlockTextBox(f"ERR: Cannot get name of players. please enable 'quere' in server.properties")
            else:
                lockUnlockTextBox(f"No Players Online. Quere Skipped!")
                    
            #time_text.insert(tk.END, f"Seconds passed: {seconds}") #Updates the text field 
            #time_text.config(state='disabled') #Disables user's ability to edit text field (Good)
            time.sleep(1) #Time delay for the counter
            #seconds += 1
    # Start a thread to update the time display
    threading.Thread(target=update_time, daemon=True).start()
            
def getIPInfo(): 
    server = JavaServer.lookup(test)# "tu-ece.playit.gg"))

    '''
        'status' is supported by all Minecraft servers that are version 1.7 or higher.
        Don't expect the player list to always be complete, because many servers run
        plugins that hide this information or limit the number of players returned or even
        alter this list to contain fake players for purposes of having a custom message here.
    '''
    status = server.status()

    print(f"The server has the following number players online: {status.players.online}") #and replied in {status.latency} ms")

    """
        # 'ping' is supported by all Minecraft servers that are version 1.7 or higher.
        # It is included in a 'status' call, but is also exposed separate if you do not require the additional info.
        #latency = server.ping()
        #print(f"The server replied in {latency} ms")

        # 'query' has to be enabled in a server's server.properties file!
        # It may give more information than a ping, such as a full player list or mod information.
    """
    if (status.players.online != 0):
        print("\nAttempting to pull active player names...")
        try:
            query = server.query()
            print(f"The server has the following players online: {', '.join(query.players.names)}")
        except:
            print("ERR: Cannot get name of players. please enable 'quere' in server.properties")
    else:
        print("No Players Online. Quere Skipped!")





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
