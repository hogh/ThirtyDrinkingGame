import socket
import random
import json

port = 55555

def onClientChoice():
    IPaddr = input("IP-address of server: ")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IPaddr,port))

'''
Messages to transmit:
a) SwitchTurn
b) [Terninger] (array of terninger) // Spiller slag
c) [PickedTerninger][NotPieckedTerninger][Score] // S 
d) [TotalScore]
'''

'''
[STATE] {Turn, Roll, Result, End} // State can be one of those
- [TURN] // Shift turn
- [ROLL][DICES]{Dice1,Dice2,Dice3..DiceN} // Contains array of dices 
- [PICKED]{Dice1,DiceK...DiceN} // Contains the picked Dices by the oppnent
- [TOTAL]{Value}

 
'''



def getRandomDices(no_dices):
    result = []
    for i in range(0, dices_left):
        result.append(random.randint(1 ,6))


    return result




def handleTurn(dices_left):
    print("Turn")




def handleRoll():
    print("Roll")

def handlePicked():
    print("Picked")

def handleTotal():
    print("Total")
        

    
def onNewEvent(json_input):
    fuck_input = json_input.loads(json_input)
    state = fuck_input["state"]

    if(state == "TURN"):
        handleturn()
    elif(state == "ROLL"):
        handleRoll()
    elif(state == "PICKED"):
        handlePicked()
    elif(state == "TOTAL"):
        handleTotal();

    
            

    
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




    
handleTurn(6)
