import socket

port = 5555

def onClientChoice():
    IPaddr = input("IP-address of server: ")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IPaddr,port))

def onServerChoice():
    HOST = ''
    PORT = 55555

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)



onClientChoice()
    
