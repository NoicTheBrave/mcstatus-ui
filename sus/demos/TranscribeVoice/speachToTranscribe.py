#https://github.com/Uberi/speech_recognition/blob/master/examples/write_audio.py

#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

from TranscriptV3_1 import *
from pydub import AudioSegment 
import os
import threading
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
        try: 
            #audio = r.listen(source,timeout=0.5)
            audio = r.listen(source)        
                    # Creates file name based on counter, in an attempt to log and NOT override other audio files... :) 
            audioFileName = storeAudio + audioname + str(counter) + fileExtension
            
                    # write audio to a WAV file
            with open(audioFileName, "wb") as f:
                f.write(audio.get_wav_data())
        
            #---------TRANSCRIBING SECTION------------

            """  transcript(audioFileName, counter, 0, storeText) """
            
            def transcribe_thread(audio_file, index, offset):
                transcript(audio_file, index, offset, storeText)
            
            # Create a thread for transcription
            try:
                threading.Thread(target=transcribe_thread, args=(audioFileName, counter, 0)).start()
            except:
                print("Threading error occured ")
                
        except sr.WaitTimeoutError:
            print("ERR: No Voice detected - will prompt again ")

    



    counter = counter + 1
    print(counter)

            
        

    



