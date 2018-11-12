import servidorControle
import socket
import ast
import subprocess
from xmlrpc.server import SimpleXMLRPCServer


def played(data, campoMinado, campoLimpo):

    data = ast.literal_eval(data)
    campoMinado = ast.literal_eval(campoMinado)
    campoLimpo = ast.literal_eval(campoLimpo)

    if (data['played'] == 0):
        cm = servidorControle.CampoMinado(data['sizeField'], data['numberBomb'], 0)
        minefield = cm.dictMineField
        print(cm.dict.keys())
        print(cm.dict.values())
        cm.showMineField()
        answer = cm.dict
    else:
        game = servidorControle.Game(data, campoMinado, campoLimpo)
        minefield = game.campoMinado
        answer = game.dict
        

    answer = str(answer)
    mineField = str(minefield)



    return answer, mineField

def server():
    serverRPC = SimpleXMLRPCServer(('localhost', 7002))
    serverRPC.register_function(played)
    print("Abrindo servidor. Aperte CTRL+C para encerrar...")
    serverRPC.serve_forever()

server()
