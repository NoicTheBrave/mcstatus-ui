'''
Author: Nicholas Chorette (kinda - just like the other example files I ripped from the githubs, you get my point)
Date: 5/2/2024
Purpose: To see if I can do audio-to-text transcribing, like, PROPER transcribing w/ timestamps... thus far, I cannot find the timestamps... maybe docs mention it. 

NOTE: 
Demo below APPEARS to try and use MULTIPLE different examples of audio-to-transcribing programs & methods... 
Interestingly enough, it goes as far to do that JUST for you to try and compare them. 

I personally could care less about SOME of them, but it would be nice if I could quickly transcribe WITH TIME STAMPS, w/ 2 or even 3 pgms at the same time, in parallel or even threadded, just to compare the texts with one another, find any discrepancies, and MAYBE get an average/majority of what was believed to have been said by most of them, and use that word, w/ respective time stamps... but again, NOT REQUIRED, and so if you ...


if you DONT have the programs for the demo below, @ lest get 1 of them, (one may come w/ the demo itself, idk), but if you just RUN it as-is from the github, it WILL throw errors,

EXPECT THE ERRORS

'''

#This is DIFFERENT from my other transcribe methods, to my knowledge since I believe the OTHER transcribing method used that downloaded library or whatever to work, where this uses the same lib for listening to my mic and stuff as the other examples in this folder... 
#Idealy, if after every sentence I say gets turned into an audio file, and idk if the audio file is wiritten when I stop talking or while I am talking, lets assume I just keep EVERY SINGLE ONE (audio file) for the sake of argument... 
#   ... then I wanna be able to transcribe what I said AS SOON as possible, so I can then, idealy, later down the chain edit the audio file after a word I dont like that I said (swear or other word) is detected -> edit the audio -> Re-stitch together OR played side-by-side (might save more time that way) thru OBS output or streaming output, idk mang, somethin, so my filtered audio gets played over my video 
#    ... might have to make my own python pgm to record video & audio seporately, or mute/remove the video's audio and play the filtered audio over the video (IDEALY not stitching them back together after the audio is edited, BUT where they still line-up would be excelent, THEN that resulting prodsuct be sent to OBS, somehow, idk mang, and streamed to ppl... idk bro.)

#https://github.com/Uberi/speech_recognition/blob/master/examples/audio_transcribe.py

#needed THIS as wel as the speach lib:
#  pip3.10 install pocketsphinx
# pip3.10 install google-api-python-client
# (as mentioned in documentation) -> https://pypi.org/project/SpeechRecognition/ (Scroll to the "requirements" section and youll see it... VOSK is there too.... how strange... )



#!/usr/bin/env python3

import speech_recognition as sr

# obtain path to "english.wav" in the same folder as this script
from os import path

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "microphone-results.wav")
#AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "english.wav")

# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# recognize speech using Google Cloud Speech
GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""
try:
    print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))

# recognize speech using Wit.ai
WIT_AI_KEY = "INSERT WIT.AI API KEY HERE"  # Wit.ai keys are 32-character uppercase alphanumeric strings
try:
    print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
except sr.UnknownValueError:
    print("Wit.ai could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Wit.ai service; {0}".format(e))

# recognize speech using Microsoft Azure Speech
AZURE_SPEECH_KEY = "INSERT AZURE SPEECH API KEY HERE"  # Microsoft Speech API keys 32-character lowercase hexadecimal strings
try:
    print("Microsoft Azure Speech thinks you said " + r.recognize_azure(audio, key=AZURE_SPEECH_KEY))
except sr.UnknownValueError:
    print("Microsoft Azure Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Azure Speech service; {0}".format(e))

# recognize speech using Microsoft Bing Voice Recognition
BING_KEY = "INSERT BING API KEY HERE"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
try:
    print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY))
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

# recognize speech using Houndify
HOUNDIFY_CLIENT_ID = "INSERT HOUNDIFY CLIENT ID HERE"  # Houndify client IDs are Base64-encoded strings
HOUNDIFY_CLIENT_KEY = "INSERT HOUNDIFY CLIENT KEY HERE"  # Houndify client keys are Base64-encoded strings
try:
    print("Houndify thinks you said " + r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY))
except sr.UnknownValueError:
    print("Houndify could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Houndify service; {0}".format(e))

# recognize speech using IBM Speech to Text
IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE"  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE"  # IBM Speech to Text passwords are mixed-case alphanumeric strings
try:
    print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))
except sr.UnknownValueError:
    print("IBM Speech to Text could not understand audio")
except sr.RequestError as e:
    print("Could not request results from IBM Speech to Text service; {0}".format(e))