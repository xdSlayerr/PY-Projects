from pytube import YouTube
from sys import argv


link = input('Link to video: (inside quotation marks)\n')
yt = YouTube(link)


print(f'Title: {yt.title}')

yd = yt.streams.get_highest_resolution()
yd.download('YT_Downloader\downloads')
print(f'Te video "{yt.title}" has been successfully downloaded from YouTube')