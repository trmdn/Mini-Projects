import socket, threading

def handle_messages(connection: socket.socket):
    while True:
        try:
            message = connection.recv(1024)
            
            if message:
                print(message.decode())
            else:
                connection.close()
                break
        
        except Exception as e:
            print(f"Error handling message from server: {e}")
            connection.close()
            break


def client() -> None:
    SERVER_ADDRESS = '127.0.0.1'
    SERVER_PORT = 12000

    try:
        socket_instance = socket.socket()
        socket_instance.connect((SERVER_ADDRESS, SERVER_PORT))
        
        threading.Thread(target=handle_messages, args=[socket_instance]).start()

        print('Connected to chat!')

        while True:
            message = input()

            if message == "quit":
                break

            socket_instance.send(message.encode())

        socket_instance.close()
    
    except Exception as e:
        print(f"Error connecting to server socket {e}")
        socket_instance.close()

if __name__ == "__main__":
    client()