from gtts import gTTS
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


