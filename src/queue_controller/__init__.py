import os
import messageSystem

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
    with open(filepath, "a") as file:
        file.write(str(url) + "\n")
        file.close()
    messageSystem.sucess_message(f"Adicionado o link: {url} ao arquivo queue_list")

def clearQueue(filepath):
    with open(filepath, "w") as file:
        file.write("")
    messageSystem.sucess_message("O arquivo queue_list foi limpo com sucesso")

def downloadQueue(filepath):
    with open(filepath, "r") as file:
        bigtext = file.read()
        for url in bigtext.splitlines():
            messageSystem.alert_message(f"o link: {url}, foi lido com sucesso")
    clearQueue(filepath)
