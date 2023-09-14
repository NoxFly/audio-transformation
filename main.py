from sys import argv
from pydub import AudioSegment
from pydub.playback import play
from os.path import exists

def showUsage() -> None:
    print("Usage : " + argv[0] + " <audioPath> <sentence>")

def main(argc, argv) -> None:
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
        loop = AudioSegment.from_file(argv[1])
    except:
        print("Could not load audio")

    try:
        play(loop)
    except:
        print() # if Ctrl^C



if __name__ == "__main__":
    main(len(argv), argv)