'''
Author: Nicholas Chorette
Date: 5/2/2024 (@ 2:16am - ECT)
Purpose: To test and see if this program will effect the lag on a minecraft server if it pings it fast enough, or, alternatively, multiple computers. HOWEVER, due to the nature of the internet I  have sat up at my appt, there is likely a change IT has software in place that if I send or recieve too many packets, they will just cut my computer off compleatly, and NOT fix the issue  (problem has happened to other residence in the past, and I am not about to become a statistic) :) 

'''

import threading
import time
from mcstatus import JavaServer

# Function to ping the Minecraft server
def ping_server():
    server_address = "festivianservers.net"  # Replace with your Minecraft server address
    server = JavaServer.lookup(server_address)

    while not stop_event.is_set():
        try:
            status = server.status()
            print(f"Server is online! Players: {status.players.online}")
        except Exception as e:
            print(f"Server is offline or unreachable: {e}")

        time.sleep(0.1)  # Ping interval (in seconds)

# Function to handle thread creation
def start_threads():
    global threads
    threads = []

    for _ in range(20):  # Create 20 threads
        thread = threading.Thread(target=ping_server)
        thread.start()
        threads.append(thread)

# Function to stop all threads
def stop_threads():
    stop_event.set()
    for thread in threads:
        thread.join()

# Main function
if __name__ == "__main__":
    stop_event = threading.Event()

    try:
        start_threads()
        input("Press Enter to stop the application...")
    except KeyboardInterrupt:
        pass
    finally:
        stop_threads()
