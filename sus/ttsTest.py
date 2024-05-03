from gtts import gTTS
import os

# Text to be converted to speech
text = "Hello! This is an example of text-to-speech using Python."

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine, slow=False to make the speed normal
speech = gTTS(text=text, lang=language, slow=False)

# Saving the converted audio in a file named example.mp3
speech.save("example.mp3")

# Playing the converted file
os.system("start example.mp3")
