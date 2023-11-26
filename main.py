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

def getDirectoryPath(path: str) -> str:
    return path[:path.rfind('/')] if os.path.splitext(path)[1] != '' else path

# create directory recursively if it does not exist
def ensureDirectoryExists(path: str) -> None:
    dirpath = getDirectoryPath(path)

    if not exists(dirpath):
        os.makedirs(dirpath)

# Never used
def convertStringtoBytes(string: str) -> bytes:
    return bytes(string, 'utf-8')   

# Never used
def createAudioFromBytes(bytesArray: bytes):
    return AudioSegment.from_file(BytesIO(bytesArray)).export("resources/audio/result.mp3",format="mp3")


def createAudiofromString(msg: str) -> AudioSegment:
    language = 'fr'
    myobj = gTTS(text=msg, lang=language, slow=False)

    filepath = "resources/audio/tmp/tmp.mp3"

    ensureDirectoryExists(filepath)

    myobj.save(filepath)
    audio = AudioSegment.from_mp3(filepath)
    os.remove(filepath)
    os.rmdir(getDirectoryPath(filepath))

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

    # -- Avant le 24/09S
    #bMsg = convertStringtoBytes(message)
    #hiddenAudio = createAudioFromBytes(bMsg)

    hiddenAudio = createAudiofromString(message)
    hiddenAudio = hiddenAudio - 22

    dHidden = hiddenAudio.duration_seconds
    dAudio = audio.duration_seconds

    # delay between each hidden message
    dmargin = 2 # seconds

    # number of times the hidden message will be repeated
    count = dAudio // (dHidden + dmargin)

    audio = audio - 20

    while count > 0:
        count -= 1
        position = count * (dHidden + dmargin) * 1000
        audio = audio.overlay(hiddenAudio, position=position)
    
    finalAudio = audio

    filepath = "resources/audio/results/result.wav"

    ensureDirectoryExists(filepath)

    finalAudio.export(filepath, format="wav")

    readMessagefromAudio(filepath)

#
if __name__ == "__main__":
    main(len(argv), argv)