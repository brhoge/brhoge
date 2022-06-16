import subprocess
import os
import random
from moviepy.editor import *

here = os.path.dirname(os.path.abspath(__file__))
os.chdir(f'{here}\\Content\\Movies\\bmo')

# Select random videos to combine
vid_list = os.listdir()
random_vids = random.sample(vid_list, 3)

# Make list of moviepy clips
clip_list = []
for vid in random_vids:
    clip = VideoFileClip(vid)
    clip_list.append(clip)

# Combine clips into video
final_vid = concatenate_videoclips(clip_list)

#Write final video to loading.mp4
os.chdir(here)
final_vid.write_videofile('Content\\Movies\\loading.mp4')
subprocess.run('Binaries\\Win64\\Borderlands3.exe')
