from tkinter import *
from tkinter import ttk
#Importa o TKINTER para desenvolver a interface

cor1= "#3B3B3B"
cor2= "#FEFFFF"
cor3= "#38576B"
cor4= "#ECEFF1"
cor5= "#FFAB40"
#cores

janela =Tk()
janela.title("Calculadora")
#cria a janela

janela.geometry("535x618")
janela.config(bg=cor1)
#define o tamanho da janela (largura x altura)

frame_tela = Frame(janela, width=535, height=120, bg=cor3)
frame_tela.grid(row=0, column=0)
#cria um frame separado na inteface da aplicação para exibir os resultados

frame_corpo = Frame(janela, width=535, height=498, bg=cor2)
frame_corpo.grid(row=1, column=0)
#cria o frame inferior

b_1 = Button(frame_corpo, text="C", width=20, height=4)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, text="%", width=20, height=4)
b_2.place(x=185, y=0)

b_2 = Button(frame_corpo, text="/", width=20, height=4)
b_2.place(x=340, y=0)

janela.mainloop()