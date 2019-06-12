# THE ABILITIES OF THE HEXAPOD

## Movements
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

## Files
Modules are made for the hexapod. Every module is a grouped up set of actions that describe a broader functionality.(e.g. portSetup, standing, walking)

**Modules:**
All modules are imported inside [main.py](./main.py). Here is where the main work is done.
* Ports are initialized by importing [portSetup.py](./portSetup/portSetup.py) from [portSetup](./portSetup) and [tripodgait.py](./walking/tripodgait.py) from [walking](./walking) inside [main.py](./main.py) file.
* Inside [main.py](./main.py) file the module [walking](./walking) can be used to call forward, backward, turning and strafing walking movement functions.
* Sitting and standing can be found in [stableStance.py](./standing/stableStance.py) in module [standing](./standing). 
* Modules can be set to execute from [main.py](./main.py). Keyboard interrupt is possible to stop all actions and let the hexapod sit.

# Hexapod-PRO78
To get the Yolo detector to work you will need to download the following [zip file](https://drive.google.com/open?id=1PMZW4vWV5GoeFPflUKIzErvv4S2NUkbg).
If you have downloaded this zip file extract it and you will need to put it in the **src folder**.

Now you can run the program by executing the following command:

`python yolo_detector.py --yolo yolo-coco`
