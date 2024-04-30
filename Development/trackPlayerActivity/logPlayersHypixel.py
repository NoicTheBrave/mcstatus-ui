from trackPlayerActivity import *

if __name__ == "__main__": #main function
    toggleQuery = False #True
    ip_address = "mc.hypixel.net"
    
    while True:
        #data = logPlayerActivity(ip_address,toggleQuery) #Log data, reguardless of player count, once per second (or the time delay indicated below)
        data = smartLogPlayerActivity(ip_address,toggleQuery) #Log data - If one or more player is online, log data once per second (or whatever the time delay states below), if NOBODY is online, then ONLY log data once per minute, but keep checking to see if anyone is online (how frequently this checks id dependent on the timeDelay sat below - currently, its once / second)
        
        for i in data:
            print(i)
        print("___________")
        
        
        #if(data[2] > 0): #if anyone is online, start logging data every second, otherwise, do so for a longer time interval (server is still pinged every second, just, the only time it will store data from second-to-second is when someone is online, which is the smart thing to do inorder to minimize file size for logging data, since this is all I am logging and care about atm)

        time.sleep(1)
    


