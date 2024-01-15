import socket


# initialize the socket object
def init_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 8888))  # the 5000 is the server ip that client is going to connect to.
    s.listen(5)  # the queue
    return s


# functions to establish the client, and to send to the client
def get_client(s):
    while True:
        client_socket, address = s.accept()
        print(f'IP Address [{address}] has connect to the server')
        if client_socket:
            return client_socket


# constructs message, sending just the number 10 for this example
def msg_construction():
    packet = 10
    return packet.to_bytes(2, 'big')


# the function which runs continually throughout, sending packets
def send(client_socket):
    while True:
        msg = msg_construction()
        client_socket.send(msg)


def main():
    s = init_server()
    c = get_client(s)
    send(c)


if __name__ == '__main__':
    main()
