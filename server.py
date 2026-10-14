import socket
import threading

HOST = '127.0.0.1'
PORT = 8888
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

def broadcast(msg):
    for c in clients:
        try:
            c.send(msg)
        except:
            pass

def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            if not msg:
                break
            broadcast(msg)
        except:
            break
            
    
    try:
        if client in clients:
            i = clients.index(client)
            name = nicknames[i]
            broadcast(f'{name} left!'.encode('utf-8'))
            clients.remove(client)
            nicknames.remove(name)
            client.close()
    except:
        pass

print("Server is running...")
while True:
    try:
        client, addr = server.accept()
        client.send('NICK'.encode('utf-8'))
        name = client.recv(1024).decode('utf-8')
        
        if name:
            nicknames.append(name)
            clients.append(client)
            broadcast(f'{name} joined!'.encode('utf-8'))
            thread = threading.Thread(target=handle, args=(client,))
            thread.start()
    except:
        pass