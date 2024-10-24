def botao_0():
    label_result.config(text=0)

def botao_1():
    label_result.config(text=1)

def botao_2():
    label_result.config(text=2)

def botao_3():
    label_result.config(text=3)

def botao_4():
    label_result.config(text=4)
    
def botao_5():
    label_result.config(text=5)

def botao_6():
    label_result.config(text=6)

def botao_7():
    label_result.config(text=7)

def botao_8():
    label_result.config(text=8)

def botao_9():
    label_result.config(text=3)

def dot():
    label_result.config(text='.')

def sum():
    label_result.config(text='+')
    
def minus():
    label_result.config(text='-')

def divided():
    label_result.config(text='/')
    
def sum():
    label_result.config(text='+')
    
def result():
    global result

from tkinter import *
import tkinter as tk

tela_calculadora = Tk()

tela_calculadora.geometry("712x1284") #tamanho da tela
tela_calculadora.config(bg="black")

frame_central = Frame(tela_calculadora, bg='black') #tamanho do grupo (frame)
frame_central.place(relx=0.5, rely=0.5, anchor=CENTER)

photo_clear = PhotoImage(file='calculadora/clear.png')

label_result = Label(frame_central, text='result')
label_result.config(width=10)
label_result.config(font=('Arial',46))

button_0 = Button(frame_central,
                 command=botao_0,
                 text="0",
                 width=4,
                 height=2,
                 relief='raised',
                 font=('Arial',20,'bold'),
                 fg='orange',
                 bg='gray')
button_1 = Button(frame_central, 
                 text="1",
                 width=4,
                 height=2,
                 relief='raised',
                 font=('Arial',20,'bold'),
                 fg='orange',
                 bg='gray')
button_2 = Button(frame_central, 
                 text="2",
                 width=4,
                 height=2,
                 relief='raised',
                 font=('Arial',20,'bold'),
                 fg='orange',
                 bg='gray')
button_3 = Button(frame_central, 
                 text="3",
                 width=4,
                 height=2,
                 relief='raised',
                 font=('Arial',20,'bold'),
                 fg='orange',
                 bg='gray')
button_4 = Button(frame_central, 
                 text="4",
                 width=4,
                 height=2,
                 relief='raised',
                 font=('Arial',20,'bold'),
                 fg='orange',
                 bg='gray')
button_5 = Button(frame_central, 
                 text="5",
                 width=4,
                 height=2,
                 relief='raised',
                 font=('Arial',20,'bold'),
                 fg='orange',
                 bg='gray')
button_6 = Button(frame_central, 
                 text="6",
                 width=4,
                 height=2,
                 relief='raised',
                 font=('Arial',20,'bold'),
                 fg='orange',
                 bg='gray')
button_7 = Button(frame_central, 
                 text="7",
                 width=4,
                 height=2,
                 relief='raised',
                 font=('Arial',20,'bold'),
                 fg='orange',
                 bg='gray')
button_8 = Button(frame_central, 
                 text="8",
                 width=4,
                 height=2,
                 relief='raised',
                 font=('Arial',20,'bold'),
                 fg='orange',
                 bg='gray')
button_9 = Button(frame_central, 
                 text="9",
                 width=4,
                 height=2,
                 relief='raised',
                 font=('Arial',20,'bold'),
                 fg='orange',
                 bg='gray')

button_dot = Button(frame_central, 
                 text=".",
                 width=4,
                 height=2,
                 relief='raised',
                 font=('Arial',20,'bold'),
                 fg='orange',
                 bg='gray')
button_equals = Button(frame_central, 
                 text="=",
                 width=4,
                 height=2,
                 font=('Arial',20,'bold'),
                 relief='raised',
                 fg='white',
                 bg='orange')

button_sum = Button(frame_central, 
                 text="+",
                 width=4,
                 height=2,
                 font=('Arial',20,'bold'),
                 relief='raised',
                 fg='orange',
                 bg='gray')

button_minus = Button(frame_central, 
                 text="-",
                 width=4,
                 height=2,
                 font=('Arial',20,'bold'),
                 relief='raised',
                 fg='orange',
                 bg='gray')
button_times = Button(frame_central, 
                 text="*",
                 width=4,
                 height=2,
                 font=('Arial',20,'bold'),
                 relief='raised',
                 fg='orange',
                 bg='gray')
button_divided = Button(frame_central, 
                 text="/",
                 width=4,
                 height=2,
                 font=('Arial',20,'bold'),
                 relief='raised',
                 fg='orange',
                 bg='gray')
            
button_percent = Button(frame_central, 
                 text="%",
                 width=4,
                 height=2,
                 font=('Arial',20,'bold'),
                 relief='raised',
                 fg='orange',
                 bg='gray')
button_clear_all = Button(frame_central, 
                 text="AC",
                 width=4,
                 height=2,
                 font=('Arial',20,'bold'),
                 relief='raised',
                 fg='orange',
                 bg='gray')        
button_clear = Button(frame_central, 
                 text="C",
                 width=4,
                 height=2,
                 font=('Arial',20,'bold'),
                 relief='raised',
                 fg='orange',
                 bg='gray')

button_power = Button(frame_central, 
                 text="^",
                 width=4,
                 height=2,
                 font=('Arial',20,'bold'),
                 relief='raised',
                 fg='orange',
                 bg='gray')
            
label_result.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
button_0.grid(row=5,column=2,padx=10)
button_dot.grid(row=5,column=1,padx=10)
button_equals.grid(row=5,column=3,padx=10)

button_1.grid(row=4,column=1,padx=10)
button_2.grid(row=4,column=2,padx=10)
button_3.grid(row=4,column=3,padx=10)

button_sum.grid(row=5,column=4,padx=10)
button_minus.grid(row=4,column=4,padx=10)
button_times.grid(row=3,column=4,padx=10)

button_divided.grid(row=2,column=4,padx=10)
button_4.grid(row=3,column=1,padx=10)
button_5.grid(row=3,column=2,padx=10)

button_6.grid(row=3,column=3,padx=10)
button_7.grid(row=2,column=1,padx=10)
button_8.grid(row=2,column=2,padx=10)

button_9.grid(row=2,column=3,padx=10)
button_percent.grid(row=1,column=3,padx=10)
button_clear_all.grid(row=1,column=1,padx=10)

button_power.grid(row=1,column=4,padx=10)

button_clear.grid(row=1,column=2,padx=10)


tela_calculadora.mainloop()

