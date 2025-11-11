import socket
import threading
import requests
import datetime as datetime
import time


# Helper function to handle a single client connection
def handle_client(conn, addr):
    print(f"Connected by {addr}")
    try:
        while True:
            # Receive data
            data = conn.recv(1024)

            if not data:
                break

            client_message = data.decode('utf-8')
            print(f"[{addr[0]}:{addr[1]}] Received: {client_message}")

            # Send echo response
            response_message = f"Echo: {client_message.upper()}"
            conn.sendall(response_message.encode('utf-8'))
            
    except Exception as e:
        print(f"Error handling connection from {addr}: {e}")
    finally:
        conn.close()
        print(f"Connection closed with {addr}")


class Network:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
    
    def TCPClientServer(self):
        # Create a socket object with the IPv4 Address and TCP Client
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            # Connect the client to the target host and port
            client.connect((self.ip, self.port))
            
            # Formulate and send HTTP GET request
            request_string = f"GET / HTTP/1.1\r\nHost: {self.ip}\r\nConnection: close\r\n\r\n" 
            http_request = request_string.encode('utf-8')
            client.send(http_request)
            
            # Receive data
            response = client.recv(4096)
            
            print(response.decode('utf-8', errors='ignore'))
            
        except ConnectionRefusedError:
            print(f"Error: Connection refused by {self.ip}:{self.port}. Is the server running?")
        except Exception as e:
            print(f"An error occurred in TCP Client: {e}")
        finally:
            client.close()

    def UDPClientServer(self): # FIXED: Removed parameters and now uses self.ip/port
        target_host = self.ip
        target_port = self.port
        
        # Create a socket object (SOCK_DGRAM for UDP)
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        client.settimeout(5.0)
        
        data_to_send = b"AAABBBCCC"

        try:
            # Passing in the data and the server that we will send to
            client.sendto(data_to_send, (target_host, target_port))
            
            # Received UDP data back
            data, addr = client.recvfrom(4096)
            print(f"Received from {addr}: {data.decode('utf-8', errors='ignore')}")
            
        except socket.timeout:
            print("Timeout: No response received.")
        except Exception as e:
            print(f"An error occurred in UDP Client: {e}")
        finally:
            client.close()
        
    def TCPHostServer(self):
        # 1. Create a socket object and use a context manager
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
                
                # Allows the server to immediately reuse the port
                server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                
                # 2. Bind the socket to the ip address and the port 
                server_socket.bind((self.ip, self.port))
                
                # 3. Set the socket to listen for incoming connection
                server_socket.listen(5) # max connections backlog set to 5
                print(f"Server listening on {self.ip}:{self.port} ... ")
                
                while True:
                    # 4. Accept a new connection
                    conn, addr = server_socket.accept()
                    
                    # 5. Start a new thread to handle the client
                    client_handler = threading.Thread(target=handle_client, args=(conn, addr))
                    client_handler.start()

        except Exception as e:
            print(f"An error occurred in TCP Server: {e}")
            
    

        

# The rest of your code remains largely the same
def NetworkingCLI():
    display = """
    *** Python Network CLI ***
    1. TCP Client (HTTP GET)
    2. UDP Client (Send/Receive)
    3. TCP Host Server (Multi-threaded)
    """
    
    print(display)
    
    while True:
        try:
            command = int(input(">>> Enter Command Number: "))
            
            if command in [1, 2, 3]:
                host = str(input("Target IP/Host: "))
                port = int(input("Target Port: "))
                network = Network(host, port) # Use user input for all cases
                
                if command == 1:
                    network.TCPClientServer()
                elif command == 2:
                    network.UDPClientServer()
                elif command == 3:
                    # Note: TCPHostServer will block the CLI, run it in a separate terminal for testing
                    network.TCPHostServer()
            else:
                print("Invalid command.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\nExiting CLI.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    try:
        NetworkingCLI()
    except KeyboardInterrupt:
        print("\nProgram shut down.")