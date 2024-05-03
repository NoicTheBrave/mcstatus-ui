import tkinter as tk
from tkinter import messagebox, simpledialog
import threading
import time
from mcstatus import JavaServer
from ttsLib import *

def create_buttons(num_buttons):
    global button_window
    button_window = tk.Toplevel()
    button_window.title("Button Selector")
    button_window.protocol("WM_DELETE_WINDOW", close_program)
    
    label = tk.Label(button_window, text="Press a Button to get started:")
    label.grid(row=0, column=0, columnspan=2)

    with open("iplist.txt", "r") as file:
        lines = file.readlines()[1:]  # Skip the first line
        for i in range(num_buttons):
            if i < len(lines):
                ip_address = lines[i].strip()
            else:
                ip_address = ""
            button = tk.Button(button_window, text=ip_address, command=lambda idx=i: on_button_press(idx))
            button.grid(row=i+1, column=0)

    add_button = tk.Button(button_window, text="Add Server IP", command=add_server_ip)
    add_button.grid(row=num_buttons+1, column=0)

def on_button_press(button_index):
    threading.Thread(target=show_popup, args=(button_index,)).start()

prevPlayerCnt = -1

def show_popup(button_index):
    ip_address = get_ip_address(button_index)
    popup_window = tk.Toplevel()
    popup_window.title("Button Pressed")
    
    ip_label = tk.Label(popup_window, text=f"IP Address: {ip_address}")
    ip_label.grid(row=0, column=1)

    query_var = tk.BooleanVar(value=False)  # Default: Querying Disabled
    query_button = tk.Checkbutton(popup_window, text="Enable Query", variable=query_var)
    query_button.grid(row=1, column=0, columnspan=1)

    logData_var = tk.BooleanVar(value=False)  # Default: Logging Disabled
    logData_button = tk.Checkbutton(popup_window, text="Enable Player Data Logging", variable=logData_var)
    logData_button.grid(row=1, column=1, columnspan=1)

    ttsPlayerStatus_var = tk.BooleanVar(value=False)  # Default: Logging Disabled
    ttsPlayerStatus_button = tk.Checkbutton(popup_window, text="Enable TTS Player Status", variable=ttsPlayerStatus_var)
    ttsPlayerStatus_button.grid(row=1, column=2, columnspan=2)

    time_text = tk.Text(popup_window, height=10, state='disabled')
    time_text.grid(row=4, column=0, columnspan=4)

    def lockUnlockTextBox(message):
        time_text.config(state='normal')
        time_text.insert(tk.END, f"{message}")
        time_text.config(state='disabled')
    
    def tts_playerOnline(ip):
        tts_file_name = "ttsAudio.mp3"
        serverData = pingServer(ip_address, False)
        num_players = serverData[2]
        global prevPlayerCnt
        if(prevPlayerCnt > num_players):
            msg = "Goodbye - Player Logged off " + str(ip)
            try:
                tts_textToMP3(msg, tts_file_name)
                play_music(tts_file_name)
            except:
                print("TTS made an oopsie! ")
        
        if(prevPlayerCnt < num_players):
            msg = "Hello! - Player Logged ON " + str(ip)
            try:
                tts_textToMP3(msg, tts_file_name)
                play_music(tts_file_name)
            except:
                print("TTS made an oopsie! ")
        prevPlayerCnt = num_players
    
    def update_time(): 
        seconds = 0
        test = ip_address
        
        while True:
            try:
                time_text.config(state='normal')
                time_text.delete(1.0, tk.END)

                server = JavaServer.lookup(test)
                status = server.status()

                lockUnlockTextBox(f"The server has the following number players online: {status.players.online}")
                
                toggleQuery = query_var.get()
                if toggleQuery:
                    lockUnlockTextBox(f"\nAttempting to pull active player names...")
                    try:
                        query = server.query()
                        lockUnlockTextBox(f"The server has the following players online: {', '.join(query.players.names)}")
                    except:
                        lockUnlockTextBox(f"\nERR: Cannot get name of players. please enable 'query' in server.properties")
                        time.sleep(3)
                else:
                    lockUnlockTextBox(f"\nQuery Skipped!")

                if logData_var.get():
                    lockUnlockTextBox("\n-----------------------")
                    lockUnlockTextBox(f"\nLogging Player Data...")
                    data = smartLogPlayerActivity(ip_address,toggleQuery)
                    lockUnlockTextBox("\nIP Address: " + str(data[0]))
                    lockUnlockTextBox("\nenableQuere: " + str(data[1]))
                    lockUnlockTextBox("\nPlayersOnline: " + str(data[2]))
                    lockUnlockTextBox("\nPlayerNames: " + str(data[3]))
                    lockUnlockTextBox("\nTime(Epoch): " + str(data[4]))
                    lockUnlockTextBox("\nTime(Human Readable): " + str(data[5]))
                else:
                    lockUnlockTextBox(f"\nData is Not being logged.")

                if ttsPlayerStatus_var.get():
                    threading.Thread(target=tts_playerOnline, daemon=True,args = (ip_address,)).start()
                
                time.sleep(1)
            except Exception as e:
                print("ERR: Failed to Ping Minecraft server - Attempting to ping...")
                
                if("invalid command name" in str(e)): 
                    print("Attempting to close thread...")
                    break
                time.sleep(0.5)
    
    threading.Thread(target=update_time, daemon=True).start()

    def set_background_color(num_players, prevPlayerCnt, ip):
        color_palette = ["#FF0000", "#FFA500", "#FFFF00", "#008000", "#0000FF", "#900C3F", "#00FFFF", "#00FF00", "#FFFFFF"]
        
        if num_players == 0:
            popup_window.configure(bg=color_palette[8])
        elif num_players <= 8:
            popup_window.configure(bg=color_palette[num_players - 1])
        
    def update_background_color():
        preciousPlayerCount = -1
                
        while True:
            try:
                server = JavaServer.lookup(ip_address)
                status = server.status()
                num_players = status.players.online
                set_background_color(num_players, preciousPlayerCount, ip_address)
                preciousPlayerCount = num_players
            except Exception as e:
                errMsg =  str(e)
                if "invalid command name" in errMsg:
                    break
                else:
                    print("Color Background has thrown an error:" + errMsg) 
            time.sleep(1)

    threading.Thread(target=update_background_color, daemon=True).start()
    
def close_program():
    root.destroy()

def read_num_buttons():
    try:
        with open("iplist.txt", "r") as file:
            lines = file.readlines()
            output = len(lines)
            return output - 2
    except FileNotFoundError:
        messagebox.showerror("File Not Found", "The file 'iplist.txt' was not found.")
        return 0

def get_ip_address(button_index):
    with open("iplist.txt", "r") as file:
        lines = file.readlines()[1:]        
        if button_index < len(lines):
            return lines[button_index].strip()
        else:
            return ""

def add_server_ip():
    new_ip = simpledialog.askstring("Add Server IP", "Enter the new IP address:")
    if new_ip is not None:
        try:
            with open("iplist.txt", "r+") as file:
                lines = file.readlines()
                if lines[-1][-1] != '\n':
                    file.write("\n")
                file.write(new_ip + "\n")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add IP: {e}")
    button_window.destroy()
    main()

def main():
    num_buttons = read_num_buttons() + 1
    if num_buttons > 0:
        create_buttons(num_buttons)
    else:
        close_program()

root = tk.Tk()
root.withdraw()  

main()

root.mainloop()
