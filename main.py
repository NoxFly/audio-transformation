from sys import argv
from pydub import AudioSegment
from pydub.playback import play
from os.path import exists
from io import BytesIO
from typing import List
from gtts import gTTS
import numpy as np
import os
import speech_recognition as sr

r = sr.Recognizer()

# Show command usage
def showUsage() -> None:
    print("Usage : " + argv[0] + " <audioPath> <sentence>")

# Checks if given arguments are well formed.
# If not, then exit the program.
# If yes, then returns a tuple (audio, message)
def entryVerification(argc: int, argv: List[str]) -> tuple[AudioSegment, str]:
    if argc < 2:
        print("Missing audio file to read.")
        showUsage()
        exit(1)

    if(argc < 3):
        print("Missing sentence to insert in to the audio.")
        showUsage()
        exit(2)

    if not exists(argv[1]):
        print("File does not exist.")
        exit(3)

    if not (argv[1].endswith('.mp3') or argv[1].endswith('.wav')):
        print("Unsupported audio format.")
        exit(4)

    try:
        audio = AudioSegment.from_file(argv[1])

        return (audio, argv[2])

    except:
        print("Could not load audio")
        exit(5)


# Never used
def convertStringtoBytes(string: str) -> bytes:
    return bytes(string, 'utf-8')   

# Never used
def createAudioFromBytes(bytesArray: bytes):
    return AudioSegment.from_file(BytesIO(bytesArray)).export("resources/audio/result.mp3",format="mp3")


def createAudiofromString(msg: str) -> AudioSegment:
    language = 'fr'
    myobj = gTTS(text=msg, lang=language, slow=False)
    myobj.save("resources/audio/tmp/tmp.mp3")
    audio = AudioSegment.from_mp3("resources/audio/tmp/tmp.mp3")
    os.remove("resources/audio/tmp/tmp.mp3")
    return audio

def readMessagefromAudio(path: str,lang = 'fr'):
    if not path.endswith(".wav"):
        print("Unsupported audio format.")
        exit(6)
    
    with sr.AudioFile(path) as source:
        audio_file = r.record(source)
        try:
            print(r.recognize_google(audio_file, language=lang))
        except:
            print("No message found.")
            exit(7)

# Main process
def main(argc, argv) -> None:
    (audio, message) = entryVerification(argc, argv)

    positions = [1000, 5000, 9000, 13000, 17000, 21000, 25000] # toutes les 4 sec

    # -- Avant le 24/09S
    #bMsg = convertStringtoBytes(message)
    #hiddenAudio = createAudioFromBytes(bMsg)

    hiddenAudio = createAudiofromString(message)
    hiddenAudio = hiddenAudio - 22
    audio = audio - 20
    for position in positions:
        audio = audio.overlay(hiddenAudio, position=position)
    
    finalAudio = audio

    finalAudio.export("resources/audio/results/result.wav", format="wav")

    readMessagefromAudio("resources/audio/results/result.wav")

#
if __name__ == "__main__":
    main(len(argv), argv)