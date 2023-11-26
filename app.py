# V4
import os
import torch
from file_cleanup import source_file
from combined_audios import combined_audio

device = torch.device('cpu')
torch.set_num_threads(4)
local_file = 'model.pt'

if not os.path.isfile(local_file):
    torch.hub.download_url_to_file('https://models.silero.ai/models/tts/en/v3_en.pt',
                                   local_file)  

model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
model.to(device)

# example_text = "Hello, World!"
#example_batch = ["Hello","World!"]

files = os.listdir("./")
print("The text files in the current folder:- ")
for i in files:
    if ".txt" in i:
        print(i.capitalize())


file_name = input("""\nenter the name of your text file
the source file must be located in the current directory
no need to append .txt 
>>>  """)
example_batch = source_file(f"./{file_name}.txt")
sample_rate = 48000
speaker='en_99'



s = ""
for i in range(len(example_batch)):
    example_text = example_batch[i]
    strnum = str(i+1)

    if os.path.isfile(f"news{strnum}.wav"):
        s += f" S:\\silero\\{file_name}{strnum}.wav"
        continue
    else:
        audio_paths = model.save_wav(text=example_text,
                                     speaker=speaker,
                                     sample_rate=sample_rate)
                                     
        # renaming file
        renaming_file = os.system(f"ren test.wav news{strnum}.wav" )
        s += f" S:\\silero\\news{strnum}.wav"

combined_audio(s,file_name)
print(s)
