#python pip install pytube 
from pytube import YouTube
import os 

link = str(input("Enter Your Link: "))
yt = YouTube(link)

song = yt.streams.get_highest_resolution().download()

#You can remove everything below if you want the full video and audio downloaded 
filetype = [
    ("mp3", "*.mp3")
]
new_name = os.path.splitext(song)
os.rename(song, new_name[0] + '.mp3' )
print("Download Successful")

