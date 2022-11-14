import socket            #importa o modulo de sockets

HEADER = 64
PORT = 5050                         # Porta de acesso
FORMAT = 'utf-8'                    # Formato para codificacao
DISCONNECT_MESSAGE = "!DISCONNECT"  # Desconexão
SERVER = "192.168.1.26"             # IP do servidor
ADDR = (SERVER, PORT)               # Address do servidor

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Declarando o client
client.connect(ADDR)                                        # atribuindo as características do client (server, PORT)

def send(msg):
    message = msg.encode(FORMAT)                        # Define o formato de decodificacao
    msg_length = len(message)                           # Salva o comprimento da mensagem
    send_length = str(msg_length).encode(FORMAT)        # Salva o comprimendo de forma codificada
    send_length += b' ' * (HEADER - len(send_length))   # Garante que a mensagem tenha 64 bytes
    client.send(send_length)                            # Envia o comprimento da mendagem
    client.send(message)                                # Envia a mensagem
    print(client.recv(2048).decode(FORMAT))             # Decodificacao da mensagem

send("Hello World!")
input()
send("Hello Everyone!")
input()
send("Hello Tim!")

send(DISCONNECT_MESSAGE)
