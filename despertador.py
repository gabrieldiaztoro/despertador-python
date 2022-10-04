from tkinter.ttk import *
from tkinter import *

from pygame import mixer
import time
from datetime import datetime
from time import sleep
from threading import Thread


# importando pillow (imagens)
from PIL import Image, ImageTk

# instalando o pygame (som)
from pygame import mixer

# cores
cor0 = "f0f3f5"   # --preto
cor1 = "#FFFFFF"  # --branca
cor2 = "#d6872d"  # --ouro
cor3 = "#fc766d"  # --vermelho
cor4 = "#403d3d"  # --preto
cor5 = "#4a88e8"  # --azul

janela = Tk()
janela.title("DESPERTADOR")
janela.geometry('350x150')
janela.configure(background=cor1)
janela.resizable(width=FALSE, height=FALSE)


# Dividindo frames

frame_logo = Frame(janela, width=350, height=10, bg=cor2)
frame_logo.grid(row=0, column=0, pady=1, padx=0)

frame_baixo = Frame(janela, width=350, height=290, bg=cor1)
frame_baixo.grid(row=1, column=0, pady=1, padx=0)

# Label logo
l_linha = Label(frame_logo, text="Alarme", width=400,
                bg=cor2,  anchor=NW, font=('Ivi 20 bold'))
l_linha.place(x=0, y=30)

# Adicionando Imagem despertador
imagem_despertador = Image.open('arquivos/despertador.png')
imagem_despertador = imagem_despertador.resize((120, 100))
imagem_despertador = ImageTk.PhotoImage(imagem_despertador)

l_imagem_despertador = Label(
    frame_baixo, height=100, image=imagem_despertador, compound=LEFT, padx=10, anchor=NW, font=('Ivi 16 bold'), bg=cor1, fg=cor3)
l_imagem_despertador.place(x=0, y=10)

# nao precisei criar outra variavel, eu adicionei juntas no mesmo.
#imagem_csv = Image.open('imagens/idades.png')
#imagem_csv = imagem_csv.resize((50, 50))
#imagem_csv = ImageTk.PhotoImage(imagem_csv)

# Label texto Alarme
l_imagem_despertador = Label(frame_baixo, text="ALARME",
                             height=1, anchor=NE, font=('Ivi 15 bold'), bg=cor1, fg=cor3)
l_imagem_despertador.place(x=160, y=0)


# criando box e labels dos box (HORAS)
c_hora = Combobox(frame_baixo, width=2, font=('Ivi 12'))
c_hora['value'] = ("00", "01", "02", "03", "04", "05",
                   "06", "07", "08", "09", "10", "11", "12")
c_hora.current(0)
c_hora.place(x=130, y=50)

l_imagem_horas = Label(frame_baixo, text="HORAS",
                       height=1, anchor=NW, font=('Arial 7 bold'), bg=cor1, fg=cor4)
l_imagem_horas.place(x=130, y=30)


# criando box e labels dos box (MINUTOS)
c_minutos = Combobox(frame_baixo, width=2, font=('Ivi 12'))
c_minutos['value'] = ("00", "01", "02", "03", "04", "05",
                      "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_minutos.current(0)
c_minutos.place(x=180, y=50)

l_imagem_minutos = Label(frame_baixo, text="MINUTOS",
                         height=1, anchor=NW, font=('Arial 7 bold'), bg=cor1, fg=cor4)
l_imagem_minutos.place(x=175, y=30)


# criando box e labels dos box (segundos)
c_segundos = Combobox(frame_baixo, width=2, font=('Ivi 12'))
c_segundos['value'] = ("00", "01", "02", "03", "04", "05",
                       "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_segundos.current(0)
c_segundos.place(x=230, y=50)

l_imagem_segundos = Label(frame_baixo, text="SEGUNDOS",
                          height=1, anchor=NW, font=('Arial 7 bold'), bg=cor1, fg=cor4)
l_imagem_segundos.place(x=230, y=30)


# criando box e labels dos box (PERIODO)
c_periodo = Combobox(frame_baixo, width=3, font=('Ivi 12'))
c_periodo['value'] = ("AM", "PM")
c_periodo.current(0)
c_periodo.place(x=290, y=50)

l_imagem_periodo = Label(frame_baixo, text="PERIODO",
                         height=1, anchor=NW, font=('Arial 7 bold'), bg=cor1, fg=cor4)
l_imagem_periodo.place(x=290, y=30)


# CRIANDO RADIO ATIVAR
def ativar_alarme():
    if selecionado.get() == 1:
        print('Ativar: ', selecionado.get())
    else:
        t1 = Thread(target=alarme)
        t1.start()


def desativar_alarme():
    print('Alarme desativado: ', selecionado.get())
    mixer.music.stop


selecionado = IntVar()


radio = Radiobutton(frame_baixo, command=ativar_alarme, text='Ativar', value=1,
                    variable=selecionado, font='Arial 8', bg=cor1, fg=cor4)
radio.place(x=125, y=95)

# CRIANDO FUNCOES DO ALARME


def tocar_alarme():

    mixer.music.load()
    mixer.music.play()
    selecionado.set(0)

    radio = Radiobutton(frame_baixo, command=desativar_alarme, text='Desativar', value=1,
                        variable=selecionado, font='Arial 8', bg=cor1, fg=cor4)


radio.place(x=187, y=95)


def alarme():
    while True:
        control = selecionado.get()
        h_alarme = c_hora.get()
        m_alarme = c_minutos.get()
        s_alarme = c_segundos.get()
        p_alarme = c_periodo.get().upper()

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
                            print("hora de fazer pausa")
                            tocar_alarme()
                            ativar_alarme()

        sleep(1)


t1 = Thread(target=alarme)
# iciar o thread

t1.start()
mixer.init()


janela.mainloop()
