from moviepy.editor import *
#makesure mp4 file is in your program folder
#enter file name with extension in mp4_file
mp4_file = ""
#rename a.mp3 to whatever you want
mp3_file = "a.mp3"

videoClip = VideoFileClip(mp4_file)

audioclip = videoClip.audio

audioclip.write_audiofile(mp3_file)

audioclip.close()

videoClip.close()
