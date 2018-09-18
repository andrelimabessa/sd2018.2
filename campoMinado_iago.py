from random import randint
import replit

def criarTabuleiro(numLinhas, numColunas):
  tabuleiro = [];
  for i in range(numLinhas):
    linha = [];
    for j in range(numColunas):
      linha.append(randint(0,1));
    tabuleiro.append(linha);
  
  return tabuleiro

def exibirCampoMinado(campoMinado):
  for i in range(len(campoMinado)):
    print(campoMinado[i])
    
def getTabuleiroCoberto(campoMinado):
  tabuleiroCoberto = [];
  for i in range(len(campoMinado)):
    linhaCoberta = []
    for j in range(len(campoMinado[i])):
      linhaCoberta.append('X')
    tabuleiroCoberto.append(linhaCoberta)

  return tabuleiroCoberto

def exibirTabuleiroCoberto(tabuleiroCoberto):
  posicao = " "
  for i in range(len(tabuleiroCoberto)):
    linha = "|"
    posicao += "   " + str(i)  
    for j in range(len(tabuleiroCoberto[i])):
      #  
      linha += " " + tabuleiroCoberto[i][j] + " |"
    print(i, linha)
  print(posicao)

def verificarJogada(valor):
  if(valor == 1):
    return True
  else:
    return False

def valorContidoNaPosicaoEscolhida(campoMinado, linha, coluna):
  for i in range(len(campoMinado)):
    if(i == linha):
      linha = campoMinado[i]
      for j in range(len(linha)):
        if j == coluna:
          valor = linha[j]
          return valor

def processarJogadas(campoMinado, tabuleiro, qtdBombas, totalPosicoes):
  jogadas = 0
  isBomba = False
  tabuleiroAtualizado = tabuleiro
  while (isBomba != True):
    if(jogadas + qtdBombas == totalPosicoes):
      print("----------VOCÊ--VENCEU---------")
      return True
    else:
      print("\n\nFaça uma jogada escolhendo linha e coluna")
      linha = int(input("Escolha a linha"))
      coluna= int(input("Escolha a coluna"))
      isBomba = verificarJogada(valorContidoNaPosicaoEscolhida(campoMinado, linha, coluna))
      replit.clear()
      tabuleiroAtualizado = atualizarTabuleiro(campoMinado, tabuleiroAtualizado, linha, coluna, isBomba)
      exibirTabuleiroCoberto(tabuleiroAtualizado);
      #exibirCampoMinado(campoMinado)
      jogadas += 1
  if(isBomba == True):
    print("-------Game--Over------")
    return True

def atualizarTabuleiro(campoMinado, tabuleiro, linhaEscolhida, colunaEscolhida, existBomba):
  tabuleiroCoberto = tabuleiro;
  qtdBombasVizinhas = getNumeroBombaVizinhas(campoMinado, linhaEscolhida, colunaEscolhida);
  for i in range(len(tabuleiroCoberto)):
    for j in range(len(tabuleiroCoberto[i])):
      if(i == linhaEscolhida and j == colunaEscolhida):
        if(existBomba == True):
          tabuleiroCoberto[i][j] = ('B')
        elif(qtdBombasVizinhas == 0):
          tabuleiroCoberto[i][j] = (' ')
        else:
          tabuleiroCoberto[i][j] = str(qtdBombasVizinhas)

  return tabuleiroCoberto

def getNumeroBombaVizinhas(campoMinado, linha, coluna):
  qtdBombas = 0;
  for i in range(len(campoMinado)):
    tam = len(campoMinado) - 1
    for j in range(len(campoMinado[i])):
      if(i == linha and j == coluna):
        if(coluna < tam and linha >= 0 and campoMinado[i][j+1] == 1):
          qtdBombas += 1
        if(coluna < tam and linha < tam and campoMinado[i+1][j+1] == 1):
          qtdBombas += 1
        if(coluna < tam and linha > 0 and campoMinado[i-1][j+1] == 1):
          qtdBombas += 1
        if(coluna > 0 and campoMinado[i][j-1] == 1):
          qtdBombas += 1
        if(coluna > 0 and (linha - 1 >=0) and campoMinado[i - 1][j-1] == 1):
          qtdBombas += 1
        if(coluna > 0 and linha + 1 <= tam and campoMinado[i + 1][j-1] == 1):
          qtdBombas += 1
        if(linha > 0 and campoMinado[i - 1][j] == 1):
          qtdBombas += 1
        if(linha < tam and campoMinado[i + 1][j] == 1):
          qtdBombas += 1

  return qtdBombas

def getNumeroBombas(campoMinado):
  numeroDeBombas = 0
  for i in range(len(campoMinado)):
    for j in range(len(campoMinado[i])):
      if(campoMinado[i][j] == 1):
        numeroDeBombas = numeroDeBombas + 1
  return numeroDeBombas

def getTotalPosicoes(campoMinado):
  totalPosicoes = len(campoMinado) * len(campoMinado)
  return totalPosicoes

#recebe o tamanho do tabuleiro
def inicializar(tamanhoTabuleiro):
  campoMinado = criarTabuleiro(tamanhoTabuleiro, tamanhoTabuleiro);
  exibirTabuleiroCoberto(getTabuleiroCoberto(campoMinado));
  processarJogadas(campoMinado, getTabuleiroCoberto(campoMinado), getNumeroBombas(campoMinado), getTotalPosicoes(campoMinado));

  return True

inicializar(5)







