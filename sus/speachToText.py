
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
