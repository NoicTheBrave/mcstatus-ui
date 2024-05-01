from mcstatus import JavaServer
import time
import os

# You can pass the same address you'd enter into the address field in minecraft into the 'lookup' function
# If you know the host and port, you may skip this and use JavaServer("example.org", 1234)

startMsg = [
  "Please select an IP from the list below:",
  "Attempting to get information on "
]

print(startMsg[0])
ipList = []
counter = 0
f = open("iplist.txt", "r")
for x in f:
  print(str(counter) + ") " + x)
  ipList.append(x)
  counter += 1
f.close()  #always good 2 do

try:
  temp = int(input("Please Type which Server number you would like to ping: "))
except:
  print("Invalid input, try again. please re-run program,. ")

if (temp == 0):
  temp = str(input("Please Enter the IP you want to Add: "))
  f = open("iplist.txt", "a")
  f.write("\n" + temp)
  #might just be counter, who knows
  ipList.append(temp)
  f.close()  # wanna make sure she saves!
  #assume user selects the final option of ""
  #ipList.append(temp)
  temp = counter

while True:
  print("Starting minecraft server ping...")

  test = str(ipList[temp])
  print(test)
  server = JavaServer.lookup(test)  # "tu-ece.playit.gg"))

  # 'status' is supported by all Minecraft servers that are version 1.7 or higher.
  # Don't expect the player list to always be complete, because many servers run
  # plugins that hide this information or limit the number of players returned or even
  # alter this list to contain fake players for purposes of having a custom message here.
  status = server.status()

  print(
    f"The server has the following number players online: {status.players.online}"
  )  #and replied in {status.latency} ms")

  # 'ping' is supported by all Minecraft servers that are version 1.7 or higher.
  # It is included in a 'status' call, but is also exposed separate if you do not require the additional info.
  #latency = server.ping()
  #print(f"The server replied in {latency} ms")

  # 'query' has to be enabled in a server's server.properties file!
  # It may give more information than a ping, such as a full player list or mod information.

  if (status.players.online != 0):

    print("\nAttempting to pull active player names...")
    try:
      query = server.query()
      print(f"The server has the following players online: {', '.join(query.players.names)}")
    except:
      print("ERR: Cannot get name of players. please enable 'quere' in server.properties")
      time.sleep(1) #it gets another second of delay to allow you to see this error 
  else:
    print("No Players Online. Quere Skipped!")

  time.sleep(1)  #This is the ONLY real difference atm between the other one and this one. Just wanted a slower stream of messages coming in, since I do NOT have a UI for this or anything. :/
  os.system('clear')  #By adding this, it makes the consol look cleaner.
