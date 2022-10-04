
from pygame import mixer
import time
from datetime import datetime
from time import sleep
from threading import Thread


from tkinter import *

janela = Tk()
janela.title("DESPERTADOR")
janela.geometry('350x150')


def tocar_alarme():

    mixer.music.load()
    mixer.music.play()


def alarme():
    while True:
        control = 1
        h_alarme = "?"
        m_alarme = "?"
        s_alarme = "?"
        p_alarme = "?"

        hora_atual = datetime.now

        hora = hora_atual.strftime("%I")
        minuto = hora_atual.strftime("%M")
        segundo = hora_atual.strftime("%S")
        periodo = hora_atual.strftime("%p")

        if control == 1:
            if p_alarme == periodo:
                if h_alarme == hora:
                    if m_alarme == minuto:
                        if s_alarme == segundo:
                            tocar_alarme()

        sleep(1)


t1 = Thread(target=alarme)
t1.start()
mixer.init()

janela.mainloop()
