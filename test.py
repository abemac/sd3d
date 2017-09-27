from stepper import Stepper


import RPi.GPIO as GPIO
import time
import sys

if sys.version_info[0] < 3:
    raise "Must be using Python 3"

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
s.setSpeed(Stepper.SPEED_SLOW)
s.rotate_rot(5)
s.rotate_rot(-2)

GPIO.cleanup()
