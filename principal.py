from CampoMinado import CampoMinado

def imprimir_menu():
        print("Menu:\n")
        print("1. Iniciar jogo;")
        print("2. Retornar para jogo passado;")
        print("9. Finalizar partida; \n")

        print ("Escolha uma numeração do menu de 1, 2 ou 9, para fazer a acao desejada.")
        escolha = int(input("Numero do menu"))
        print("")
        return escolha

def iniciar_jogo():
        #pergunta a qtd de linhas ecam colunas para o usuario
        lins = int(input("Insira o num de linhas: "))
        cols = int(input("Insira o num de colunas: "))

        return CampoMinado(lins, cols) 

def tratar_jogo_passado():
        pass

def jogada():
        pass

def sair():
        pass


def interface():
        escolha = imprimir_menu()

        map_funcoes = {
                '1':iniciar_jogo,
                '2':tratar_jogo_passado,
                '9':sair
        }
        
        func = map_funcoes.get(escolha)
        func()

def imprimir_Tabuleiro (lins,cols):
    for x in range(lins):
        print (str(lins) + ' ',end='')
        for y in range(cols):
            if [x,y] in [y[0] for y in cols]:
                for y in cols:
                    if y[0] == [x,y]:
                        print ('(' + str(y[1]) + ') ',end='')
                        break
            else:
                print ('(X) ',end='')
        print()
        lins += 1
