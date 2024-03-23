import socket

HOST = 'localhost' #serve pra informar de onde é o servidor, no caso vai ser na minha maquina.
PORT = 8002 # porta 8000 é do django então 8002 pra diferenciar caso ja esteja usando django.

#primeiro temos que informar que estamos utilizando o protocolo TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#agora preciso falar para esse socket onde ele está rodando, qual o ip, qual a porta etc.
sock.bind((HOST, PORT))#dentro do bind tem uma tupla. Aki estou falando que ele vai rodar dentro desse ip e nessa porta em específico.

#Agora preciso falar para o servidor de quem ele vai escutar, vai ter pessoas fazendo requisições para este servidor.
sock.listen(5)
while True:
    #com essa variavel o servidor ja está funcionando.
    novoSock, _ = sock.accept()
    
    #Fazer o servidor receber uma msg em binário, lembra que tudo que o servidor recebe é em binário.
    #o decode serve decodificar as msgs que chegam do cliente
    mensagem = novoSock.recv(1024).decode()
    print(mensagem)
    #enviando msg para o cliente, no momento q o cliente entra em contato, os dados do clente fica salvo neste servidor.
    novoSock.send(b'ola')