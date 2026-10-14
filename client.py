import socket
import threading

name = input("Choose Your Nickname : ")
HOST = '127.0.0.1'
PORT = 8888

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))

def recieve():
    while True:
        try:
            msg = (client.recv(1024).decode('utf-8'))
            if msg == 'NICK':

                client.send (name.encode("utf-8"))
            else:
                print(msg)
        except:
            print("Disconnect!")
            client.close()
            break

receive_thread = threading.Thread(target=recieve)
receive_thread.start()

while True:
    msg = f'{name}:{input("")}'
    client.send(msg.encode('utf-8'))