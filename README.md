# whisper
Simple experiment with whisper AI 

## Background
### 
Whisper AI is described as a speech recognition model. It's an AI tool that is designed to recognize speech, translate, transcribe, build captions, among other things. 

## Getting started
I'm going to give a quick over view of what you need to get started then run through some of the experiments I tried. 
You'll need to use python 3.10 or below to make this model work. You can check what version of python you're running with this command `python --version`. 

### Install PyTorch
PyTorch is a compliler you'll need to rewrite some of the bytecode before it's executed. Once you've started your pipenv shell you can`pip install torch torchvision torchaudio` (for Mac). Read more here: PyTorch documentation : https://pytorch.org/docs/stable/dynamo/index.html

### Install FFMPEG
This is a tool for reading the different audio files. `pip install ffmpeg`.
FFMPEG documentation: https://ffmpeg.org/documentation.html

### Finally, install Whisper AI
Run 'pip install -U openai-whisper` to instaill Whisper. 

### Basic Application
Now you can use Whisper to transcribe audio files. The most basic way to do this is to run `whisper <audiofile>`. The output will return a transcribed document with timestamps: ![whisper](https://files.slack.com/files-pri/T0351JZQ0-F055Y5EBPGR/image.png). 

It will also return several new files, all in different formats, that contains all of the transcribed text. 

### Experimentations
I built a audio recorder in Python using `pyaudio` and `wave`. In its current iteration it works as a voice memo app. And it pairs well with `Whisper` to record then transcribe audio files. 

### Next Steps 
- [X] Build audio recording app
- [] Automatically transcribe every audio file recorded in the app using `Whisper`
- [] 

