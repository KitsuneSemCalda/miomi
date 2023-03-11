#!/usr/bin/env python3

import pytube
import os
import pathlib
from threading import Thread


home_dir = os.path.expanduser("~")
videos_dir = os.path.join(home_dir, "Vídeos")

def download_video(url, resolution):
    video = pytube.YouTube(url)
    stream = video.streams.filter(resolution=resolution, progressive=True).first()
    print(f"Baixando video: {video.title} na resolução: {resolution}")
    
    file_path = pathlib.Path.home() / "Vídeos" / f"{video.title}.mp4"
    
    if os.path.exists(file_path):
        print(f"O arquivo {file_path} já existe!")
        return

    confirm = str(input("Deseja baixar o vídeo? (s/n): "))
    if confirm.lower() == "s":
        download_thread = Thread(target=stream.download, args=(videos_dir,))
        download_thread.start()
    else:
        print("Operação cancelada pelo usuário")
