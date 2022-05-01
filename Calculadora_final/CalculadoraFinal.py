# Importando biblioteca
from tkinter import *

# Definindo bases
operacao = "inicio"
P_num = None

# Criando a janela
janela = Tk()
janela.title("Calculadora")
janela.resizable(False, False)
janela['bg'] = 'white'
janela.iconbitmap('IconeCalculadora.ico')

# Tela onde aparecerão os números
numNaTela = Entry(janela, font='arial 12 bold', bd=5)
numNaTela.grid(columnspan=5, row=0, ipadx=13, ipady=10)


# Definindo funções de botões
def button_click(number):
    if numNaTela.get() == 'erro':
        numNaTela.delete(0, 'end')
    atual = numNaTela.get()
    numNaTela.delete(0, END)
    numNaTela.insert(0, str(atual) + str(number))


def button_C():
    global P_num
    global operacao
    numNaTela.delete(0, END)
    P_num = None
    operacao = 'inicio'


def button_igual():
    if P_num is None:
        numNaTela.delete(0, 'end')
        numNaTela.insert(0, 'erro')
    segundoNumero = numNaTela.get()
    segundoNumero = segundoNumero.replace(',', '.')
    numNaTela.delete(0, END)

    if operacao == 'inicio' or segundoNumero.replace('.', '').isnumeric() is False:
        numNaTela.insert(0, "erro")

    if operacao == "soma" and segundoNumero.replace('.', '').isnumeric():
        if '.0' in str(P_num + float(segundoNumero)) and str(P_num + float(segundoNumero)).index('.') + 2 == len(str(P_num + float(segundoNumero))):
            numNaTela.insert(0, str(P_num + float(segundoNumero)).replace('.0', ''))
        else:
            numNaTela.insert(0, str(P_num + float(segundoNumero)).replace('.', ','))

    if operacao == "subtracao" and segundoNumero.replace('.', '').isnumeric():
        if '.0' in str(P_num - float(segundoNumero)) and str(P_num - float(segundoNumero)).index('.') + 2 == len(str(P_num - float(segundoNumero))):
            numNaTela.insert(0, str(P_num - float(segundoNumero)).replace('.0', ''))
        else:
            numNaTela.insert(0, str(P_num - float(segundoNumero)).replace('.', ','))

    if operacao == "divisao" and segundoNumero.replace('.', '').isnumeric():
        if '.0' in str(P_num / float(segundoNumero)) and str(P_num / float(segundoNumero)).index('.') + 2 == len(str(P_num / float(segundoNumero))):
            numNaTela.insert(0, str(P_num / float(segundoNumero)).replace('.0', ''))
        else:
            numNaTela.insert(0, str(P_num / float(segundoNumero)).replace('.', ','))

    if operacao == "multiplicacao" and segundoNumero.replace('.', '').isnumeric():
        if '.0' in str(P_num * float(segundoNumero)) and str(P_num * float(segundoNumero)).index('.') + 2 == len(str(P_num * float(segundoNumero))):
            numNaTela.insert(0, str(P_num * float(segundoNumero)).replace('.0', ''))
        else:
            numNaTela.insert(0, str(P_num * float(segundoNumero)).replace('.', ','))

    if operacao == "potencia" and segundoNumero.replace('.', '').isnumeric():
        if '.0' in str(P_num * float(segundoNumero)) and str(P_num ** float(segundoNumero)).index('.') + 2 == len(str(P_num ** float(segundoNumero))):
            numNaTela.insert(0, str(P_num ** float(segundoNumero)).replace('.0', ''))
        else:
            numNaTela.insert(0, str(P_num ** float(segundoNumero)).replace('.', ','))

    if operacao == "divisao_int" and segundoNumero.replace('.', '').isnumeric():
        if '.0' in str(P_num * float(segundoNumero)) and str(P_num // float(segundoNumero)).index('.') + 2 == len(str(P_num // float(segundoNumero))):
            numNaTela.insert(0, str(P_num // float(segundoNumero)).replace('.0', ''))
        else:
            numNaTela.insert(0, str(P_num // float(segundoNumero)).replace('.', ','))

    if operacao == "resto" and segundoNumero.replace('.', '').isnumeric():
        if '.0' in str(P_num * float(segundoNumero)) and str(P_num % float(segundoNumero)).index('.') + 2 == len(str(P_num % float(segundoNumero))):
            numNaTela.insert(0, str(P_num % float(segundoNumero)).replace('.0', ''))
        else:
            numNaTela.insert(0, str(P_num % float(segundoNumero)).replace('.', ','))


def pegar_numero():
    global P_num
    global operacao
    primeiroNumero = numNaTela.get()
    primeiroNumero = primeiroNumero.replace(',', '.')

    if primeiroNumero.replace('.', '').isnumeric():
        P_num = float(primeiroNumero)
        numNaTela.delete(0, END)
    else:
        numNaTela.delete(0, 'end')
        numNaTela.insert(0, 'erro')


def potencia():
    global operacao
    operacao = "potencia"
    pegar_numero()


def divisao_int():
    global operacao
    operacao = "divisao_int"
    pegar_numero()


def resto():
    global operacao
    operacao = "resto"
    pegar_numero()


def button_soma():
    global operacao
    operacao = "soma"
    pegar_numero()


def button_subtracao():
    global operacao
    operacao = "subtracao"
    pegar_numero()


def button_multiplicacao():
    global operacao
    operacao = "multiplicacao"
    pegar_numero()


def button_divisao():
    global operacao
    operacao = "divisao"
    pegar_numero()


# Gerando a tela
botao = Button(janela, text='1', command=lambda: button_click(1), font="lucida 10 bold", bg='white', bd=0)
botao.grid(column=1, row=1, ipadx=17, ipady=10)

botao2 = Button(janela, text='2', command=lambda: button_click(2), font="lucida 10 bold", bg='white', bd=0)
botao2.grid(column=2, row=1, ipadx=17, ipady=10)

botao3 = Button(janela, text='3', command=lambda: button_click(3), font="lucida 10 bold", bg='white', bd=0)
botao3.grid(column=3, row=1, ipadx=17, ipady=10)

botao4 = Button(janela, text='4', command=lambda: button_click(4), font="lucida 10 bold", bg='white', bd=0)
botao4.grid(column=1, row=2, ipadx=17, ipady=10)

botao5 = Button(janela, text='5', command=lambda: button_click(5), font="lucida 10 bold", bg='white', bd=0)
botao5.grid(column=2, row=2, ipadx=17, ipady=10)

botao6 = Button(janela, text='6', command=lambda: button_click(6), font="lucida 10 bold", bg='white', bd=0)
botao6.grid(column=3, row=2, ipadx=17, ipady=10)

botao7 = Button(janela, text='7', command=lambda: button_click(7), font="lucida 10 bold", bg='white', bd=0)
botao7.grid(column=1, row=3, ipadx=17, ipady=10)

botao8 = Button(janela, text='8', command=lambda: button_click(8), font="lucida 10 bold", bg='white', bd=0)
botao8.grid(column=2, row=3, ipadx=17, ipady=10)

botao9 = Button(janela, text='9', command=lambda: button_click(9), font="lucida 10 bold", bg='white', bd=0)
botao9.grid(column=3, row=3, ipadx=17, ipady=10)

botao0 = Button(janela, text='0', command=lambda: button_click(0), font="lucida 10 bold", bg='white', bd=0)
botao0.grid(column=2, row=4, ipadx=17, ipady=10)

vezes = Button(janela, text='x', command=button_multiplicacao, font="lucida 10 bold", bg='white', bd=0)
vezes.grid(column=4, row=4, ipadx=15, ipady=10)

divisao = Button(janela, text='/', command=button_divisao, font="lucida 10 bold", bg='white', bd=0)
divisao.grid(column=4, row=3, ipadx=17, ipady=10)

soma = Button(janela, text='+', command=button_soma, font="lucida 10 bold", bg='white', bd=0)
soma.grid(column=4, row=2, ipadx=15, ipady=10)

subtracao = Button(janela, text='-', command=button_subtracao, font="lucida 10 bold", bg='white', bd=0)
subtracao.grid(column=4, row=1, ipadx=17, ipady=10)

igual = Button(janela, text='=', command=button_igual, font="lucida 10 bold", bg='white', bd=0)
igual.grid(column=4, row=5, ipadx=17, ipady=10)

apagar = Button(janela, text='C', command=button_C, font="lucida 10 bold", bg='white', bd=0)
apagar.grid(column=1, row=5, ipadx=17, ipady=10)

ponto = Button(janela, text='.', command=lambda: button_click('.'), font="lucida 10 bold", bg='white', bd=0)
ponto.grid(column=3, row=4, ipadx=17, ipady=10)

divisao_int_botao = Button(janela, text='//', command=divisao_int, font="lucida 10 bold", bg='white', bd=0)
divisao_int_botao.grid(column=3, row=5, ipadx=17, ipady=10)

resto_botao = Button(janela, text='%', command=resto, font="lucida 10 bold", bg='white', bd=0)
resto_botao.grid(column=2, row=5, ipadx=17, ipady=10)

potencia_botao = Button(janela, text='^', command=potencia, font="lucida 10 bold", bg='white', bd=0)
potencia_botao.grid(column=1, row=4, ipadx=17, ipady=10)

# Rodando a tela
janela.mainloop()
