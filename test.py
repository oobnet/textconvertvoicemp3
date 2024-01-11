from gtts import gTTS
import time , subprocess,os
from subprocess import call


def countDown():
    for i in range (10):
        print(i, end='')
        time.sleep(1)


text = "ESTE E UM TESTE PARA O ROBOR LER  TUDO QUE EU ESCREVO"

language = "pt-BR"

speech = gTTS(text = text, lang = language, slow = False)

speech.save("text.mp3")

mp3 = os.getcwd()+'/text.mp3'

#linha para abrir o audio
# subprocess.call(['xdg-open', mp3])
