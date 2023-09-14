# Audio transformation

University project.

The goal is to manipulate audio to superimpose different audio, and even create audio to hide in another.

This is to reproduce the Adverse Examples attacks.


## Requires

1. Install python3 (with pip)
1. Install PyDub : `pip install pydub`
1. Install ffmpeg :
    * On Windows : `pip install ffmpeg`
    * On linux : `sudo apt-get install ffmpeg`
1. Install Numpu : `pip install numpy`

## Run

```py
# use py or python3 depending what you have
py main.py [args]
```

For now, input entry is not used. Latter it may be the audio file to treat, or the sentence to create audio from (TTS).

## Licence

This repository has the [MIT licence](./LICENCE)