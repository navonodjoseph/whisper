import configparser
import requests 
import os


# read config file  
config = configparser.ConfigParser()
config.read('config.ini')
api_key=config['whisper_ai']['api_key']

# set file path and API endpoint
file_path = 'recordings/recording.wav'
api_endpoint = 'https://api.whisper.ai/transcriptions'

# read the WAV file contents
with open(file_path, 'rb') as f:
    audio_content = f.read()

# send request to API
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'audio/wav'
}

response = requests.post(api_endpoint, headers=headers, data=audio_content)

# check conditions to see if request is successful
if response.status_code !=200 :
    print('Error:', response.json()['message'])
else:
    transcription = response.json()['transcription']
    print('Transcription:', transcription)

    #save transcription 
    output_folder = 'transcriptions'
    output_file = 'transcription.txt'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    with open(os.path.join(output_folder, output_file), 'w') as f:
        f.write(transcription)

