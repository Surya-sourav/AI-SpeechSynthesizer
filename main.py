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

# Step 4: Synthesize the output
outputs = model.synthesize(
    "It took me quite a long time to develop a voice and now that I have it I am not going to be silent.",
    config,
    speaker_wav="input.wav",  # Replace with the correct path
    gpt_cond_len=3,
    language="en",
)

# Step 5: Save the synthesized speech to a wav file
output_wav = outputs['wav']
sf.write('output.wav', output_wav, config.audio.sample_rate)

print("Speech synthesis complete and saved to output.wav")