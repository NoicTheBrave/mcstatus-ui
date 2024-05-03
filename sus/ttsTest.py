'''
Author: Nicholas Chorette
Date: 5/2/2024
Purpose: If I would like to add a nice TTS ability to my program, I can. If I want to even just play audio files as well, I now have that ability as well. Extreemly useful if I would like to add TTS, or even play audio of an mp3, to any application :) 
'''

#pip install pygame
#pip install gTTS

from gtts import gTTS
#from playMP3Pygame import *
#import os

import pygame

def play_music(file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print("Error occurred:", str(e))
    finally:
        pygame.mixer.quit()
        pygame.quit()


def tts_textToMP3(text,fileName): 
    # Text to be converted to speech
    #text = msg

    # Language in which you want to convert
    language = 'en' #I speak english, one of the most common languages, so it will stay english for my code

    # Passing the text and language to the engine, slow=False to make the speed normal
    speech = gTTS(text=text, lang=language, slow=False)

    # Saving the converted audio in a file named example.mp3
    speech.save(fileName)
    #speech.save("example.mp3")  


#pygame stuff
file_name = "example.mp3" ##"your_file_path.mp3"  # Change this to the path of your MP3 file
msg = "Hello! This is an example of text-to-speech using Python."

tts_textToMP3(msg, file_name)

play_music(file_name)


# Playing the converted file
#os.system("start example.mp3")



