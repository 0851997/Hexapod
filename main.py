import portSetup.portSetup as port
import walking.tripodgait as walking
import standing.stableStance as standing
import yoloServer.yolo_pickle_server as server
import time
import string
import threading

boundary = (85, 224, 416, 555, 640)
centerLocationPoint = 0;
personYLocationBorder = 0;

config = port.Configurations("UART1","/dev/ttyO1",9600)
config.initializePorts()
config.serialConn.close()
config.serialConn.open()

# ready = threading.Event()
# connection = server.Server('192.168.43.5',8787,ready)
# mythread = threading.Thread(target=connection.connect)
# mythread.start()
# ready.wait()
# thread = threading.Thread(target=connection.run)
# thread.start()

try:
    if config.serialConn.isOpen():
        standing.stableStance(config, 0.2)
        while(True):
            mode = input("Press a key for movement command: ")
            for i in range(3):
                if mode == 'q':
                    walking.strafeLeft(config, 0.5)
                elif mode == 'w':
                    walking.tripodWalking(config, 0.5)
                elif mode == 'e':
                    walking.strafeRight(config, 0.5)
                elif mode == 'a':
                    #we are testing this now
                    walking.turnLeft(config, 1.5)
                    break
                elif mode == 's':
                    walking.reverse(config, 0.5)
                elif mode == 'd':
                    #we are testing this now
                    walking.turnRight(config, 1.5)
                    break
                elif mode == 'z':
                    standing.stableStance(config, 0.2)
                    break
                elif mode == 'x':
                    standing.sit(config)
                    break
#             if (connection.rectCenterWidth > 0 and connection.rectCenterWidth < 213):
#                 walking.turnLeft(config, 0.05)
#             #elif (connection.rectCenterWidth < 224 and connection.rectCenterWidth > 112):
#             #   walking.strafeLeft(config, 0.2)
#             elif (connection.rectCenterWidth > 213 and connection.rectCenterWidth < 416):
#                 #total 90 - 176
#                 #front 90 - 119
#                 if connection.dimensionRectangleWidth > 90 and connection.dimensionRectangleWidth < 119:
#                     walking.tripodWalking(config, 0.05)
#                 #stand 119 - 147
#                 elif connection.dimensionRectangleWidth > 119 and connection.dimensionRectangleWidth < 147:
#                     standing.stableStance(config, 0.2)
#                 #back 147 - 176
#                 elif connection.dimensionRectangleWidth > 147 and connection.dimensionRectangleWidth < 176:
#                     walking.reverse(config, 0.05)
#             #elif (connection.rectCenterWidth < 512 and connection.rectCenterWidth > 406):
#             #    walking.strafeRight(config, 0.2)
#             elif (connection.rectCenterWidth > 416 and connection.rectCenterWidth < 640):
#                 walking.turnRight(config, 0.05)
#             elif connection.rectCenterWidth < 0 or connection.rectCenterWidth > 640:
#                 standing.stableStance(config, 0.2)
#             else:
#                 standing.stableStance(config, 0.2)
except KeyboardInterrupt:
    standing.sit(config)
    config.serialConn.close()
    connection.conn.close()