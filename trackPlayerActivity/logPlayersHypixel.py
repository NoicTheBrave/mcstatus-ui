from trackPlayerActivity import *

if __name__ == "__main__": #main function
    toggleQuery = False #True
    ip_address = "mc.hypixel.net"
    
    while True:
        data = smartLogPlayerActivity(ip_address,toggleQuery) #logPlayerActivity(ip_address,toggleQuery)
        
        for i in data:
            print(i)
        print("___________")
        
        
        #if(data[2] > 0): #if anyone is online, start logging data every second, otherwise, do so for a longer time interval (server is still pinged every second, just, the only time it will store data from second-to-second is when someone is online, which is the smart thing to do inorder to minimize file size for logging data, since this is all I am logging and care about atm)

        time.sleep(1)
    


