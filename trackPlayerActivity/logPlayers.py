from trackPlayerActivity import *

if __name__ == "__main__": #main function
    toggleQuery = False #True
    ip_address = "festivianservers.net"
    
    while True:
        data = logPlayerActivity(ip_address,toggleQuery)
        
        #if
        
        time.sleep(1)
    


