import os
import pytube
import alerts
import downloader 
import shutil

home = os.getenv("HOME")

docpath = str(home) + "/Documentos/"

dirpath = "/tmp/queue/"
filepath = dirpath + "queue_list.txt"

try:
    os.makedirs(dirpath)
except FileExistsError:
    pass
except FileNotFoundError:
    pass

try:
    with open(filepath) as file:
        file.close()
except FileExistsError:
    pass
except FileNotFoundError:
    pass

def incrementNewLink(filepath, url):
    if not downloader.is_playlist(url):
        youtube = pytube.YouTube(url)
        with open(filepath, "a") as file:
            file.write(f"#{youtube.title} \n")
            file.write(str(url) + "\n")
            file.close()
    else:
        playlist = pytube.Playlist(url)
        with open(filepath, "a") as file:
            file.write(f"#{playlist.title} \n")
            file.write(str(url) + "\n")
            file.close()
        alerts.sucess_message(f"Adicionado o link: {url} ao arquivo queue_list")

def clearQueue(filepath):
    with open(filepath, "w") as file:
        file.write("")
    alerts.sucess_message("O arquivo queue_list foi limpo com sucesso")

def downloadQueue(filepath, mode):
    try:
        with open(filepath, "r") as file:
            bigtext = file.read()
            for url in bigtext.splitlines():
                if str(url).startswith("#"):
                    pass
                else:
                    if mode == "video":
                        downloader.download_video(url)
                    if mode == "audio":
                        downloader.download_audio(url)
        clearQueue(filepath)
    except FileNotFoundError:
        alerts.warning_message("Não há nenhum queue_list para ser lido")

def download(url, mode):
    if mode == "video":
        downloader.download_video(url)
    if mode == "audio":
        downloader.download_audio(url)
 
def readQueue(filepath):
    try:
        with open(filepath, "r") as file:
            bigtext = file.read()
            for text in bigtext.splitlines():
                print(text)
    except FileNotFoundError:
        alerts.warning_message("não existe nenhum queue_list.txt para ser usado")

def persistent():
    try:
        shutil.copy(filepath, docpath)
    except FileNotFoundError:
        pass
