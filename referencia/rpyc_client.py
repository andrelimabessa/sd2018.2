import rpyc

def resposta(string):
    print(repr(string))

def client():
    
    config = {'allow_public_attrs': True}
    proxy = rpyc.connect('localhost', 18861, config=config)

    proxy.root.jogar()
    # print(teste)
