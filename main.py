import walking.tripodgait as mx
import portSetup.portSetup as port
import standing.stableStance as standing

try:
    port1 = port.Ports("UART1","/dev/ttyO1",9600)
    mx.ports(port1)
    mx.tripodWalking(0.05)

except KeyboardInterrupt:
    standing.sit()