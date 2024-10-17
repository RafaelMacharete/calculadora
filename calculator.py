from tkinter import *
import tkinter as tk

tela_calculadora = Tk()
#estilizando a tela da calculadora
tela_calculadora.geometry("924x924")
tela_calculadora.config(bg="black")

button0 = Button(tela_calculadora, 
                 text="0",
                 width=6,
                 height=3,
                 relief='raised',
                 font=('Arial',9,'bold'),
                 fg='orange',
                 bg='gray')
button1 = Button(tela_calculadora, 
                 text="1",
                 width=6,
                 height=3,
                 relief='raised',
                 font=('Arial',9,'bold'),
                 fg='orange',
                 bg='gray')
button2 = Button(tela_calculadora, 
                 text="2",
                 width=6,
                 height=3,
                 relief='raised',
                 font=('Arial',9,'bold'),
                 fg='orange',
                 bg='gray')
button3 = Button(tela_calculadora, 
                 text="3",
                 width=6,
                 height=3,
                 relief='raised',
                 font=('Arial',9,'bold'),
                 fg='orange',
                 bg='gray')
button4 = Button(tela_calculadora, 
                 text="4",
                 width=6,
                 height=3,
                 relief='raised',
                 font=('Arial',9,'bold'),
                 fg='orange',
                 bg='gray')
button5 = Button(tela_calculadora, 
                 text="5",
                 width=6,
                 height=3,
                 relief='raised',
                 font=('Arial',9,'bold'),
                 fg='orange',
                 bg='gray')
button6 = Button(tela_calculadora, 
                 text="6",
                 width=6,
                 height=3,
                 relief='raised',
                 font=('Arial',9,'bold'),
                 fg='orange',
                 bg='gray')
button7 = Button(tela_calculadora, 
                 text="7",
                 width=6,
                 height=3,
                 relief='raised',
                 font=('Arial',9,'bold'),
                 fg='orange',
                 bg='gray')
button8 = Button(tela_calculadora, 
                 text="8",
                 width=6,
                 height=3,
                 relief='raised',
                 font=('Arial',9,'bold'),
                 fg='orange',
                 bg='gray')
button9 = Button(tela_calculadora, 
                 text="9",
                 width=6,
                 height=3,
                 relief='raised',
                 font=('Arial',9,'bold'),
                 fg='orange',
                 bg='gray')

button_dot = Button(tela_calculadora, 
                 text=".",
                 width=6,
                 height=3,
                 relief='raised',
                 font=('Arial',9,'bold'),
                 fg='orange',
                 bg='gray')
button_equals = Button(tela_calculadora, 
                 text="=",
                 width=12,
                 height=3,
                 font=('Arial',9,'bold'),
                 relief='raised',
                 fg='orange',
                 bg='gray')

            

button0.grid(row=5,column=1,padx=10)
button_dot.grid(row=5,column=2,padx=10)
button_equals.grid(row=5,column=3,padx=10)
button1.grid(row=4,column=1,padx=10)
button2.grid(row=4,column=2,padx=10)
button3.grid(row=4,column=3,padx=10)
button4.grid(row=3,column=1,padx=10)
button5.grid(row=3,column=2,padx=10)
button6.grid(row=3,column=3,padx=10)
button7.grid(row=2,column=1,padx=10)
button8.grid(row=2,column=2,padx=10)
button9.grid(row=2,column=3,padx=10)


tela_calculadora.mainloop()

