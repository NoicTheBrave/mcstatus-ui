#https://github.com/Uberi/speech_recognition/blob/master/examples/write_audio.py

#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# write audio to a WAV file
with open("microphone-resultsV2.wav", "wb") as f:
    f.write(audio.get_wav_data())
