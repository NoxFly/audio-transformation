from sys import argv
from pydub import AudioSegment
from pydub.playback import play


def main(argc, argv) -> None:
    print("Argument count :", argc)
    print("Arguments :", argv)

    loop = AudioSegment.from_wav("metallic.wav")

    play(loop)



if __name__ == "__main__":
    main(len(argv), argv)