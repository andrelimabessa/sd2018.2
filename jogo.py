import random
import replit
from colorama import init
from colorama import Fore, Back, Style
init()


def criando_campo_minado():
  global n_max_bombas
  global n_bombas_em_campo
  linha = []
  matriz_jogo = []
  while len(matriz_jogo) != numero:
    n = random.randint(0, 1)
    n = str(n)
    if n == '1' and n_max_bombas > 0:
      n_max_bombas -= 1
      n_bombas_em_campo += 1
    else:
      n = '0'
    linha.append(n)
    if len(linha) == numero:
      matriz_jogo.append(linha)
      linha = []
  return matriz_jogo


def criando_campo_usuario():
  matriz_visivel = []
  linha = []
  c = 0
  while len(matriz_visivel) != numero:
    n = alfa[c]
    linha.append(n)
    if len(linha) == numero:
      matriz_visivel.append(linha)
      linha = []
    c += 1
  return matriz_visivel


def isnumber(value):
  try:
    float(value)
  except ValueError:
    return False
  return True


def imprimir(matriz_visivel):
  print()
  for l in range(numero):
    linha = ''
    print(' ')
    for c in range(numero):
      valor = ' '
      if isnumber(matriz_visivel[l][c]):
        if int(matriz_visivel[l][c]) == 0:
          valor = Fore.BLUE + matriz_visivel[l][c] + Fore.RESET
        elif int(matriz_visivel[l][c]) == 1:
          valor = Fore.GREEN + matriz_visivel[l][c] + Fore.RESET
        elif int(matriz_visivel[l][c]) == 2:
          valor = Fore.YELLOW + matriz_visivel[l][c] + Fore.RESET
        elif int(matriz_visivel[l][c]) >= 3:
          valor = Fore.RED + matriz_visivel[l][c] + Fore.RESET
      else:
        valor = matriz_visivel[l][c]
      linha += " " + valor + " |"
    print('  |' + linha)


def find_elemento_no_alfa(elemento):
  global alfa
  elemento = elemento.upper()
  list_element = alfa;
  try:
      index_element = list_element.find(elemento)
      if index_element >= 0:
        alfa = alfa.replace(elemento, '§')
        return index_element
      else:
        return None
  except ValueError:
      return None


def get_coordenadas(index):
  linha = index // numero;
  coluna = index - (linha * numero)
  return linha, coluna


def is_bomba(linha, coluna):
  bomba = matriz_jogo[linha][coluna]
  estado = 0;
  if bomba == '1':
    estado = 1
  else:
    estado = 0
  return estado


def get_vizinhos(linha, coluna):
  vizinhos = []
  numero_max = numero - 1
  if coluna + 1 <= numero_max:
    vizinhos.append([linha, coluna + 1])
    if linha + 1 <= numero_max:
      vizinhos.append([linha + 1, coluna + 1])
    if linha - 1 >= 0:
      vizinhos.append([linha - 1, coluna + 1])

  if coluna - 1 >= 0:
    vizinhos.append([linha, coluna - 1])
    if linha + 1 <= numero_max:
      vizinhos.append([linha + 1, coluna - 1])
    if linha - 1 >= 0:
      vizinhos.append([linha - 1, coluna - 1])

  if linha + 1 <= numero_max:
    vizinhos.append([linha + 1, coluna])
  if linha - 1 >= 0:
    vizinhos.append([linha - 1, coluna])
  return vizinhos

def analisar_vizinhos(vizinhos):
  c = 0
  for i in vizinhos:
    c += is_bomba(i[0],i[1])
  return c

def analisando_jogada(linha,coluna):
  estado = is_bomba(linha,coluna)
  if estado == 1:
    matriz_usuario[linha][coluna] = '*'
    estado = -1
  else :
    vizinhos = get_vizinhos(linha,coluna)
    c = analisar_vizinhos(vizinhos)
    if c > 0 :
      matriz_usuario[linha][coluna] = str(c)
    else :
      matriz_usuario[linha][coluna] = ' '
      for vizinho in vizinhos:
        jogar(matriz_usuario[vizinho[0]][vizinho[1]])
  return estado

def marcar_bomba(letra):
  index = find_elemento_no_alfa(letra)
  if index != None:
    linha,coluna = get_coordenadas(index)
    matriz_usuario[linha][coluna] = "º"
  replit.clear()

def game_over():
  print('GAME OVER')

def jogar(letra):
  global n_jogadas
  index = find_elemento_no_alfa(letra)
  n = 0
  if index != None:
    replit.clear()
    linha,coluna = get_coordenadas(index)
    n = analisando_jogada(linha,coluna)
    if n == -1 :
      imprimir(matriz_usuario)
      game_over()
    else:
      n_jogadas += 1
  else:
      replit.clear()
  return n

def start():
  n = 0
  while n >= 0 :
    # imprimir(matriz_jogo)
    imprimir(matriz_usuario)
    print(" .CAMPO MINADO")
    letra = input("Faça sua jogada:")
    if letra.find('-m') > 0:
      marcar_bomba(letra.replace('-m' , ''))
    else :
      n = jogar(letra)
      if len(alfa) - n_jogadas == n_bombas_em_campo:
        imprimir(matriz_usuario)
        print("GAMHOU")
        n = -1


# configuraçao
numero = 5
n_max_bombas = 5
n_bombas_em_campo = 0
n_jogadas = 0
alfa ='QWERTYUIOPASDFGHJKLZXCVBN'
matriz_jogo = criando_campo_minado()
matriz_usuario = criando_campo_usuario()

start()