import socket
import threading


class Network:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
    
    def TCPClientServer(self):
        
        #Create a socket object with the IPv4 Address and TCP Client
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        #Connect the client to the target host and port
        client.connect((self.ip, self.port))
        
        request_string =  f"GET / HTTP/1.1\r\nHost: {self.ip}\r\nConnection: close\r\n\r\n" 
        http_request = request_string.encode('utf-8')
        #Send data
        client.send(http_request)
        
        #Receive data
        response = client.recv(4096)
        
        client.close()
        
        print(response.decode('utf-8', errors='ignore'))
        
        
        
    def UDPClientServer(target_host="127.0.0.1", target_port=80):
        
        #Create a socket object
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        client.settimeout(5.0)
        
        data_to_send = b"AAABBBCCC"

        #Passing in the data and the server that we will send to
        client.sendto(data_to_send ,(target_host, target_port))
        
        try:
            #Received UDP data back
            data, addr = client.recvfrom(4096)
            print(f"Received from {addr}: {data.decode('utf-8', errors='ignore')}")
        except socket.timeout:
            print("Timeout: No response received. ")
        except Exception as e:
            print(f"An error occured: {e}")
        finally:
            client.close()
        

    def TCPHostServer(self):
        #1. Create a socket object and insert the IPv4 address and TCP client in the parameter
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            
            #Allows the server to immediately reuse the port
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            #2. Bind the socket to the ip address and the port 
            server_socket.bind((self.ip, self.port))
            
            #3. Set the socket to listen for incoming connection
            server_socket.listen()
            print(f"Server listening on {self.ip}:{self.port} ... ")
            
            while True:
                conn, addr = server_socket.accept()
                
                with conn:
                    print(f"Connected by {addr}")
                    
                    while True:
                        
                        data = conn.recv(1024)
                        
                        if not data:
                            break
                        
                        client_message = data.decode('utf-8')
                        print(f"Received: {client_message}")
                        
                        response_message = f"Echo: {client_message.upper()}"
                        conn.sendall(response_message.encode('utf-8'))
                        
                    print(f"Connection closed with {addr}")


def NetworkingCLI():
    display = """
    1. TCP Client Server
    2. UDP Client Server
    3. TCP Host Server
    """
    
    print(display)
    command = ""
    
    while True:
        command = int(input(">>> "))
        match command:
            case 1:
                host = str(input("Target: "))
                port = int(input("Port: "))
                network = Network(host, port)
                network.TCPClientServer()
                
            case 2:
                host = str(input("Target: "))
                port = int(input("Port: "))
                network = Network(host="127.0.0.1", port=80)
                network.UDPClientServer()
                
            case 3:
                host = str(input("Target: "))
                port = int(input("Port: "))
                network = Network(host, port)
                network.TCPHostServer()
                

if __name__ == '__main__':
    try:
        NetworkingCLI()
    except KeyboardInterrupt:
        print("\nServer shutting down.")