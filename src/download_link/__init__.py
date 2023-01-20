import pytube
import pytube.exceptions
import messageSystem
import os

music_path = str(os.getenv("HOME")) + "/Música/"
video_path = str(os.getenv("HOME")) + "/Vídeos/"

def is_playlist(url):
    try:
        pytube.YouTube(url)
        return False
    except pytube.exceptions.RegexMatchError:
        return True

def download_video_in_format_audio(url):
    youtube = pytube.YouTube(url)
    
    title = youtube.title
    messageSystem.alert_message(f"Estamos baixando o vídeo: {title} no formato de audio")
    
    audiostream = youtube.streams.get_audio_only()
    audiostream.download(music_path)
    messageSystem.sucess_message("O vídeo foi baixado com sucesso no formato de audio")

def download_video_in_highest_resolution(url):
    youtube = pytube.YouTube(url)
    
    title = youtube.title
    messageSystem.alert_message(f"Estamos baixando o vídeo: {title} na maior resolução")
    
    videostream = youtube.streams.get_highest_resolution()
    videostream.download(video_path)
    messageSystem.sucess_message("O vídeo foi baixado com sucesso na maior resolução")

def download_playlist_in_format_audio(url):
    youtube = pytube.Playlist(url)
    
    playlist_location = music_path + youtube.title

    title = youtube.title
    messageSystem.alert_message(f"Estamos baixando uma playlist inteira: {title} em formato audio")

    for audio in youtube.videos:
        audio.streams.get_audio_only().download(playlist_location)
    messageSystem.sucess_message(f"Esta playlist foi baixada com sucesso no formato audio")

def download_playlist_in_highest_resolution(url):
    youtube = pytube.Playlist(url)
    
    playlist_location = video_path + youtube.title

    title = youtube.title
    messageSystem.alert_message(f"Estamos baixando uma playlist inteira: {title} na maior resolução")

    for video in youtube.videos:
        video.streams.get_highest_resolution().download(playlist_location)
    messageSystem.sucess_message(f"Esta playlist foi baixada com sucesso na maior resolução")

def download_audio(url):
    if not is_playlist(url):
        download_video_in_format_audio(url)
    else:
        download_playlist_in_format_audio(url)

def download_video(url):
    if not is_playlist(url):
        download_video_in_highest_resolution(url)
    else:
        download_playlist_in_highest_resolution(url)
