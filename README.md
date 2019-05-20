# THE ABILITIES OF THE HEXAPOD

## Movements
**The hexapod is equipped with the following walking functionalities:**
Markup : * Forward movement
		 * Backward movement
 		 * Turn 90° left movement
  		 * Turn 90° right movement
		 * Strafing left movement

**Good to know:**
Markup : * Every walking movement uses the tripod gait fully. 
		 * Exceptions are when sitting and standing. 
		 * Turns will not be taken with stationary legs.

## Files
Modules are made for the hexapod. Every module is a grouped up set of actions that describe a broader functionality.(e.g. portSetup, standing, walking)

**Modules:**
Markup : * Declare the port in 1 go from file [tripodgait.py](./walking/tripodgait.py) in module 
		   [walking](./walking). Forward, backward, turning and strafing walking movements can also be found 		        		   in the same file.
		 * Sitting and standing can be found in [stableStance.py](./standing/stableStance.py) in module 		                          		   [standing](./standing). 
		 * Modules can be set to execute from [main.py](./main.py). Keyboard interrupt interups all actions 		    	       and lets the hexapod sit.
		 