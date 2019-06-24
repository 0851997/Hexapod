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
        
        #Loop for main program
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
                    walking.turnLeft(config, 0.5)
                elif mode == 's':
                    walking.reverse(config, 0.5)
                elif mode == 'd':
                    walking.turnRight(config, 0.5)
                elif mode == 'z':
                    standing.stableStance(config, 0.2)
                    break
                elif mode == 'x':
                    standing.sit(config)
                    break
#             #turnLeftBoudaries = 0 - 85
#             #strafeLeftBoundary = 85 - 224
#             #forwardBackwardBoundary = 224 - 416
#             #strafeRightBoundary = 416 - 555
#             #turnRightBoundary = 555 - 640
#             if (connection.rectCenterWidth < 112 and connection.rectCenterWidth > 0):
#                 standing.stableStance(config, 0.2)
#                 walking.turnLeft(config, 0.5)
#                 
#             elif (connection.rectCenterWidth < 224 and connection.rectCenterWidth > 112):
#                 walking.strafeLeft(config, 0.5)
#                 
#             elif (connection.rectCenterWidth < 406 and connection.rectCenterWidth > 278):
#                 #front 85 - 220
#                 #stand 220 - 265
#                 #back 265 - 615
#                 if connection.dimensionRectangleWidth > 90 and connection.dimensionRectangleWidth < 119:
#                     standing.stableStance(config, 0.2)
#                     walking.tripodWalking(config, 0.5)
#                     
#                 elif connection.dimensionRectangleWidth > 119 and connection.dimensionRectangleWidth < 147:
#                     standing.stableStance(config, 0.2)
# 
#                 elif connection.dimensionRectangleWidth > 147 and connection.dimensionRectangleWidth < 176:
#                     standing.stableStance(config, 0.2)
#                     walking.reverse(config, 0.5)
#                     
#             elif (connection.rectCenterWidth < 512 and connection.rectCenterWidth > 406):
#                 walking.strafeRight(config, 0.5)
# 
#             elif (connection.rectCenterWidth < 640 and connection.rectCenterWidth > 512):
#                 standing.stableStance(config, 0.2)
#                 walking.turnRight(config, 0.5)
# 
#             elif connection.rectCenterWidth < 0 or connection.rectCenterWidth > 640:
#                 standing.stableStance(config, 0.2)
#             
#             else:
#                 standing.stableStance(config, 0.2)
# 
#             time.sleep(0.5)

except KeyboardInterrupt:
    standing.sit(config)
    config.serialConn.close()
    connection.conn.close()