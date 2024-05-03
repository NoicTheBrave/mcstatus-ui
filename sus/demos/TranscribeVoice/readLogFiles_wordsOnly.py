def read_verbal_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if len(lines) >= 3:
                # Start from the third line
                current_line = 2
                returnString = ""
                while current_line < len(lines):
                    #print(lines[current_line].strip())
                    returnString = returnString +  " " + lines[current_line].strip()
                    current_line += 4
                return returnString
            else:
                print("File doesn't have enough lines.")
    except FileNotFoundError:
        print("File not found.")

""" # Replace 'filename.txt' with the path to your text file
filename = 'filename.txt'
read_verbal_lines(filename) """
