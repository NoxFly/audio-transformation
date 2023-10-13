# Text-To-Speech Adversarial Attack

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

## Execution

```py
# use py or python3 depending what you have
py main.py <audio_path> <text-to-speech>
```

## Licence

This repository has the [MIT licence](./LICENCE)
