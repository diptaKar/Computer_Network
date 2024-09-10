import socket
format = 'utf-8'
buffer = 16
disconnected = 'End'
port = 5050  
hostname = socket.gethostname() 
host_ip = socket.gethostbyname(hostname) 

server_socket_address = (host_ip, port)
client = socket.socket(socket.AF_INET ,  socket.SOCK_STREAM)                                                      
client.connect(server_socket_address)

def msg_to_send(msg):
    message = msg.encode(format)
    msg_length = str(len(message)).encode(format)
    msg_length += b" "*(buffer - len(msg_length))
    
    client.send(msg_length)
    client.send(message)

    print(client.recv(2048).decode(format))

while True:
    input_msg = input('Please enter your message ')
    if input_msg.lower() == 'done':
        msg_to_send(disconnected)
        break
    else:
        msg_to_send(input_msg)
