# Hexapod-PRO78
The Hexapod project consists of two parts.
* The server side consisting of the hexapod, microcontroller, ssc-32u board and servo motors. The server code is responsible for the movement of the Hexapod and tracking of a person.
* The client side represents a device on which a webcam can be plugged in. The client code is resposible for running computer vision for detection.

## THE ABILITIES OF THE HEXAPOD
### Movements
**The hexapod is equipped with the following walking functionalities:**
* Forward movement
* Backward movement
* Turn 90° left movement
* Turn 90° right movement
* Strafing left movement

**Good to know:**
* Every walking movement uses the tripod gait fully. 
* Exceptions are when sitting and standing. 
* Turns will not be taken with stationary legs.

### Modules
Modules are made for the hexapod. Every module is a grouped up set of actions that describe a broader functionality.(e.g. portSetup, standing, walking) 

All modules are imported inside [main.py](./main.py). Here is where the main work is done.
* Ports are initialized by importing [portSetup.py](./portSetup/portSetup.py) from [portSetup](./portSetup) and [tripodgait.py](./walking/tripodgait.py) from [walking](./walking) inside [main.py](./main.py) file.
* Inside [main.py](./main.py) file the module [walking](./walking) can be used to call forward, backward, turning and strafing walking movement functions.
* Sitting and standing can be found in [stableStance.py](./standing/stableStance.py) in module [standing](./standing). 
* Modules can be set to execute from [main.py](./main.py). Keyboard interrupt is possible to stop all actions and let the hexapod sit.

## Computer Vision OpenCV
To get the Yolo detector to work you will need run this command in your command line:
`python yolo_detector.py --yolo yolo-coco`

