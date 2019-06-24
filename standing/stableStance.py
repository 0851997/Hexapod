from time import sleep

def stableStance(config, time):
    #stablestance
    config.serialConn.write("#31P1055#26P1055#18P1055#30P1277#25P1277#17P1277#29P1722#24P1500#16P1278#13P1278#8P1500#0P1722#1P1722#9P1722#14P1722#2P1944#10P1944#15P1944T200r".encode())
    sleep(time)

def sit(config):
    #sit
    stableStance(config, 0.2)
    config.serialConn.write("#30P1139#9P1861#17P1139#14P1861#1P1861#25P1139#29P2022T500\r".encode())
    config.serialConn.write("#14P2056#1P2056#25P944#30P944#9P2056#17P944T500\r".encode())
    config.serialConn.write("#14P2350#1P2350#25P650#30P650#9P2350#17P650 #31P650#26P650#18P650#2P2350#10P2350#15P2350T500\r".encode())
