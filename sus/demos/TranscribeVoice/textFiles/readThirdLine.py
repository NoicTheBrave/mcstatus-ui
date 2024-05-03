filename = "output4.txt"

# Open the file for reading
with open(filename, "r") as file:
    # Read all lines
    lines = file.readlines()

# Find the index of the third row
third_row_index = 2  # Python is zero-indexed, so the third row has index 2

# Iterate from the third row index until the start of the file with a step of -3
""" for i in range(third_row_index, -1, -3):
    print(lines[i].strip())  # Print the line (strip() removes trailing newline characters) """

for i in range(len(lines)): #make it go exactly as far as it needs to 
    if( (i%3 == 0) and (i != 0)): #would be every 
    

# Close the file
file.close()
