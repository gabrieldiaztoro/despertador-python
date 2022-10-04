from tkinter.ttk import *
from tkinter import *

# importando pillow (imagens)
from PIL import Image, ImageTk

# cores
cor0 = "f0f3f5"   # --preto
cor1 = "#FFFFFF"  # --branca
cor2 = "#d6872d"  # --ouro
cor3 = "#fc766d"  # --vermelho
cor4 = "#403d3d"  # --letra
cor5 = "#4a88e8"  # --azul

janela = Tk()
janela.title("DESPERTADOR")
janela.geometry('350x150')
janela.configure(background=cor1)
janela.resizable(width=FALSE, height=FALSE)


frame_cima = Frame(janela, width=400, height=200,
                   pady=0, padx=0, relief=FLAT, bg=cor2)
# - parte de cima da calculadora relief = estilo   'flat' ou FLAT, bg = background
frame_cima.grid(row=0, column=0)


l_alarme = Label(frame_cima, text="Alarme", width=18, height=1, padx=3,
                 relief='flat', anchor='center', font=('Ivi 20 bold'), bg=cor2, fg=cor3)
l_alarme.place(x=0, y=30)


janela.mainloop()
