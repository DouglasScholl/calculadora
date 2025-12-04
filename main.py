from tkinter import *
from tkinter import ttk
#Importa o TKINTER para desenvolver a interface

cor1= "#3B3B3B"
cor2= "#FEFFFF"
cor3= "#38576B"
cor4= "#ECEFF1"
cor5= "#FFAB40"
#cores

janela = Tk()
janela.title("Calculadora")
#cria a janela

janela.config(bg=cor1)
# Configurar pesos para responsividade
janela.grid_rowconfigure(0, weight=1)  # frame_tela
janela.grid_rowconfigure(1, weight=4)  # frame_corpo (maior que frame_tela)
janela.grid_columnconfigure(0, weight=1)

frame_tela = Frame(janela, bg=cor3)
frame_tela.grid(row=0, column=0, sticky='nsew')
#cria um frame separado na inteface da aplicação para exibir os resultados

frame_corpo = Frame(janela, bg=cor2)
frame_corpo.grid(row=1, column=0, sticky='nsew')
#cria o frame inferior
# Visor da calculadora usando Entry do Tkinter
display_var = StringVar()
display_font = ("Arial", 28, "bold")

frame_tela.grid_rowconfigure(0, weight=1)
frame_tela.grid_columnconfigure(0, weight=1)

entry = Entry(frame_tela, textvariable=display_var, font=display_font, bg=cor3, fg=cor2, justify=RIGHT, bd=0, relief=FLAT)
entry.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

# Lógica da calculadora
expression = ""

def update_display(value):
	display_var.set(value)

def add_to_expression(char):
	global expression
	expression += str(char)
	update_display(expression)

def clear():
	global expression
	expression = ""
	update_display("")

def backspace():
	global expression
	expression = expression[:-1]
	update_display(expression)

def calculate():
	global expression
	try:
		# Avalia a expressão atual com eval (uso local em app de calculadora)
		result = eval(expression)
		expression = str(result)
		update_display(expression)
	except Exception:
		expression = ""
		update_display("Erro")

def percent():
	global expression
	try:
		result = eval(expression) / 100
		expression = str(result)
		update_display(expression)
	except Exception:
		expression = ""
		update_display("Erro")

# Layout de botões usando grid para manter alinhamento responsivo
btn_font = ("Arial", 18)

buttons = [
	["C", "%", "⌫", "/"],
	["7", "8", "9", "*"],
	["4", "5", "6", "-"],
	["1", "2", "3", "+"],
]

for r, row in enumerate(buttons):
	for c, label in enumerate(row):
		if label == 'C':
			cmd = clear
		elif label == '⌫':
			cmd = backspace
		elif label == '%':
			cmd = percent
		else:
			cmd = lambda v=label: add_to_expression(v)
		btn = Button(frame_corpo, text=label, font=btn_font, command=cmd)
		btn.grid(row=r, column=c, sticky='nsew', padx=2, pady=2)

# Última linha: 0 (espalha por 2 colunas), '.', '='
btn_0 = Button(frame_corpo, text='0', font=btn_font, command=lambda: add_to_expression('0'))
btn_0.grid(row=4, column=0, columnspan=2, sticky='nsew', padx=2, pady=2)

btn_dot = Button(frame_corpo, text='.', font=btn_font, command=lambda: add_to_expression('.'))
btn_dot.grid(row=4, column=2, sticky='nsew', padx=2, pady=2)

btn_eq = Button(frame_corpo, text='=', font=btn_font, bg=cor5, command=calculate)
btn_eq.grid(row=4, column=3, sticky='nsew', padx=2, pady=2)

# Configure as colunas e linhas para expandir conforme o tamanho do frame
for i in range(4):
	frame_corpo.grid_columnconfigure(i, weight=1)
for i in range(5):
	frame_corpo.grid_rowconfigure(i, weight=1)

janela.mainloop()
#execução da janela principal da aplicação