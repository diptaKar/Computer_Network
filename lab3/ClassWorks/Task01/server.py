import socket

buffer = 16
format = 'utf-8'
port = 5050
hostname = socket.gethostname() 
host_ip = socket.gethostbyname(hostname)
disconnected = 'End'
server_socket_address = (host_ip, port) 

server = socket.socket(socket.AF_INET ,  socket.SOCK_STREAM) 

server.bind(server_socket_address)

server.listen()
print("Server is listening.")

while True:
    conn,addr = server.accept()
    print(f"Connected to {addr}")
    connected = True
    while connected:
        message_length = conn.recv(buffer).decode(format)
        print("Length of the message to be sent ", message_length)
        if message_length:
            msg_length = int(message_length)
            msg = conn.recv(msg_length).decode(format)

            if msg == disconnected:
                print('Terminating connection with ',addr)
                conn.send('Connection ended\n'.encode(format))
                connected = False
            else:
                print(msg)
                conn.send('Received your message.'.encode(format))
conn.close()