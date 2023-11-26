# Combine all the audio files.
import os

def combined_audio(s,filename):
    """ 1) takes the names of the files and then stiches them together.
        2) will use the source txt file name for the final combined audio file name.
        3) does accept arg for a file name of choice """  
    os.chdir("C:\Program Files (x86)\sox-14-4-2")
    combining_files = os.system(f"sox{s} S:\\silero\\all_audios\\{filename}.wav" )
