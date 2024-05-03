import wave
import json

from vosk import Model, KaldiRecognizer, SetLogLevel
import Word as custom_Word
import time 
#from RunSecond_transcriptToBleeps import *  #from transcriptToBleeps import *

def get_epoch_time():
    epoch_time = int(time.time())
    return epoch_time

def epoch_to_human_readable(epoch_time):
    human_readable_time = time.strftime("%m-%d-%Y_%H-%M-%S-%f", time.localtime(epoch_time))
    return human_readable_time 

#Modified to specify storage folder location (writing "." should put it in the same folder w/ the python file being executed...)
def transcript(audio_filename, index, time_offset, storeTextFolder):
    #model_path = "vosk-model-en-us-0.42-gigaspeech" #Biggest & most accurate model (longest to run-> slowest) (demo ~30-32 sec)
    model_path = "vosk-model-small-en-us-0.15" #(probably) Fastest & smallest Model to run [LEAST ACCURATE] (demo ~2 sec - INSANELy fast)
    #model_path = "vosk-model-en-us-0.22" #middle-man: Larger Size, accurate enough, (far more than smallest mode, but runtime is still ~x10 more than fastest model) (demo ~20 sec -> Middle of the road, but definitely on the larger side)
    
    #audio_filename = "RIP_Riley_ShittingThunder.wav"#"audio/speech_recognition_systems.wav"

    model = Model(model_path)
    wf = wave.open(audio_filename, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    # get the list of JSON dictionaries
    results = []
    # recognize speech using vosk model
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            part_result = json.loads(rec.Result())
            results.append(part_result)
    part_result = json.loads(rec.FinalResult())
    results.append(part_result)

    # convert list of JSON dictionaries to list of 'Word' objects
    list_of_Words = []
    for sentence in results:
        if len(sentence) == 1:
            # sometimes there are bugs in recognition 
            # and it returns an empty dictionary
            # {'text': ''}
            continue
        for obj in sentence['result']:
            w = custom_Word.Word(obj)  # create custom Word object
            list_of_Words.append(w)  # and add it to list

    wf.close()  # close audiofile

    # output to the screen
    """ for word in list_of_Words:
        #print("FUCK! - " )
        print(word.to_string()) """
        
    currentTimeEpoch = get_epoch_time()
    currentTimeHumanReadable = epoch_to_human_readable(currentTimeEpoch)
    
    outputFileName = storeTextFolder + currentTimeHumanReadable + ".txt" # Updated to work w/ storeTextFolder 
    #outputFileName = storeTextFolder + "output" + str(index) + ".txt" # Updated to work w/ storeTextFolder 
    with open(outputFileName, 'w') as file:
        for word in list_of_Words:
            #file.write(str(item) + '\n')
            #file.write(word.to_string() + "\n")
            
            #---get 2nd item in the "array" if possible (or split @ '/n' ), THEN split @ " > ", THEN convert both string to ints, add the time offset, RECONSTRUCT THE STRING WITH THE OFFSETS, AND RE-INSERT IT BACK INTO THE THING (AAAH!)
            temp = word.to_string().split('\n')
            #print(temp)
            temp1 = temp[1].split('>')
            #print("TEMP1: " + str(temp[1]))
            #print("OFFSET: " + str(time_offset))
            
            counter = 0 
            for i in temp1: 
                temp1[counter] = float(temp1[counter]) + time_offset
                counter += 1
            temp[1] = str(temp1[0]) + " > " + str(temp1[1])
            print(temp)
            
            output = temp[0] + '\n' + temp[1] + '\n' + temp[2] + '\n'
            
            #file.write(word.to_string() + "\n")
            
            file.write(output + "\n")
            
            
    
#transcript("tempAudio_0.wav", 0, 20) #FOR TESTING ONLY            
                