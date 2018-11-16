import socket

port = 5555

def onClientChoice():
    IPaddr = input("IP-address of server: ")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IPaddr,port))



onClientChoice()
    
