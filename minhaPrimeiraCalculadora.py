from tkinter import *


numero1 = ''
numero2 = ''
adicao = FALSE
subtracao = FALSE
multiplicacao = FALSE
divisao = FALSE


interface = Tk()
interface.geometry("408x355")
interface.title("Eu não nasci pra trabalhar como CLT")
interface.maxsize(408, 355)
interface.minsize(408, 355)

interface.configure(background='#282828')

e = Entry(interface, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF',
          bg='#282828', font=('futura', 25, 'bold'), justify=RIGHT)
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)
def botao_click(num):
    e.insert(END, num)

def botao_adiciona():
    global numero1
    global adicao
    adicao = TRUE
    numero1 = e.get()
    e.delete(0, END)

def botao_subrai():
    global numero1
    global subtracao
    subtracao = TRUE
    numero1 = e.get()
    e.delete(0, END)

def botao_multiplica():
    global numero1
    global multiplicacao
    multiplicacao = TRUE
    numero1 = e.get()
    e.delete(0, END)

def botao_divide():
    global numero1
    global divisao
    divisao = TRUE
    numero1 = e.get()
    e.delete(0, END)

def botao_igual():
    global subtracao
    global divisao
    global multiplicacao
    global adicao
    numero2 = e.get()
    e.delete(0, END)
    if adicao == TRUE:
        e.insert(0, int(numero1) + int(numero2))
        adicao = FALSE
    if multiplicacao == TRUE:
        e.insert(0, int(numero1) * int(numero2))
        multiplicacao = FALSE
    if subtracao == TRUE:
        e.insert(0, int(numero1) - int(numero2))
        subtracao = FALSE
    if divisao == TRUE:
        e.insert(0, int(numero1) // int(numero2))
        divisao = FALSE


def botao_limpa():
    e.delete(0, END)

def botao_num(num, row, column):
    botao = Button(interface,
                   text=num,
                   padx=40,
                   pady=20,
                   command=lambda: botao_click(num),
                   fg='#FFFFFF',
                   activebackground='#1D1D1D',
                   activeforeground='#FFFFFF',
                   bg='#282828',
                   relief=FLAT,
                   font=('futura', 12, 'bold'))
    botao.grid(row=row, column=column)

def botao_operador(op, command, row, column):
    operador = Button(interface,
                      text=op,
                      padx=40,
                      pady=20,
                      command=command,
                      fg='#F37C2D',
                      activebackground='#1D1D1D',
                      activeforeground='#FFFFFF',
                      bg='#282828',
                      relief=FLAT,
                      font=('futura', 12, 'bold'))
    operador.grid(row=row, column=column)


botao_operador('÷', botao_divide, 0, 4)

botao_num(1, 1, 1)
botao_num(2, 1, 2)
botao_num(3, 1, 3)
botao_operador('×', botao_multiplica, 1, 4)

botao_num(4, 2, 1)
botao_num(5, 2, 2)
botao_num(6, 2, 3)
botao_operador(' -', botao_subrai, 2, 4)

botao_num(7, 3, 1)
botao_num(8, 3, 2)
botao_num(9, 3, 3)
botao_operador('+', botao_adiciona, 3, 4)

zero = Button(interface,
              text='0',
              padx=91,
              pady=20,
              command=lambda: botao_click(0),
              fg='#FFFFFF',
              activebackground='#1D1D1D',
              activeforeground='#FFFFFF',
              bg='#282828',
              relief=FLAT,
              font=('futura', 12, 'bold'))
zero.grid(row=4, column=1, columnspan=2)
botao_operador('C', botao_limpa, 4, 4)
botao_operador('=', botao_igual, 4, 3)

interface.mainloop()
