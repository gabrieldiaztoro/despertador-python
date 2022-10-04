from tkinter.ttk import *
from tkinter import *

# importando pillow (imagens)
from PIL import Image, ImageTk

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
imagem_despertador = Image.open('imagens/despertador.png')
imagem_despertador = imagem_despertador.resize((120, 100))
imagem_despertador = ImageTk.PhotoImage(imagem_despertador)

l_imagem_despertador = Label(
    frame_baixo, height=100, image=imagem_despertador, compound=LEFT, padx=10, anchor=NW, font=('Ivi 16 bold'), bg=cor1, fg=cor3)
l_imagem_despertador.place(x=10, y=10)

# nao precisei criar outra variavel, eu adicionei juntas no mesmo.

#imagem_csv = Image.open('imagens/idades.png')
#imagem_csv = imagem_csv.resize((50, 50))
#imagem_csv = ImageTk.PhotoImage(imagem_csv)

# Label texto Alarme
l_imagem_despertador = Label(frame_baixo, text="ALARME",
                             height=1, anchor=NE, font=('Ivi 15 bold'), bg=cor1, fg=cor3)
l_imagem_despertador.place(x=160, y=0)


janela.mainloop()
