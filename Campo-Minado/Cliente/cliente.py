import sys
from _operator import concat

import udp_cliente
from datetime import datetime


def menu():
    msn = ""
    try:

        while msn != "0":


            x = int(input("Digite a posicao do eixo X:"))
            y = int(input("Digite a posicao do eixo Y:"))
            msn = (udp_cliente.client(str(x)+"-"+str(y)))

    except:
        for val in sys.exc_info():
            print(val)
