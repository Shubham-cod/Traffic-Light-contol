# Project: Traffic Light System
# Author: Shubham Agarwal
# Date: 12/06/2020

#importing modules
import busio
import time
import board
import adafruit_pca9685

#defining function for Phase 1 operation
def SA_phase_1():
   # set first red LED on and second green LED on
   pca9685.channels[SA_trafficLight_0].duty_cycle = SA_onLED
   pca9685.channels[SA_trafficLight_5].duty_cycle = SA_onLED
   print("First Red LED is on")
   print("Second Green LED is on")
   time.sleep(3) # 3 seconds
   # set first red LED off and second green LED off
   pca9685.channels[SA_trafficLight_0].duty_cycle = SA_offLED
   pca9685.channels[SA_trafficLight_5].duty_cycle = SA_offLED
   return

#defining function for Phase 2 operation
def SA_phase_2():
   # set first red and yellow LED on and second yellow LED on
   pca9685.channels[SA_trafficLight_0].duty_cycle = SA_onLED
   pca9685.channels[SA_trafficLight_1].duty_cycle = SA_onLED
   pca9685.channels[SA_trafficLight_4].duty_cycle = SA_onLED
   print("First Red and Yellow LEDs are on")
   print("Second Yellow is on")
   time.sleep(3) # 3 seconds
   # set first red and yellow LED off and second yellow LED off
   pca9685.channels[SA_trafficLight_0].duty_cycle = SA_offLED
   pca9685.channels[SA_trafficLight_1].duty_cycle = SA_offLED
   pca9685.channels[SA_trafficLight_4].duty_cycle = SA_offLED
   return

#defining function for Phase 3 operation
def SA_phase_3():
   # set first green LED on and second red LED on
   pca9685.channels[SA_trafficLight_2].duty_cycle = SA_onLED
   pca9685.channels[SA_trafficLight_3].duty_cycle = SA_onLED
   print("First Green LED is on")
   print("Second Red LED is on")
   time.sleep(3) # 3 seconds
   # set first green LED off and second red LED off
   pca9685.channels[SA_trafficLight_2].duty_cycle = SA_offLED
   pca9685.channels[SA_trafficLight_3].duty_cycle = SA_offLED
   return

#defining function for Phase 4 operation
def SA_phase_4():
   #set first yellow LED on and second red and yellow led on
   pca9685.channels[SA_trafficLight_1].duty_cycle = SA_onLED
   pca9685.channels[SA_trafficLight_3].duty_cycle = SA_onLED
   pca9685.channels[SA_trafficLight_4].duty_cycle = SA_onLED
   print("First Yellow LED is on")
   print("Second Red and Yellow LED's are on")
   #set first yellow LED off and second red and yellow led off
   time.sleep(3) # 3 seconds   
   pca9685.channels[SA_trafficLight_1].duty_cycle = SA_offLED
   pca9685.channels[SA_trafficLight_3].duty_cycle = SA_offLED
   pca9685.channels[SA_trafficLight_4].duty_cycle = SA_offLED
   return

#defining function for setting off all LED's
def SA_allLEDsOff():
    #set off all LED's
    for trafficLightNr in range(6):
        pca9685.channels[trafficLightNr].duty_cycle = SA_offLED
    return

# Create the I2C bus interface.
i2c_bus = busio.I2C(board.SCL, board.SDA)

# Create a simple PCA9685 class instance.
pca9685 = adafruit_pca9685.PCA9685(i2c_bus)

# Set the PWM frequency to 60 Hz.
pca9685.frequency =    60

#defining required variables
SA_onLED             = 65535 # PWM duty cycle 100%
SA_offLED            =     0 # PWM duty cycle   0%
SA_trafficLight_0    =     0 # First traffic light Red
SA_trafficLight_1    =     1 # First traffic light Yellow
SA_trafficLight_2    =     2 # First traffic light Green
SA_trafficLight_3    =     3 # Second traffic light Red
SA_trafficLight_4    =     4 # Second traffic light Yellow
SA_trafficLight_5    =     5 # Second traffic light Green

#calling function to terminate program and set off all LED's
SA_allLEDsOff()
print("To finish press Ctrl C")

#calling all 4 phases on an infinite loop
try:
   while True:
       print()
       SA_phase_1()
       SA_phase_2()
       SA_phase_3()
       SA_phase_4()
except:
    print("finish")
    SA_allLEDsOff()
    
###########################################################    END    ##############################################################
