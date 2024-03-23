'''receber mensagem'''
# import socket

# #criando um cliente.
# #O cliente não precisa se estabelecer em nenhuma porta ele so precisa se conectar com alguém.
# HOST = 'localhost'#aki é o mesmo ip do seu servidor.
# PORT = 8002

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect((HOST, PORT))#conectando com o servidor, tem q ser uma tupla dentro do connect.

# #o cliente enviando uma msg para o servidor.
# #use o encode para codificara msg, ou seja para transformar a msg em binário
# sock.send(input('Digite uma mensagem ').encode())

# #receber msg do servidor
# confirmacao = sock.recv(1024)
# if confirmacao == b'ola':
#     print('mensagem recebida')

'''receber arquivo'''
import socket

HOST = 'localhost'
PORT = 8002

arquivo = open('python.png', 'rb')#abrindo a imagem

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.send(input('Digite o nome do arquivo: ').encode())
sock.send(arquivo.read())
confirmacao = sock.recv(1024)
if confirmacao == b'ok':
    print('mensagem recebida')