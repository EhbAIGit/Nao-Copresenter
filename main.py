from server_module import create_server_socket, accept_connection, receive_message, send_response, close_server_connection
import text_parser
import socket

def server_program():
    host = socket.gethostname()
    port = 5000

    print("Starting server...")
    server_socket = create_server_socket(host, port)
    conn, address = accept_connection(server_socket)
    print("Connection from: " + str(address))

    try:
        while True:
            input_text = input('Enter text to process and send: ')
            if input_text.lower() == 'exit':
                break
            
            # Process the text to get sentences
            sentences = process_text(input_text)
            for sentence in sentences:
                send_response(conn, sentence)
                print("Sent: " + sentence)
                print("Waiting for client response...")
                client_response = receive_message(conn)
                if client_response is None or client_response.lower() != 'success':
                    print("No success message received or connection error.")
                    break
                else:
                    print("Received success response from client.")
    finally:
        close_server_connection(conn)
        server_socket.close()

if __name__ == '__main__':
    server_program()