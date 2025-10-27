import socket
import threading


def TCPClientTest(target_host="www.google.com", target_port=80):
    
    #Create a socket object with the IPv4 Address and TCP Client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #Connect the client to the target host and port
    client.connect((target_host, target_port))
    
    request_string =  f"GET / HTTP/1.1\r\nHost: {target_host}\r\nConnection: close\r\n\r\n" 
    http_request = request_string.encode('utf-8')
    #Send data
    client.send(http_request)
    
    #Receive data
    response = client.recv(4096)
    
    client.close()
    
    print(response.decode('utf-8', errors='ignore'))
    
    
    
def UDPClientTest(target_host="127.0.0.1", target_port=80):
    
    #Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    client.settimeout(5.0)
    
    data_to_send = b"AAABBBCCC"

    #Passing in =the data and the server that we will send to
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
    

    