import portSetup.portSetup as port
import walking.tripodgait as walking
import standing.stableStance as standing
import string

#turnLeftBoudaries = 0 - 85
#strafeLeftBoundary = 85 - 224
#forwardBackwardBoundary = 224 -416
#strafeRightBoundary = 416 - 555
#turnRightBoundary = 555 - 640
boundary = (85, 224, 416, 555, 640)
centerLocationPoint = 0;
personYLocationBorder = 0;

config = port.Configurations("UART1","/dev/ttyO1",9600)
config.initializePorts()
config.serialConn.close()
config.serialConn.open()

try:
    if config.serialConn.isOpen():
        standing.stableStance(config)
        while(True):
            mode = input("Press a key for movement command: ")
            if walkingMode == 'q':
                walking.strafeLeft(config, 0.05)
            elif walkingMode == 'w':
                walking.tripodWalking(config, 0.05)
            elif walkingMode == 'e':
                walking.strafeRight(config, 0.05)
            elif walkingMode == 'a':
                walking.turnLeft(config)
            elif walkingMode == 's':
                walking.reverse(config, 0.05)
            elif walkingMode == 'd':
                walking.turnRight(config)
            elif walkingMode == 'z':
                standing.stableStance(config)
            elif walkingMode == 'x':
                standing.sit(config)
    
    #THIS IS THE INTERFACE FOR THE END OF THE PROJECT
    #         while(True):
    #             if centerLocationPoint < boundary[0]:
    #                 walking.turnLeft()
    #             elif centerLocationPoint < boundary[1]:
    #                 walking.strafeLeft()
    #             elif centerLocationPoint < boundary[2]:
    #                 print ("random")#if personYLocationBorder 
    #             elif centerLocationPoint < boundary[3]:
    #                 walking.strafeRight()
    #             elif centerLocationPoint < boundary[4]:
    #                 walking.turnRight()
    #             
    #             
    #     port1 = port.Ports("UART1","/dev/ttyO1",9600)
    #     walking.ports(port1)
    #     walking.tripodWalking(0.05)

except KeyboardInterrupt:
    standing.sit(config)
    config.serialConn.close()
