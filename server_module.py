import socket

def create_server_socket(host, port):
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    return server_socket

def accept_connection(server_socket):
    conn, address = server_socket.accept()
    return conn, address

def receive_message(conn):
    try:
        data = conn.recv(1024).decode()
        return data
    except ConnectionResetError:
        return None

def send_response(conn, response):
    conn.send(response.encode())

def close_server_connection(conn):
    conn.close()
