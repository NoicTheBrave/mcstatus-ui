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
