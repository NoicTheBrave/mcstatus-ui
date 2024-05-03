#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
from TranscriptV3_1 import *
from pydub import AudioSegment 
import os
import threading

currentFileDirectory = str(os.getcwd()) 
audioname = "microphone-results" 
fileExtension = ".wav"
storeAudio = currentFileDirectory + "\\audioFiles\\"
storeText = currentFileDirectory + "\\textFiles\\"

counter = 0
while True: 
    
    #--------------RECORDING SECTION--------------
    r = sr.Recognizer()
    def startListeningAndSave():
        with sr.Microphone() as source:
            print("Say something!")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        audioFileName = audioname + str(counter) + fileExtension
        tst = storeAudio + audioFileName
        print(tst)
        with open(tst, "wb") as f:
            f.write(audio.get_wav_data())
    
    threading.Thread(target=startListeningAndSave).start()
    
    
    #---------TRANSCRIBING SECTION------------
    
    song = AudioSegment.from_file(tst)
    time_div = song.duration_seconds * 1.0
    time_offset = counter * time_div
    
    # Define a function for threading
    def transcribe_thread(audio_file, index, offset):
        transcript(audio_file, index, offset, storeText)
    
    # Create a thread for transcription
    """     transcribe_thread = threading.Thread(target=transcribe_thread, args=(tst, counter, time_offset))
    transcribe_thread.start() """
    threading.Thread(target=transcribe_thread, args=(tst, counter, time_offset)).start()
    
    counter += 1

        
        
        
        
        
