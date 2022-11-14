import socket       #importa o modulo de sockets
import threading    #importa o modulo de threads

HEADER = 64       
PORT = 5050                                            # Porta de acesso
SERVER = socket.gethostbyname(socket.gethostname())    # Forma padrao para adquirir o IP do host
ADDR = (SERVER, PORT)                                  # Endereco para realizar o server bind (utilizando o Server IP e a Porta de Acesso)
FORMAT = 'utf-8'                                       # Formato de decodificacao
DISCONNECT_MESSAGE = "!DISCONNECT"                     # Desconexão

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # Declarando o servidor
server.bind(ADDR)                                             # utilizando o metodo bind com a Server IP e a Porta de Acesso

def handle_client(conn, addr):                    # Define nova função 
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()
        

def start():                                                 # define nova função start
    server.listen()                                          # procura novas conexões
    print(f"[LISTENING] Server is listening on {SERVER}") 
    while True:                                                             # loop infinito "escutando" até que o servidor seja desligado
        conn, addr = server.accept()                                        # bloqueia o loop até uma nova conexão ocorrer
        thread = threading.Thread(target=handle_client, args=(conn, addr))  # a thread eh utilizada para realizar as acoes solicitadas pelo cliente 
        thread.start()                                                      # inicia a thread 
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")  #indica que o servidor está iniciando
start()
