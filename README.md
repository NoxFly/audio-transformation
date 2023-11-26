# Text-To-Speech Adversarial Attack

University project.

The goal is to manipulate audio to superimpose different audio, and even create audio to hide in another.

This is to reproduce the Adverse Examples attacks.


## Requires

1. Install python3 (with pip)
1. Install all needed packages (PyDub, gTTS, Numpy, SpeechRecognition, ffmpeg) : `pip install pydub gtts numpy SpeechRecognition ffpmeg`
1. Install ffmpeg on OS :
    * On Windows :
        1. Download the zip : `https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip`
        1. Extract to get the bin/ folder
        1. Add the bin/ folder to the env path
    * On linux : `sudo apt-get install ffmpeg`

## Execution

```py
# use py or python3 depending what you have
py main.py <audio_path> <text-to-speech>
```

## Licence

This repository has the [MIT licence](./LICENCE)
