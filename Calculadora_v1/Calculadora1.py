from tkinter import *

P_num = None
operacao = None

janela = Tk()
janela.title("Calculadora")
janela.iconbitmap("IconeCalculadora.ico")
janela.resizable(False, False)
numNaTela = Entry(janela)
numNaTela.grid(columnspan=5, row=0, padx=5, pady=5)


def button_click(number):
    atual = numNaTela.get()
    numNaTela.delete(0, END)
    numNaTela.insert(0, str(atual) + str(number))


def button_C():
    numNaTela.delete(0, END)


def button_soma():
    global P_num
    global operacao
    operacao = "soma"
    primeiroNumero = numNaTela.get()
    if primeiroNumero.isnumeric():
        P_num = float(primeiroNumero)
        numNaTela.delete(0, END)
    else:
        numNaTela.delete(0, 'end')
        numNaTela.insert(0, 'erro')


def button_igual():
    segundoNumero = numNaTela.get()
    numNaTela.delete(0, END)
    if operacao == "soma":
        numNaTela.insert(0, P_num + float(segundoNumero))

    if operacao == "subtracao":
        numNaTela.insert(0, P_num - float(segundoNumero))

    if operacao == "divisao":
        numNaTela.insert(0, P_num / float(segundoNumero))

    if operacao == "multiplicacao":
        numNaTela.insert(0, P_num * float(segundoNumero))


def button_subtracao():
    global P_num
    global operacao
    operacao = "subtracao"
    primeiroNumero = numNaTela.get()
    if primeiroNumero.isnumeric():
        P_num = float(primeiroNumero)
        numNaTela.delete(0, END)
    else:
        numNaTela.delete(0, 'end')
        numNaTela.insert(0, 'erro')


def button_multiplicacao():
    global P_num
    global operacao
    operacao = "multiplicacao"
    primeiroNumero = numNaTela.get()
    if primeiroNumero.isnumeric():
        P_num = float(primeiroNumero)
        numNaTela.delete(0, END)
    else:
        numNaTela.delete(0, 'end')
        numNaTela.insert(0, 'erro')


def button_divisao():
    global P_num
    global operacao
    operacao = "divisao"
    primeiroNumero = numNaTela.get()
    if primeiroNumero.isnumeric():
        P_num = float(primeiroNumero)
        numNaTela.delete(0, END)
    else:
        numNaTela.delete(0, 'end')
        numNaTela.insert(0, 'erro')


botao = Button(janela, text='1', command=lambda: button_click(1), font="lucida 10 bold")
botao.grid(column=1, row=1, padx=5, pady=5)

botao2 = Button(janela, text='2', command=lambda: button_click(2), font="lucida 10 bold")
botao2.grid(column=2, row=1, padx=5, pady=5)

botao3 = Button(janela, text='3', command=lambda: button_click(3), font="lucida 10 bold")
botao3.grid(column=3, row=1, padx=5, pady=5)

botao4 = Button(janela, text='4', command=lambda: button_click(4), font="lucida 10 bold")
botao4.grid(column=1, row=2, padx=5, pady=5)

botao5 = Button(janela, text='5', command=lambda: button_click(5), font="lucida 10 bold")
botao5.grid(column=2, row=2, padx=5, pady=5)

botao6 = Button(janela, text='6', command=lambda: button_click(6), font="lucida 10 bold")
botao6.grid(column=3, row=2, padx=5, pady=5)

botao7 = Button(janela, text='7', command=lambda: button_click(7), font="lucida 10 bold")
botao7.grid(column=1, row=3, padx=5, pady=5)

botao8 = Button(janela, text='8', command=lambda: button_click(8), font="lucida 10 bold")
botao8.grid(column=2, row=3, padx=5, pady=5)

botao9 = Button(janela, text='9', command=lambda: button_click(9), font="lucida 10 bold")
botao9.grid(column=3, row=3, padx=5, pady=5)

botao0 = Button(janela, text='0', command=lambda: button_click(0), font="lucida 10 bold")
botao0.grid(column=2, row=4, padx=5, pady=5)

vezes = Button(janela, text='x', command=button_multiplicacao, font="lucida 10 bold")
vezes.grid(column=4, row=1, padx=5, pady=5)

divisao = Button(janela, text='/', command=button_divisao, font="lucida 10 bold")
divisao.grid(column=4, row=2, padx=5, pady=5)

soma = Button(janela, text='+', command=button_soma, font="lucida 10 bold")
soma.grid(column=4, row=3, padx=5, pady=5)

subtracao = Button(janela, text='-', command=button_subtracao, font="lucida 10 bold")
subtracao.grid(column=4, row=4, padx=5, pady=5)

igual = Button(janela, text='=', command=button_igual, font="lucida 10 bold")
igual.grid(column=3, row=4, padx=5, pady=5)

apagar = Button(janela, text='C', command=button_C, font="lucida 10 bold")
apagar.grid(column=1, row=4, padx=5, pady=5)

janela.mainloop()
