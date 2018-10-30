import sys
from udp_cliente import criar_novo_jogo
from udp_cliente import jogada

TABULEIRO = "tabuleiro"
INSTANCIA = "instancia"
VITORIA = "Parabéns você venceu"
GAME_OVER = "GAME_OVER"
TOTAL_JOGADAS = "Total de Jogadas"
""" 
    1. Menu para iniciar o jogo
    2. Menu declara jogada
    3. Regra pra vitória
    
    4. Salvar jogadas
    5. Continuar jogo 
 """

def menu_inicial():
    print("---------------------------------------")
    print("------------ Campo Minado -------------")
    print("---------------------------------------")
    print("\n")
    print(" Selecione uma opção")
    print("1. Criar novo jogo")
    print("9. Sair do Jogo")

def inicializar_tabuleiro(linha, coluna):
    return [[str('X') for x in range(coluna)] for j in range(linha)]

def total_bombas(linha, coluna):
    return int((linha*coluna)/3)

def calcular_total_jogadas(linha, coluna):
    return (linha*coluna) - total_bombas(linha, coluna)

def imprimir_tabuleiro(contexto):

    tabuleiro = contexto[TABULEIRO]

    for posicao in tabuleiro:
        print(str(posicao))

def iniciar_novo_jogo(contexto):

    criar_novo_jogo(4,4)
    
    contexto[TABULEIRO] = inicializar_tabuleiro(4,4)
    contexto[TOTAL_JOGADAS] = calcular_total_jogadas(4,4)
    imprimir_tabuleiro(contexto)

    return efetuar_nova_jogada(contexto)

def efetuar_nova_jogada(contexto):

    jogadas_restantes = contexto[TOTAL_JOGADAS]

    while jogadas_restantes > 0:
        linha = int(input("Defina uma linha: "))
        coluna = int(input("Defina uma coluna: "))
        if jogada(linha,coluna) == GAME_OVER:
            return GAME_OVER
        imprimir_tabuleiro(contexto)
        jogadas_restantes -= 1
    
    return VITORIA

def sair(contexto):
    sys.exit(0)

if __name__ == "__main__":

    switcher = {
        1: iniciar_novo_jogo,
        9: sair,
    }

    contexto = {TABULEIRO: '',
                 TOTAL_JOGADAS: '' }
    
    while True:
        menu_inicial()
        opcao = int(input("Opção escolhida: "))

        func = switcher.get(opcao)
        print(func(contexto))

