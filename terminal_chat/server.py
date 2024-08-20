import socket, threading

connections = []

def handle_users_connection(connection: socket.socket, address: str) -> None:
    while True:
        try:
            message = connection.recv(1024)

            if message:
                print(f'{address[0]}:{address[1]} - {message.decode()}')

                message_to_send = f'From {address[0]}:{address[1]} - {message.decode()}'
                broadcast(message_to_send, connection)
            
            else:
                remove_connection(connection)
                break

        except Exception as e:
            print(f'Error to handle user connection: {e}')
            remove_connection(connection)
            break

def broadcast(message: str, connection: socket.socket) -> None:
    for client_conn in connections:
        if client_conn != connection:
            try:
                client_conn.send(message.encode())
            except Exception as e:
                print(f'Error broadcasting message: {e}')
                remove_connection(client_conn)


def remove_connection(conn: socket.socket) -> None:
    if conn in connections:
        conn.close()
        connections.remove(conn)

def server() -> None:
    LISTENING_PORT = 12000

    try:
        socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_instance.bind(('', LISTENING_PORT))
        socket_instance.listen(4)

        print('Server running!')

        while True:
            socket_connection, address = socket_instance.accept()
            connections.append(socket_connection)
            threading.Thread(target=handle_users_connection, args=[socket_connection, address]).start()
    
    except Exception as e:
        print(f"An error has occurred when instancing socket: {e}")
    finally:
        if len(connections) > 0:
            for conn in connections:
                remove_connection(conn)
        socket_instance.close()

if __name__ == "__main__":
    server()