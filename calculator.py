from tkinter import *
import tkinter as tk

valor_armazenado = ""

def botao_numero(numero):
    global valor_armazenado
    valor_armazenado += str(numero)
    resultado_label.config(text=valor_armazenado)
    print(valor_armazenado)

def dot():
    global valor_armazenado
    # Checa se o número atual já tem um ponto
    if "." not in valor_armazenado.split("+")[-1].split("-")[-1].split("*")[-1].split("/")[-1]:
        valor_armazenado += "."
        resultado_label.config(text=valor_armazenado)

def operacao(op):
    global valor_armazenado
    valor_armazenado += op
    resultado_label.config(text=valor_armazenado)

def resultado():
    global valor_armazenado
    try:
        valor_avaliado = eval(valor_armazenado)
        valor_armazenado = str(round(valor_avaliado, 2))
        resultado_label.config(text=valor_armazenado)
        print(valor_armazenado)
    except:
        resultado_label.config(text="Valor Inválido")
        valor_armazenado = ""
        print(valor_armazenado)


def limpar():
    global valor_armazenado
    valor_armazenado = ""
    resultado_label.config(text="")

tela_calculadora = Tk()
tela_calculadora.geometry("400x600") 
tela_calculadora.config(bg="black")

frame_central = Frame(tela_calculadora, bg='black') # grupo da tela - frame
frame_central.place(relx=0.5, rely=0.5, anchor=CENTER)

resultado_label = Label(frame_central, text='0', width=10, font=('Arial', 46), bg="gray", fg="white")
resultado_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

button_0 = Button(frame_central, command=lambda: botao_numero(0), text="0", width=4, height=2, font=('Arial', 20, 'bold'), fg='orange', bg='gray')
button_dot = Button(frame_central, command=dot, text=".", width=4, height=2, font=('Arial', 20, 'bold'), fg='orange', bg='gray')
button_equals = Button(frame_central, command=resultado, text="=", width=4, height=2, font=('Arial', 20, 'bold'), fg='white', bg='orange')

button_1 = Button(frame_central, command=lambda: botao_numero(1), text="1", width=4, height=2, font=('Arial', 20, 'bold'), fg='orange', bg='gray')
button_2 = Button(frame_central, command=lambda: botao_numero(2), text="2", width=4, height=2, font=('Arial', 20, 'bold'), fg='orange', bg='gray')
button_3 = Button(frame_central, command=lambda: botao_numero(3), text="3", width=4, height=2, font=('Arial', 20, 'bold'), fg='orange', bg='gray')
button_4 = Button(frame_central, command=lambda: botao_numero(4), text="4", width=4, height=2, font=('Arial', 20, 'bold'), fg='orange', bg='gray')
button_5 = Button(frame_central, command=lambda: botao_numero(5), text="5", width=4, height=2, font=('Arial', 20, 'bold'), fg='orange', bg='gray')
button_6 = Button(frame_central, command=lambda: botao_numero(6), text="6", width=4, height=2, font=('Arial', 20, 'bold'), fg='orange', bg='gray')
button_7 = Button(frame_central, command=lambda: botao_numero(7), text="7", width=4, height=2, font=('Arial', 20, 'bold'), fg='orange', bg='gray')
button_8 = Button(frame_central, command=lambda: botao_numero(8), text="8", width=4, height=2, font=('Arial', 20, 'bold'), fg='orange', bg='gray')
button_9 = Button(frame_central, command=lambda: botao_numero(9), text="9", width=4, height=2, font=('Arial', 20, 'bold'), fg='orange', bg='gray')

button_sum = Button(frame_central, command=lambda: operacao('+'), text="+", width=4, height=2, font=('Arial', 20, 'bold'), fg='orange', bg='gray')
button_minus = Button(frame_central, command=lambda: operacao('-'), text="-", width=4, height=2, font=('Arial', 20, 'bold'), fg='orange', bg='gray')
button_times = Button(frame_central, command=lambda: operacao('*'), text="*", width=4, height=2, font=('Arial', 20, 'bold'), fg='orange', bg='gray')
button_divided = Button(frame_central, command=lambda: operacao('/'), text="/", width=4, height=2, font=('Arial', 20, 'bold'), fg='orange', bg='gray')
button_clear_all = Button(frame_central, command=limpar, text="AC", width=4, height=2, font=('Arial', 20, 'bold'), fg='orange', bg='gray')

button_eval = Button(frame_central, command=lambda: operacao('**'), text="**", width=4, height=2, font=('Arial', 20, 'bold'), fg='orange', bg='gray')
button_r_parentheses = Button(frame_central, command=lambda: operacao('('), text="(", width=4, height=2, font=('Arial', 20, 'bold'), fg='orange', bg='gray')
button_l_parentheses = Button(frame_central, command=lambda: operacao(')'), text=")", width=4, height=2, font=('Arial', 20, 'bold'), fg='orange', bg='gray')
button_0.grid(row=5,column=2)
button_dot.grid(row=5,column=1)
button_equals.grid(row=5,column=3)

button_1.grid(row=4,column=1)
button_2.grid(row=4,column=2)
button_3.grid(row=4,column=3)

button_sum.grid(row=5,column=4)
button_minus.grid(row=4,column=4)
button_times.grid(row=3,column=4)

button_divided.grid(row=2,column=4)
button_4.grid(row=3,column=1)
button_5.grid(row=3,column=2)
button_6.grid(row=3,column=3)
button_7.grid(row=2,column=1)
button_8.grid(row=2,column=2)
button_9.grid(row=2,column=3)

button_eval.grid(row=1,column=2)
button_r_parentheses.grid(row=1,column=3)
button_l_parentheses.grid(row=1,column=4)

button_clear_all.grid(row=1,column=1)

tela_calculadora.mainloop()