from time import sleep

''' def degree(a):
    b = a/180*2000+500
    return b
 '''
def tripodWalking(forward, time):
    if forward == True:
        print("#25P944#26P1056#24P1167#14P2056#1P2056#15P1944#2P1944#13P1611#0P2056T3000\r".encode())
        sleep(3)
        print("#29P2056#24P1500#16P944#0P1722#8P1167#13P944T3000\r".encode())
        sleep(3)
        print("#30P944#17P944#18P1056#31P1056#29P1389#16P944#9P2056#10P1944#8P1833T3000\r".encode())
        sleep(3)
        print("#29P1722#24P1833#16P1611#13P1278#8P1500#0P1722\r".encode())
        code = "string"
        return(code)
        print("a")
    elif forward == False:
        print("d")
    else:
        print("k")


def stopping():
    print("r")


def send():
    print("d")


def setup():
    print("l")


# ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
# ser.close()
# ser.open()
# if ser.isOpen():
#     while(True):
#         print ("Serial is open!")
#         ser.write("#0 P500\r".encode())
#         sleep(1)
#         ser.write("#0 P2500\r".encode())
#         sleep(1)
# ser.close()
