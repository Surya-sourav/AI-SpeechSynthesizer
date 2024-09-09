from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts
import soundfile as sf  # To save the output as a wav file

# Step 1: Load the model configuration
config = XttsConfig()
config.load_json("/home/omtrimoco/tts_project/Assets/config.json")

# Step 2: Initialize the model
model = Xtts.init_from_config(config)

# Step 3: Load the pre-trained weights
model.load_checkpoint(config, checkpoint_dir="/home/omtrimoco/tts_project/Assets", eval=True)

# Optional: If you have CUDA installed and want to use GPU, uncomment the line below
# model.cuda()

f= open('data.txt','r')
data = f.read()
f.close()


def createTTS(text,input_audio,output_audio):
# Step 4: Synthesize the output
    outputs = model.synthesize(
        data,
        config,
        speaker_wav= input_audio,  # Replace with the correct path
        gpt_cond_len=3,
        language="en",
    )

    # Step 5: Save the synthesized speech to a wav file
    output_wav = outputs['wav']
    sf.write(output_audio, output_wav, config.audio.sample_rate)

    print("Speech synthesis complete and saved to output.wav")

# createTTS("How are you ?" , "input.wav", "output.wav")

import sqlite3

conn = sqlite3.connect('tts.db')

cursor = conn.cursor()

def createTable():
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT ,text TEXT NOT NULL)''')

def createTask(text):
        
    cursor.execute("INSERT INTO tasks (text) VALUES(?)",(text, ))
    conn.commit()


def fetchTasks():
    cursor.execute("SELECT * FROM tasks")

    rows = cursor.fetchall()

print(fetchTasks())
conn.close()
 
