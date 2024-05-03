#https://github.com/Uberi/speech_recognition/blob/master/examples/write_audio.py

#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

from TranscriptV3_1 import *
from pydub import AudioSegment 
import os
#print('Get current working directory : ', os.getcwd())


currentFileDirectory = str(os.getcwd()) 
# Audio File name now comes in 2 parts, cause it was easier to do things this way... (counter is involved to change the # before the file extension... could split the audio file name up, but this works fine as well... ig)
audioname = "microphone-results" # might not like it, if it is NOT mono-channel. if thats the case, an error will occur, and audio will need to be fed thru mono-channel converter pgm used for removing curse words as well.... ug
fileExtension = ".wav"
storeAudio = currentFileDirectory + "\\audioFiles\\"
storeText = currentFileDirectory + "\\textFiles\\"

counter = 0 #again, i am lazy
while True: 

    #--------------RECORDING SECTION--------------
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source) #Might filter out some background noise words??? (not sure, came from "speachToText_LikeGhettoTranscribingWithoutTimeStamps.py" in the /sus/old/ folder - what started most of this process honestly... (Still a useful asset tho, thus why its not tossed yet ))
        audio = r.listen(source)

    # Creates file name based on counter, in an attempt to log and NOT override other audio files... :) 
    audioFileName = storeAudio + audioname + str(counter) + fileExtension


    # write audio to a WAV file
    with open(audioFileName, "wb") as f:
        f.write(audio.get_wav_data())


    #---------TRANSCRIBING SECTION------------

    #NOTE: If this section, the transcribing section, begins to take WAY too long,k or even just a bit effects my voice recording (aka, voice isnt being fully recorded cause it's taking a second or more to process things...)... THEN it's likely that I will have to make a threadded thing for this just to make sure that everything gets taken care of... heck, MAYBE even audio recording needs to be threadded as well, if writing the audio file takes too long that is... just layer one ontop of the other, and IDEALY, have ONE MAIN AUDIO FILE thread just constantly running (start it before the loop) so that we can compare later, or something idk man... (for more accurate audio recording / lining up audios and stuff later? idk man... idk how to line-up audio like that, I am just spit-balling... and if  I can, idk how long that process takes... :/ )

    """ song = AudioSegment.from_file(audioFileName) #SHOULD ALWAYS be one of these 

    # pydub does things in milliseconds 
    time_div = song.duration_seconds*1.0 #does it need to be a float? <--- combine some variables from the "demo" ver. to simplify things



    time_offset = counter * time_div#again, i am lazy  """
    #threads[i] = Thread(target=transcript, args=(audioBuffer[counter], counter, time_offset))
    transcript(audioFileName, counter, 0, storeText)

    counter = counter + 1




