# pip install youtube_dl

# Disclaimer: It is illegal to download copyrighted content from youtube. 
# However, for content that is within the law, you can use python to download 
# many youtube videos at once in case you want to watch them later offline:

import youtube_dl 
# Asks for the url
link = input("Write the url")
# Instantiate the YoutubeDL class from the youtube_dl framework
ydl = youtube_dl.YoutubeDL({})
# Download the video.
ydl.download([link])