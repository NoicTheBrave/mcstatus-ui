import tkinter as tk
from tkinter import messagebox, simpledialog
import threading
import time
import math

from trackPlayerActivity import * #Custom thing for logging python data :) 

from mcstatus import JavaServer
from ttsLib import *
def create_buttons(num_buttons):
    global button_window
    button_window = tk.Toplevel(root)
    button_window.title("Button Selector")
    button_window.protocol("WM_DELETE_WINDOW", close_program)
    
    
    menu_frame = tk.Frame(button_window)
    menu_frame.pack()
    #Top Lable added - Exsessive spaces are there to help expand the window out more artificially VS setting an acutal window size :P 
    label = tk.Label(menu_frame, text="                     Press a Button to get started:                     ")
    label.pack()
    

    with open("iplist.txt", "r") as file:
        lines = file.readlines()[1:]  # Skip the first line
        #test = [tk.Frame(button_window)]*3 #theoredically, this now represents 3 different frames... depending on which order i PACK, will determine which set of assets will be on top, middle, and bottom, I think... 
        temp = [] #*(range(num_buttons)%3)# should help me make the length of button part only 3 before rolling over to next row
        rowShifter = 0 
        counter = 0
        
        #for i in range(num_buttons):
        for i in range(math.floor(len(lines)/3) + 1): #button making loop
            if i < len(lines):
                ip_address = lines[i].strip()
            else:
                ip_address = ""
            #print(math.floor(i/3))
            
            button_frame = tk.Frame(button_window)
            button_frame.pack()
            
            
            for j in range(3):#horixontal control? Or Vert? (we're gonna find out)
                #button = tk.Button(button_frame, text=f"Button {i*3 + j + 1}", command=button_click, width=10, height=2)
                print(((len(lines)) % 3 == 0))
                print(len(lines))
                
                if(counter != 0 and (len(lines)) % 3 == 0 and counter == len(lines)): 
                    print("IPs are less than 4")
                    break
                button = tk.Button(button_frame, text=lines[counter], command=lambda idx=counter: on_button_press(idx), width=10, height=2)
                button.pack(side=tk.LEFT, padx=5, pady=5)
                counter += 1 
                print(counter)
                if(counter == len(lines)): #prevents from going past +1 buttons (due to the note I put in the iplist.txt)
                    print("End of buttons")
                    break
                 
                #button = tk.Button(menu_frame, text=ip_address, command=lambda idx=i: on_button_press(idx))
            
            
            """ button = tk.Button(test[math.floor(i/3)], text=ip_address, command=lambda idx=i: on_button_press(idx))
            
            if((i % 3 == 0) and (i != 0)):
                test[math.floor(i/3)].pack() """
            """ if((i % 3 == 0) and (i != 0)): 
                for j in range(3): #Packing loop
                    temp[j].pack(side=tk.LEFT) 
                temp = [] #clear array before using it again 
                rowShifter += 1
            button = tk.Button(menu_frame, text=ip_address, command=lambda idx=i: on_button_press(idx))
            print(i - rowShifter*3) """
            #temp.append(button)
            #temp += 1 
        print("end of setup")
        """ for i in range(3): 
            test[i].pack() """
        #rowShifter = 0 #reset the shifter 
        

    # Add "Add Server IP" button
    add_button = tk.Button(button_window, text="Add Server IP", command=add_server_ip)
    add_button.pack()

def on_button_press(button_index):
    threading.Thread(target=show_popup, args=(button_index,)).start()

prevPlayerCnt = -1 #place holder for function below 
def show_popup(button_index):
    ip_address = get_ip_address(button_index)
    popup_window = tk.Toplevel() #tk.Toplevel()
    popup_window.title("Button Pressed")
    
    menu_frame = tk.Frame(popup_window)
    menu_frame.pack()
    # Label to display the IP address
    ip_label = tk.Label(menu_frame, text=f"IP Address: {ip_address}")
    ip_label.pack()


    #checkBoxFrame = tk.Frame(root) #----We gonna see how this works and hope for the best 
    # Checkbutton to toggle querying for players
    query_var = tk.BooleanVar(value=False)  # Default: Querying Disabled
    query_button = tk.Checkbutton(menu_frame, text="Enable Query", variable=query_var)
    query_button.pack(side=tk.LEFT)

    
    
    logData_var = tk.BooleanVar(value=False)  # Default: Logging Disabled
    logData_button = tk.Checkbutton(menu_frame, text="Enable Player Data Logging", variable=logData_var)
    logData_button.pack(side=tk.LEFT)

    ttsPlayerStatus_var = tk.BooleanVar(value=False)  # Default: Logging Disabled
    ttsPlayerStatus_button = tk.Checkbutton(menu_frame, text="Enable TTS Player Status", variable=ttsPlayerStatus_var)
    ttsPlayerStatus_button.pack(side=tk.LEFT)


    text_frame = tk.Frame(popup_window)
    text_frame.pack()
    # Text box to display the running count of seconds
    time_text = tk.Text(text_frame, height=10, state='disabled')
    time_text.pack()


    def lockUnlockTextBox(message):  # This publishes the text to the location: Allows text box to be edited long enough for pgm to update box - but prevents users from editing text box (they dont need to edite it, if they did it doesnt matter, just looks better this way )
        time_text.config(state='normal')
        time_text.insert(tk.END, f"{message}")  # and replied in {status.latency} ms")
        time_text.config(state='disabled')
    
    
    def tts_playerOnline(ip): #3rd part of the pgm to ping the servrt -_-
        tts_file_name = "ttsAudio.mp3"
        
        serverData = pingServer(ip_address, False)
        #print("ServerData: " + str(serverData))
        
        """ server = JavaServer.lookup(ip_address)
        status = server.status()
        num_players = status.players.online """
        num_players = serverData[2]
        # ---------TTS-------------- TTS to tell me if someone joined a server or left (this needs to be a togglable setting... cause otherwise this might get outta hand on larger always fluxuating servers... BUT FOR NOW, ITS FINE )
        global prevPlayerCnt
        if(prevPlayerCnt > num_players): #Player Logged OFF 
            msg = "Goodbye - Player Logged off " + str(ip)
            try:
                tts_textToMP3(msg, tts_file_name)
                #print(tts_file_name)
                play_music(tts_file_name)
            except:
                print("TTS made an oopsie! ")
        
        if(prevPlayerCnt < num_players): #Player Logged ON
            msg = "Hello! - Player Logged ON " + str(ip)
            try:
                tts_textToMP3(msg, tts_file_name)

                play_music(tts_file_name)
            except:
                print("TTS made an oopsie! ")
        prevPlayerCnt = num_players
        #print("prevPlayerCnt: " + str(prevPlayerCnt))
    # Function to update the time display
    def update_time(): 
        seconds = 0
        test = ip_address  # Didn't want to update two legacy vars, lol
        

        while True:
            try: #Hopefully when a server goes down now, or, at the very least, when the pgm fails, it will attempt to ping the server again
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


                #tts_playerOnline(ip_address)#--------TTS Experiment
                
                if ttsPlayerStatus_var.get(): #if tts has been enabled 
                    threading.Thread(target=tts_playerOnline, daemon=True,args = (ip_address,)).start()
                
                time.sleep(1)  # Time delay for the counter
            except Exception as e:
                print("ERR: Failed to Ping Minecraft server - Attempting to ping...")
                
                if("invalid command name" in str(e)): 
                    print("Attempting to close thread...")
                    break #might work 
                
                #print(e)
                time.sleep(0.5) # dont need this thing going too crazy trying to reconnect to the server now...
    # Start a thread to update the time display
    threading.Thread(target=update_time, daemon=True).start()

    

    
    # Function to set background color based on the number of players online
    def set_background_color(num_players, prevPlayerCnt, ip):
        
        color_palette = ["#FF0000", #RED
                             "#FFA500", #ORANGE
                             "#FFFF00", #YELLOW
                             "#008000", #GREEN
                             "#0000FF", #BLUE
                             "#900C3F", #Purple
                             "#00FFFF", #CYAN
                             "#00FF00",#Lime Green
                             "#FFFFFF"] #White
        
        if num_players == 0:
            popup_window.configure(bg="SystemWindow")
            popup_window.configure(bg=color_palette[8])
        elif num_players <= 8:
            
            # Set background color based on the number of players
            popup_window.configure(bg=color_palette[num_players - 1])
        

    # Function to update the background color based on the number of players online
    def update_background_color():
        preciousPlayerCount = -1 #naturally, it would NEVER be this, aka this is a place holder 
                
        while True:
            try: #An attempt to make it so that when server members drops to 0, &/or an error occues before the server drops to 0 ppl online, that the color will still update, reguardless of if the server fails to ping (I believe this is where ONE of the issues of not updating the color of the background of the app comes from, after it fails to ping the server, the thread responcible for color changing dies, thus color is no longer changing anymore. This try-catch should help prevent that from happening again...)
                server = JavaServer.lookup(ip_address)
                status = server.status()
                num_players = status.players.online
                set_background_color(num_players, preciousPlayerCount, ip_address)
                
                preciousPlayerCount = num_players
            except Exception as e:
                errMsg =  str(e)
                if "invalid command name" in errMsg: #aka, window was closed
                    break #should end this thread - should beak out of the while loop
                else: # the error was NOT generated from closing the window...  (Legit problem)
                    #messagebox.showerror("Error", f"Failed to add IP: {e}")
                    print("Color Background has thrown an error:" + errMsg) 
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
