from sys import argv
from pydub import AudioSegment
from pydub.playback import play
from os.path import exists
from io import BytesIO
from typing import List

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


# Converts a string to a byte array and returns the result
def convertStringtoBytes(string: str) -> bytes:
    return bytes(string, 'utf-8')


def createAudioFromBytes(bytesArray: bytes):
    return AudioSegment.from_file(BytesIO(bytesArray), format="mp3")


# Main process
def main(argc, argv) -> None:
    (audio, message) = entryVerification(argc, argv)

    bMsg = convertStringtoBytes(message)

    hiddenAudio = createAudioFromBytes(bMsg)

    finalAudio = audio.overlay(hiddenAudio)

    play(finalAudio)



#
if __name__ == "__main__":
    main(len(argv), argv)