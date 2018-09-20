from campominado import *
from cmutil import *
from mensagemJogo import *

import pickle

from os import system, name 
from time import sleep 

campo = CampoMinado()

def clear(): 
  
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear') 


continua = True

def salvaEsaiDoJogo(campo):
    mensagensJogo.salvandoJogo()
    codigo = input("digite um codigo para o jogo a ser salvado: ")
    with open(codigo, 'wb') as handle:
        pickle.dump(campo, handle, protocol=pickle.HIGHEST_PROTOCOL)

    
    campo.salvarJogoEmArquivo()
    util.continua = False

def exibeTelaGameOver():
    
    print("GAME OVER!")

def definirTamCampoMinado(campo):
    nivel = input("Escolha o nível do jogo:\n1.Fácil\n2.Intermediário\n3.Difícil\n")
    campo.setaTamanhoCampoMinado(nivel)

def jogo(flag):
    if(flag == '2'):
        try:
            clear()
            codigo = input("digite codigo do jogo salvo: ")
            with open(codigo, 'rb') as handle:
                campo = pickle.load(handle)
        except FileNotFoundError:
            clear()
            print("Não há jogo salvo para esse código")
            menuJogo()
    else:
        clear()
        campo = CampoMinado()
        definirTamCampoMinado(campo)
        clear()
        campo.inicializaMatriz()
            

    while(util.continua and campo.totalJogadas > 0):
        mensagensJogo.exibeQtdJogadasRestantes(campo.totalJogadas)
        escolha = util.menuEscolhaContinuaOuSalva()
        clear()
        if(escolha == 'c'):
            campo.printaTabelaExibicao()
            util.continua = campo.escolheArea()
            clear()
            campo.printaTabelaExibicao()
            campo.totalJogadas-=1
        elif(escolha == 's'):
            salvaEsaiDoJogo(campo)
    
    if(util.continua == False):
        exibeTelaGameOver()
    
    util.continua = False
    
    if(campo.totalJogadas == 0):
        mensagensJogo.exibeMensagemVitoria()
        

def menuJogo():
    menu = {}
    menu['1']="Novo Jogo" 
    menu['2']="Carregar Jogo"
    menu['3']="Sobre"
    menu['4']="Exit"

    while(util.continua):
        options=menu.keys()
        
        for entry in options: 
            print(entry, menu[entry])
        selection= input("Selecione uma opção: ") 
        if selection =='1':
            jogo("1") 
        elif selection == '2':
            jogo("2")
        elif selection == '3':
            print("\n\n\nOpção não implementada ainda\n") 
        elif selection == '4':
            break
        else:
            print("Opção não conhecida!")

###### COMEÇO DO JOGO ##########

util = Cmutil()
mensagensJogo = MensagemJogo()
menuJogo()




