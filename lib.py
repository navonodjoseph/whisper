import pyaudio
import wave
import os
from peewee import * 

db = PostgresqlDatabase(
    'whisper', # name of database
    user = '', # name of user
    password= '', # password
    host = 'localhost', # name of host
    port = 5432 # port 
)

# connect to database 
db.connect()

# setup audio recordings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5

# set output folder 
output_folder = 'recordings'
output_file = 'recording.wav'


# create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#create instance of PyAudio 
audio = pyaudio.PyAudio()

# start recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

# stop recording
stream.stop_stream()
stream.close()
audio.terminate()

print('finished recording')

# save the recording to a WAV file 
wf = wave.open(os.path.join(output_folder, output_file), 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
