import os

def create_folders_and_files(name, content):
    # Create the main "library" folder if it doesn't exist
    if not os.path.exists("library"):
        os.makedirs("library")
    
    # Convert the name to lowercase
    name = name.lower()
    
    # Get the first character of the name
    first_char = name[0]
    
    # Create the sub-folder if it doesn't exist
    folder_path = os.path.join("library", first_char)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Write the file with the given name and "1" inside it
    file_path = os.path.join(folder_path, name + ".txt")
    with open(file_path, "a") as file:
        file.write("\n" + str(content))

# Example usage
name = "bobby"
content = "bobby Sucks"
create_folders_and_files(name,content)
