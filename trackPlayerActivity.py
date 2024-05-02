'''
    Author: Nicholas Chorette
    Date: 4/30/2024
    Purpose: Based on, @ minimum, # of players online per timepstamp (based on epoch time... I suppose), this application is ment to be able to track number of players, and even names of players online for a server while this application is ran. 
            @ present, this app is ment to be an add-on to the currently existing server pinging application (idealy, something that can be toggled via a check mark like querying is atm), or perhaps later down the line, its own thing, independent of the app. 
            The idea is to get an idea of, over time, what are the most ideal and/or peak hours of a server's activity based on the # of players online, when these players are online, and if querying is on for the server and/or enabled (assuming this is running under the add-on model stated above) enabled by us, the user of this app, then the app should store data as the server is pinged. 
            The goal is to use this historical data as deamed nessisary by the user. Realistically, there are more than likely tools and apps out there already like this, but I really wanna make this and not work on something atm, and this is a great distraction... I hate to say that, but it is honestly. 
            
            In the end, I would like this just to see when my own friends are online on a server they play on alot to get a general idea of when they are on to better understand their play times and avaliability, etc etc. 
            Not to mention, this would be a helpful tool as a moderator, being able to see when players are online, peak operating times, and if we want to take it another step further, maybe one day log the CPU, GPU, RAM, etc usage of a server so long as this application is running on the host machine. (That would acutally be pretty cool, even temps, so we can get an idea of how much something is pushing the limits of a system, in addition to meshing this phenomena with a server log, that would be insaaaaaaaane. idk man)
'''
    # -------------Just make this an independent app maybe? No UI? Just since it's gonna be storing historical data and all that, and if someone ever asks this to be built into the UI, IG I can bite and do that... the core functionality needs to exist first, and if I DID build it into the UI of what I already have, I would need to do several things: 
    #   - Discovered that SOMETIMES after running for a long time, or not being the main tab, the pinging the server app just STOPS working 9the thread) and needs to be closed and re-opened via my button UI main menu thingy I made (does NOT require me restarting the app as a whole) -> Need to check or preform a try-catch for that condition (maybe even fix the weird bug when I close a window for a server ping thread, it freaks out about sockets and stuff, idk man... ) 
    #   - Need to discriminate between the server NOT having quere on and me CHOSING to have quere on (feel like that might be an important distinction... maybe ping the server for quere automatically every 10-30min or every hour to see if query is enabled...?) <--- Not sure WHY I feel it's important, but it *feels* important to me... idk 

    #-----------What to aquire & store----------
    # get the number of players online
    # if quere is enabled (pass this info into the function), then get the names from the quere list. if its not, I guess I will just log an empty name list :) (I can tell historically if someone was online and quere was off by seing the number of players and NO names vs NO players w/ no names, it makes sence when checking later down the line, unless I just REALLY feel like storying a parameter if quere was on or not as a quick ref. ig?)
    # get time since epoch & store it (make another column just for the ACTUAL human-readable time as well for whatever timezone epoch uses or my own ig??? (if personal time zone used, I MUST state this in the log file))
    #   Consider pinging the server for quere every hour...? ((Might allow us, the person ))

    # ServerIP, Time (Epoch), Time (Human-Readable), Query State (On/Off), Player #, Player Names

import time #for naming and logging time data is collected 
import csv #for storing data
import os #for checking to see if file Exists for headder
from mcstatus import JavaServer #for getting server information

def get_epoch_time():
    epoch_time = int(time.time())
    return epoch_time

def epoch_to_human_readable(epoch_time):
    #human_readable_time = time.ctime(epoch_time)
    
    human_readable_time = time.strftime("%m-%d-%Y_%H-%M-%S", time.localtime(epoch_time))
    
    return human_readable_time 


""" def create_csv(server_ip): # Works for servers if a port specification is needed (such as NGROK IP addresses as well :) 
    # Replace '.' with '_' and ':' with '__'
    file_name = server_ip.replace('.', '_').replace(':', '__') + '.csv'

    # Create CSV file
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)

    print(f"CSV file '{file_name}' has been created.")
 """
def formatFileName(ip_address, currentEpochTime): 
    #epoch_time = get_epoch_time()
    formattedTime = epoch_to_human_readable(currentEpochTime)
    formattedTime = formattedTime[:len(formattedTime)-6] #Trim the seconds and minutes
    
    file_name = ip_address.replace('.', '_').replace(':', '__') +"_" + formattedTime + '.csv'
    #print("Place holder so my code works")
    
    temp = getFileDirectory()
    file_name = temp + "\\logData\\" + file_name
    
    #print("FileName: " + file_name)
    
    return file_name

def write_to_csv(filename, data):
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

def makeCSVHeadder(fileName): 
    #filename = 'data.csv'

    
    doesFileExist = check_file_exists(fileName)
    #if(doesFileExist): 
    #    print("File Exists - No Headder Required") #stop doing its task, skip function. Otherwise, proceed with the next steps
    #else:
    if(doesFileExist != True):    
        headers = ['Server IP', 'QueryState', 'PlayersOnline', 'PlayerNames', 'Time (Epoch)', 'Time (Human-Readable) [EST]'] #EST -> Only for my regeion that I am developing this code in, idk about others who use this :) 

        # Write headers to CSV file
        with open(fileName, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)

def check_file_exists(file_path):
    if os.path.exists(file_path):
        return True #print("FILE EXISTS")
    else:
        return False #print("File does NOT exist")

def getFileDirectory(): #----------------NEED TO ADD: IF I WANT TO SEPORATE THE MAIN PYTHON FILES FROM THE LOG FILES, i NEED TO USE THIS WHEN WRITING TO FILES, AND MAKE IT WRITE TO THE "logData" folder... FUG
    current_directory = os.path.dirname(os.path.abspath(__file__))
    return current_directory

def pingServer(ip_address,queryEnable): #String, Bool
    
    returnArray = ["*"]*4
    '''
        -----Information about the returnArray[]-----
        returnArray[0] = ServerIP
        returnArray[1] = QueryState (as fed to function, NOT what the state of the server's quere config is...)
        returnArray[2] = # of players
        returnArray[3] = Player Names (ONLY a important value if query, aka, returnArray[1] == True)
    '''
    
    returnArray[0] = ip_address; 
    returnArray[1] = queryEnable; 
    
    toggleQuery = queryEnable
    server = JavaServer.lookup(ip_address)
    status = server.status()
    
    returnArray[2] = status.players.online; 
    #print(f"The server has the following number players online: {status.players.online}")
    
    if(toggleQuery): 
        try:
            query = server.query()
            
            returnArray[3] = query.players.names
            #print(f"The server has the following players online: {', '.join(query.players.names)}")
            
        except:
            print(f"\nERR: Cannot get name of players. please enable 'query' in server.properties")
            #time.sleep(5)  # let ppl read the msg
    return returnArray



#serverIP - Remove "." and ":" characters from the IP, followed by "_", then the date
    
def formatPlayerLogData(ip_address,toggleQuery): 
    serverInfo = pingServer(ip_address, toggleQuery)
    
    # Getting time comes 2nd, cause I wanna know this info after I got the info, not before... 
    epoch_time = get_epoch_time()
    human_readable_time = epoch_to_human_readable(epoch_time)
    fileName = formatFileName(ip_address,epoch_time)
    
    
    csvData = []
    for i in serverInfo:
        csvData.append(i)
    csvData.append(epoch_time)
    csvData.append(human_readable_time)
    
    return [csvData, fileName]


def logPlayerActivity(ip_address,toggleQuery):

    csvDataLoggedFormat,fileName = formatPlayerLogData(ip_address,toggleQuery)
    
    
    makeCSVHeadder(fileName)
    write_to_csv(fileName, csvDataLoggedFormat)
    
    return csvDataLoggedFormat


#Value is (-1) so that if time is ever "0", it will not mess up (not sure if it would simply state "00", but just to be on the safe side)
previousMinute = -1 #this is used to keep track when the previous time was logged, assuming that nobody is online (Critical part that makes the following function "smart")
def smartLogPlayerActivity(ip_address,toggleQuery): #logs more frequently when ppl are online, and logs less when ppl are offline - constantly pings server every 1 second reguardless

    csvDataLoggedFormat,fileName = formatPlayerLogData(ip_address,toggleQuery)
    
    #print(csvDataLoggedFormat[2])
    currentMinute = csvDataLoggedFormat[5][14:16]
    #print(currentMinute)
    if(csvDataLoggedFormat[2] == 0): #if nobody is online
        print("Nobody is online... Checking time... ")
        global previousMinute
        if(csvDataLoggedFormat[5][14:16] != str(previousMinute)): #if a minute has passed since data was last logged w/ no players online
            print("Time Changed! Time was logged ")
            makeCSVHeadder(fileName)
            write_to_csv(fileName, csvDataLoggedFormat)
            previousMinute = csvDataLoggedFormat[5][14:16] #must update previous minute to current minute on the hour for this to work properly
    else: #someone IS online    
        makeCSVHeadder(fileName)
        write_to_csv(fileName, csvDataLoggedFormat)
    
    return csvDataLoggedFormat 
    
    