import csv
import time

def write_to_csv(filename, data):
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

def main():
    filename = 'data.csv'
    headers = ['Variable1', 'Variable2', 'Variable3', 'Variable4', 'Variable5', 'Variable6']

    # Write headers to CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)

    while True:
        # Replace these with your actual data sources or calculations
        variable1 = 1
        variable2 = 2
        variable3 = 3
        variable4 = 4
        variable5 = 5
        variable6 = 6

        data = [variable1, variable2, variable3, variable4, variable5, variable6]

        # Write data to CSV file
        write_to_csv(filename, data)

        # Wait for 5 seconds before writing the next line
        time.sleep(5)

if __name__ == "__main__":
    main()
