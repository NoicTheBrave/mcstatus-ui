from TranscriptV3 import *
from pydub import AudioSegment 

audioname = "microphone-results.wav" # might not like it, if it is NOT mono-channel. if thats the case, an error will occur, and audio will need to be fed thru mono-channel converter pgm used for removing curse words as well.... ug

#if converting to mono-channel audio MUST happen, it would occure here! 

song = AudioSegment.from_file(audioname) #SHOULD ALWAYS be one of these 

# pydub does things in milliseconds 
songDuration = song.duration_seconds
time_div = (songDuration *1.0) #i didnt wanna change the code fully -0 lazy I am 

counter = 0 #again, i am lazy 

time_offset = counter * time_div#again, i am lazy 

#threads[i] = Thread(target=transcript, args=(audioBuffer[counter], counter, time_offset))
transcript(audioname, counter, time_offset)


#this SHOULD result in an output0.txt file, I hope :) 

