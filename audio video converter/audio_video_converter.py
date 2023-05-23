#importing the moviepy module
import moviepy.editor
#reading the video file
video = moviepy.editor.VideoFileClip('./test.mp4')
#converting the video file to audio file
audio = video.audio
#saving the audio file to mp3 format
audio.write_audiofile('audio_name.mp3')