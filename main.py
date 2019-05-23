import walking.tripodgait as walking
import portSetup.portSetup as port
import standing.stableStance as standing
from _ast import If

#turnLeftBoudaries = 0 - 85
#strafeLeftBoundary = 85 - 224
#forwardBackwardBoundary = 224 -416
#strafeRightBoundary = 416 - 555
#turnRightBoundary = 555 - 640
boundary = (85, 224, 416, 555, 640)
centerLocationPoint = 0;
personYLocationBorder = 0;

try:
    while True:
        if centerLocationPoint < boundary[0]:
            walking.turnLeft()
        elif centerLocationPoint < boundary[1]:
            walking.strafeLeft()
        elif centerLocationPoint < boundary[2]:
            print ("random")#if personYLocationBorder 
        elif centerLocationPoint < boundary[3]:
            walking.strafeRight()
        elif centerLocationPoint < boundary[4]:
            walking.turnRight()
            
            
    #     port1 = port.Ports("UART1","/dev/ttyO1",9600)
    #     walking.ports(port1)
    #     walking.tripodWalking(0.05)

except KeyboardInterrupt:
    standing.sit()