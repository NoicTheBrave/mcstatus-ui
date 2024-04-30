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
#-------------Just make this an independent app maybe? No UI? Just since it's gonna be storing historical data and all that, and if someone ever asks this to be built into the UI, IG I can bite and do that... the core functionality needs to exist first, and if I DID build it into the UI of what I already have, I would need to do several things: 
#   - Discovered that SOMETIMES after running for a long time, or not being the main tab, the pinging the server app just STOPS working 9the thread) and needs to be closed and re-opened via my button UI main menu thingy I made (does NOT require me restarting the app as a whole) -> Need to check or preform a try-catch for that condition (maybe even fix the weird bug when I close a window for a server ping thread, it freaks out about sockets and stuff, idk man... ) 
#   - Need to discriminate between the server NOT having quere on and me CHOSING to have quere on (feel like that might be an important distinction... maybe ping the server for quere automatically every 10-30min or every hour to see if query is enabled...?) <--- Not sure WHY I feel it's important, but it *feels* important to me... idk 

#-----------What to aquire & store----------
# get the number of players online
# if quere is enabled (pass this info into the function), then get the names from the quere list. if its not, I guess I will just log an empty name list :) (I can tell historically if someone was online and quere was off by seing the number of players and NO names vs NO players w/ no names, it makes sence when checking later down the line, unless I just REALLY feel like storying a parameter if quere was on or not as a quick ref. ig?)
# get time since epoch & store it (make another column just for the ACTUAL human-readable time as well for whatever timezone epoch uses or my own ig??? (if personal time zone used, I MUST state this in the log file))
#   Consider pinging the server for quere every hour...? ((Might allow us, the person ))

# ServerIP, Time (Epoch), Time (Human-Readable), Query State (On/Off), Player #, Player Names
