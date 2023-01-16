import os
import pytube
import messageSystem
import download_link

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
    youtube = pytube.YouTube(url)
    with open(filepath, "a") as file:
        file.write(f"#{youtube.title} \n")
        file.write(str(url) + "\n")
        file.close()
    messageSystem.sucess_message(f"Adicionado o link: {url} ao arquivo queue_list")

def clearQueue(filepath):
    with open(filepath, "w") as file:
        file.write("")
    messageSystem.sucess_message("O arquivo queue_list foi limpo com sucesso")

def downloadQueue(filepath, mode):
    with open(filepath, "r") as file:
        bigtext = file.read()
        for url in bigtext.splitlines():
            if str(url).startswith("#"):
                pass
            else:
                if mode == "video":
                    download_link.download_video(url)
                if mode == "audio":
                    download_link.download_audio(url)
    clearQueue(filepath)

def readQueue(filepath):
    with open(filepath, "r") as file:
        bigtext = file.read()
        for text in bigtext.split():
            print(text)
            
