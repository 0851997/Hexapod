import portSetup.portSetup as port
import walking.tripodgait as walking
import standing.stableStance as standing
import keyboard

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
            if keyboard.is_pressed('w'):
                walking.tripodWalking(config, 0.05)
            elif keyboard.is_pressed('s'):
                walking.reverse(config)
            elif keyboard.is_pressed('a'):
                walking.strafeLeft(config, 0.05)
            elif keyboard.is_pressed('x'):
                standing.stableStance(config)
            elif keyboard.is_pressed('q'):
                standing.sit(config)
    config.serialConn.close()
    
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