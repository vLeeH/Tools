import os
try:
    from moviepy.editor import *
except ImportError:
    os.system("pip install moviepy")
if RuntimeError:
    os.system("pip install numpy==1.19.3")

print("IMPORTANT!\n.mp3 and mp4 file example: 'E:/audiofile.mp3' not is only 'audio'")
print("-" * 30)

mp4_file = []
mp3_file = []

a1 = int(0)
while True:
    a = str(input(".mp4 locate: "))
    b = str(input(".mp3 locate: "))
    mp4_file.append(a)
    mp3_file.append(b)
    a1 += 1
    print("Do you want to add more videos? [Y/N]").lower()
    inp = str(input("> "))
    if inp == "y":
        continue
    else:
        break


for i in range(0, a1):
    videoclip = VideoFileClip(mp4_file[i])
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file[i])
    print("\n")
