from moviepy.editor import VideoFileClip
import os

def extract_audio(file_path):
    if file_path.endswith((".mp4", ".mov", ".avi")):
        audio_path = file_path + ".wav"
        video = VideoFileClip(file_path)
        video.audio.write_audiofile(audio_path)
        return audio_path
    return file_path