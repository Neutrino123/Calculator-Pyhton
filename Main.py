import Functions
import math
from tkinter import *

def buttonPress(x):
    global equation_text
    equation_text = equation_text + str(x)
    equation_label.set(equation_text)

def egal():

    total = str(eval(equation_text))
    equation_label.set(total)

def clear():

    global equation_text
    equation_label.set("")
    equation_text = ""

window = Tk()
window.title("Calculator")
window.geometry("600x600")

equation_text = ""
equation_label = StringVar()

label = Label(window, textvariable=equation_label, fg='white', font=30, bg="black", width=36, height=5, text='white')
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text='1', width=8, height=4, font=35, command=lambda: buttonPress(1))
button1.grid(row=0, column=0)
button2 = Button(frame, text='2', width=8, height=4, font=35, command=lambda: buttonPress(2))
button2.grid(row=0, column=1)
button3 = Button(frame, text='3', width=8, height=4, font=35, command=lambda: buttonPress(3))
button3.grid(row=0, column=2)
buttonplus = Button(frame, text='+', width=8, height=4, font=35, command=lambda: buttonPress('+'))
buttonplus.grid(row=0, column=3)

button4 = Button(frame, text='4', width=8, height=4, font=35, command=lambda: buttonPress(4))
button4.grid(row=1, column=0)
button5 = Button(frame, text='5', width=8, height=4, font=35, command=lambda: buttonPress(5))
button5.grid(row=1, column=1)
button6 = Button(frame, text='6', width=8, height=4, font=35, command=lambda: buttonPress(6))
button6.grid(row=1, column=2)
buttonminus = Button(frame, text='-', width=8, height=4, font=35, command=lambda: buttonPress('-'))
buttonminus.grid(row=1, column=3)

button7 = Button(frame, text='7', width=8, height=4, font=35, command=lambda: buttonPress(7))
button7.grid(row=2, column=0)
button8 = Button(frame, text='8', width=8, height=4, font=35, command=lambda: buttonPress(8))
button8.grid(row=2, column=1)
button9 = Button(frame, text='9', width=8, height=4, font=35, command=lambda: buttonPress(9))
button9.grid(row=2, column=2)
buttonori = Button(frame, text='*', width=8, height=4, font=35, command=lambda: buttonPress('*'))
buttonori.grid(row=2, column=3)

buttonegal = Button(frame, text='=', width=8, height=4, font=35, command=lambda: egal())
buttonegal.grid(row=3, column=0)

buttonvirgula = Button(frame, text=',', width=8, height=4, font=35, command=lambda: buttonPress('.'))
buttonvirgula.grid(row=3, column=1)


buttonimparte = Button(frame, text='/', width=8, height=4, font=35, command=lambda: buttonPress('/'))
buttonimparte.grid(row=3, column=2)

buttonridica = Button(frame, text='^', width=8, height=4, font=35, command=lambda: buttonPress('**'))
buttonridica.grid(row=3, column=3)
clear1 = Button(frame, text='clear', width=8, height=4, font=35, command=lambda: clear())
clear1.grid(row=4, column=2)



window.mainloop()