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
name = "bobby" #This would be the name of the player I can get from querying the server, IF they were online, I suppose (probably just run a FOR loop for those online for querying, and just update their status' accordingly)
content = "bobby Sucks" #this would be any additional data I would wanna include about the player - such as their ONLINE status - we can imply they are OFFLINE if there is nothing written about them in the text file (no need to increase system storage to tell me someone is offline, I only really care whey they are ONLINE, UNLESS! I just REALLY wanna know for sure if they were offline... and I WAS infact pinging the server... then IG i would wanna know.... (frick) - maybe make that ASWELL a togglable option...?)
create_folders_and_files(name,content)

#NOTE: 
# If I DO plan to toggle on/off storing if a player is OFFLINE, then I will need to PROBABLY make that it's own thread dedicated to that... and MAYBE even have it select players to record offliner status for - for example, i might only wanna know when Z is on hypixel, and NOT ALL 40k players, so I could just pick him... alternatively, if I DID, I need a select ALL button as well (I am not about to click 40k buttons just for that data...)
# More importantly, MAYBE I can make it so it closes and re-opens a new window when querying is enabled, and then generates these new options for us... aka, "log individual player activity" & "Log Player Offline Status" (offline player status MIGHT be a sub-sub "menu" button, aka, both querying AND )"log individual player activity" must be enabled, since that would be the ONLY time I would need to do it - cause sometimes ppl just wanna know when someone is online, and can just ASSUME someone is offline ... but in reality they would be either OFFLINE or I was not logging data @ that time... *tee hee hee* (aka, do u want the MOST accurate data as possible, or NAWWWWWWWWWW -> They COULD refer back to the main data logging file - but then they would have to see if the server pinging was running or not during their friend was offline OR, hear me out.... they could just ENABLE THIS SETTING 0_0)
# 