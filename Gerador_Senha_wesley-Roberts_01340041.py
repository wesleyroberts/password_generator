import PySimpleGUI as sg
import random
import string
import os 
from playsound import playsound 

# Gera senha
def GerarSenha(tam_senha,letra_min,letra_max,simbolo,numeros):
    lista= []
    if letra_min:
        letraMin = string.ascii_lowercase
        for letra in letraMin: 
            lista.append(letra)

    if letra_max:
        letraMax = string.ascii_uppercase
        for letra in letraMax: 
         lista.append(letra) 

    if simbolo:
        syb = string.punctuation
        for caract in syb: 
         lista.append(caract)        

    if numeros:
        numero = string.digits
        for num in numero: 
         lista.append(num)

    # Realização da mistura da senha
    senha=random.choices(lista,k=int(valores['tam_senha']))
    senha= ''.join(senha)
    #return senha
    return senha

# Layout do programa
sg.theme('Black')
#playsound('01 - RITA.mp3',block=False)
layout = [
            [sg.Text('Site/Software',size=(10, 1)), sg.Input(key='Site', size=(20, 1))],
            [sg.Text('E-mail/Usuário', size=(10, 1)), sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(range(30)), key='tam_senha', default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha')]
        ] 

janela = sg.Window('Gerador de Senha', layout)
while (True):
     
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED:
        break            
    if evento=='Gerar Senha':
        tam_senha = valores['tam_senha']
        senha=GerarSenha(tam_senha,True,True,True,True)
        print(senha)
     