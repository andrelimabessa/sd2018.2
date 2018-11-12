import zmq
import sys

def main():
    try:
        context = zmq.Context(1)
        frontend = context.socket(zmq.XREP)
        frontend.bind("tcp://*:5000")
        backend = context.socket(zmq.XREQ)
        backend.bind("tcp://*:5001")
        zmq.device(zmq.QUEUE, frontend, backend)

    except :
        for val in sys.exc_info():
            print(val)
        print("Desativa a fila") 
    finally:
        pass
        frontend.close()
        backend.close()
        context.term()

if __name__ == "__main__":
    main()
