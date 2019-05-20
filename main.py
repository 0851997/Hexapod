import walking.tripodgait as walking
import portSetup.portSetup as port
import standing.stableStance as standing

try:
    port1 = port.Ports("UART1","/dev/ttyO1",9600)
    walking.ports(port1)
    walking.tripodWalking(0.05)

except KeyboardInterrupt:
    standing.sit()