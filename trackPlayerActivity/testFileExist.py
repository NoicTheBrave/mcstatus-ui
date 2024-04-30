import os

def check_file_exists(file_path):
    if os.path.exists(file_path):
        print("FILE EXISTS")
    else:
        print("File does NOT exist")

# Provide the path to the file you want to check
file_path = "festivianservers_net_04-30-2024_13.csv"

check_file_exists(file_path)
