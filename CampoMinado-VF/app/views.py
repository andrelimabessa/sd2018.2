from django.shortcuts import render
from django.utils import timezone
from .forms import JogadaForm
from .campo_minado_negocio import CampoMinado

# Create your views here.
def post_list(request):
	return render(request, 'post_list.html', {})

def NovoJogo(request):
	jogo = JogadaForm(request.POST)
	return render(request, 'index.html', {'entrada': jogo})

def Partida(request):
	if request.method == 'POST':
		entrada = JogadaForm(request.POST)
		if entrada.is_valid():
			linha = entrada.cleaned_data['linha']
			coluna = entrada.cleaned_data['coluna']
			objeto = CampoMinado(linha,coluna)
			tabuleiro = objeto.retorna_tabuleiro()
			objeto.salvarJogo()
	else:
		entrada = JogadaForm()

	return render(request, 'tabuleiro.html', {'entrada': entrada, 'tabuleiro': tabuleiro})

def Principal(request):
	objeto = CampoMinado(0,0)
	stats = {}
	stats = objeto.totais()
	linMax = stats['linMax']
	colMax = stats['colMax']
	totBomb = stats['totBombas']
	jogadas = stats['totJogadas']
	if request.method == 'POST':
		entrada = JogadaForm(request.POST)
		if entrada.is_valid():
			linha = entrada.cleaned_data['linha']
			coluna = entrada.cleaned_data['coluna']
			perdeu = objeto.jogada(linha,coluna)
			objeto.salvarJogo()
			if perdeu == False:
				if((((linMax-1)*(colMax-1))-(jogadas+1))==totBomb):
					mensagem = 'MUITO BEM VOCE GANHOU!!!!'
					tabuleiro = objeto.retorna_tabuleiro()
					return render(request, 'gameOver.html', {'tabuleiro': tabuleiro, 'mensagem': mensagem})
			elif(perdeu == 2):
				mensagem = 'Jogo Salvo!!'
				return render(request, 'gameOver.html', {'mensagem': mensagem})
			else:
				tabuleiro = objeto.retorna_tabuleiro()
				boardbomba = objeto.matriz_bomba(tabuleiro)
				mensagem = 'SPLASH!!! VOCÊ MORREU!!'
				return render(request, 'gameOver.html', {'tabuleiro': boardbomba, 'mensagem': mensagem})

	tabuleiro = objeto.retorna_tabuleiro()
	return render(request, 'tabuleiro.html', {'entrada': entrada, 'tabuleiro': tabuleiro})
