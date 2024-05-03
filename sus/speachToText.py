'''
Author: Nicholas Chorette
Date: 5/2/2024
Purpose: To record audio input from the user, and to convert it into text. Not sure how well this will actually translate into transcribing, if I saw it fitting to do so... or if it even can... but regaurdless of what I think it should be able to CAN and cannot do isn't my main priority atm... Just wanted to see if it even worked hoenstly :) 
- Want to be able to save the audio file, if possible, and the text, and if text is saved, just make it a transcribed file w/ timestamps and all that per word said... That would be awesome honestly... 
- if Possible, then one could upgrade ANOTHER project of mine... and make it "real-time" enough, that it might be massively benoficial to myself for streaming... B)


Notes: 
* If this is NOT working, for windows users, go to Settings -> System -> Sound, the scroll to "Input"
    From there, you can select the mic the system SHOULD recognize as the primary mic it will try to use for ANY application you open going forwards so long as the mic is connected to the PC (to my understanding)
    You can ALSO increase and decrease mic audio output as well from here, apparently...? (it is NOT system volume - I checked via turning up system volume via wireless headset, the presumed mic volume slider DIDNT move when I increased system output audio sooooo YIPPIE! (helps w/ YT vids) - idk why @ present it was/IS @ 76%, weird #) 
* https://pypi.org/project/SpeechRecognition/ 
    * Mentions "Transcribe an audio file" & "save audio data to an audio file". 
        * Implies to me that I can do both, maybe, hopefully, at the same time (might have to be 2 seporate processes... but ya know!)
            * Would REALLY help the auto-bleeper pgm I made along, and maybe be able to bring to life the "live bleeper" via simply delaying everything a bit to bleep myself out! (would be nice) 

'''
'''
Libraries used: 
    pip install SpeechRecognition
    
    An error was generated... try also: 
    pip install pipwin
    pipwin install pyaudio <---- didnt work, so i just did... 
    pip install pyaudio
    
    still an error... 
    directly doing, no suprise there... 
    pip3.10 install pyaudio <---- This allowed the pgm to run, however, It's still not printing anything out... idk if the pgm is batched or my mic is nor working idk, but at least it didnt error out agian 

'''

import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

if __name__ == "__main__":
    speech_to_text()
