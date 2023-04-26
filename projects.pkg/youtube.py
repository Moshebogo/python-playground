from pytube import YouTube
from sys import argv
# the video to download
link = argv[1]
# the instance of the YouTube class
yt = YouTube(link)
# some data about the video
print("Title: ", yt.title)
print("Views: ", yt.views)
# choosing the highest resolution to download
yd = yt.streams.get_highest_resolution()
# saving the download in a file on local PC
yd.download("Youtube Downloads")