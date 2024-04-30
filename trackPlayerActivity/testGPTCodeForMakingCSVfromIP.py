import csv

def create_csv(server_ip):
    # Replace '.' with '_' and ':' with '__'
    file_name = server_ip.replace('.', '_').replace(':', '__') + '.csv'

    # Example data for the CSV
    data = [
        ['Server', 'IP', 'Port'],
        ['Minecraft', server_ip.split(':')[0], server_ip.split(':')[1]]
    ]

    # Write data to CSV file
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f"CSV file '{file_name}' has been created.")

# Example usage
server_ip = "192.168.44.88:25565"
create_csv(server_ip)
