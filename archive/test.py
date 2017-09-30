from stepper import Stepper


import RPi.GPIO as GPIO
import time
import sys

if sys.version_info[0] < 3:
    print ("Must be using Python 3")
    sys.exit(1)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

motor_enable=25
motor_enable_2=21
motor_enable_btn=19

GPIO.setup(motor_enable,GPIO.OUT)
GPIO.setup(motor_enable_2,GPIO.OUT)
GPIO.setup(motor_enable_btn,GPIO.IN,GPIO.PUD_UP)

GPIO.output(motor_enable,1)
GPIO.output(motor_enable_2,1)



s = Stepper(24,23,6,12,Stepper.OUTPUT_DIRECT)
s.setSpeed(Stepper.SPEED_FAST)
s.rotate(5)
s.rotate(-2)
s.setSpeed(Stepper.SPEED_VERY_FAST)
s.rotate(-.5)
s.rotate(.5)
s.rotate(-.5)
s.rotate(.5)
s.rotate(-.5)
s.rotate(.5)
s.rotate(-.5)
s.rotate(.5)
s.rotate(-.5)
s.rotate(.5)
s.rotate(-.5)
s.rotate(.5)
s.rotate(-.5)
s.rotate(.5)
s.rotate(-.5)
s.rotate(.5)
s.rotate(-.5)
s.rotate(.5)
s.rotate(-.5)
s.rotate(.5)
s.rotate(-.5)
s.rotate(.5)
s.rotate(-.5)
s.rotate(.5)
s.rotate(-.5)


GPIO.cleanup()

