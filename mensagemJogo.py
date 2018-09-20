class MensagemJogo:
    def exibeMensagemVitoria(self):
        print("####### VOCÊ VENCEU!  ##########")
        print("Realizou suas escolhas sem explodir nenhuma BOMBA.")
    
    def exibeQtdJogadasRestantes(self,totalJogadasRestantes):
        print("TOTAL JOGADAS FALTANDO: ", totalJogadasRestantes)
    
    def salvandoJogo(self):
        print("########## SALVANDO O JOGO ############")