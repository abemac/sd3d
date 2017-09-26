import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

motor_enable=25
motor_enable_2=21
motor_enable_btn=19
motor_1A=24
motor_2A=23
motor_3A=6
motor_4A=23
up=27
down=20
stop=5

GPIO.setup(motor_enable,GPIO.OUT)
GPIO.setup(motor_enable_2,GPIO.OUT)
GPIO.setup(motor_enable_btn,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(motor_1A,GPIO.OUT)
GPIO.setup(motor_2A,GPIO.OUT)
GPIO.setup(motor_3A,GPIO.OUT)
GPIO.setup(motor_4A,GPIO.OUT)
GPIO.output(motor_enable,0)
GPIO.setup(up,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(down,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(stop,GPIO.IN,GPIO.PUD_UP)
on=False;
direction="left"
duty=50
freq=100
p=GPIO.PWM(motor_enable,freq)

def spin_left():
	GPIO.output(motor_1A,1)
	GPIO.output(motor_2A,0)
def spin_right():
	GPIO.output(motor_1A,0)
	GPIO.output(motor_2A,1)

def onBtnPress(pinNum):
	global on,p,duty
	if(on):
		on=False
		p.stop()
	else:
		on=True
		spin_left()
		p=GPIO.PWM(motor_enable,freq)
		p.start(duty)
 
def fup(x):
	global duty,p
	if(duty<100):
		duty=duty+10
		p.ChangeDutyCycle(duty)
		print(duty)
def fdown(x):
	global duty,p
	if(duty>0):
		duty=duty-10
		p.ChangeDutyCycle(duty)
		print(duty)

def fstop(x):
	global direction
	if direction=="left":
		spin_right()
		direction="right"
	else:
		spin_left()
		direction="left"
	
		
GPIO.add_event_detect(motor_enable_btn,GPIO.FALLING,onBtnPress,300)
GPIO.add_event_detect(up,GPIO.FALLING,fup,300)
GPIO.add_event_detect(down,GPIO.FALLING,fdown,300)
GPIO.add_event_detect(stop,GPIO.FALLING,fstop,300)
spin_left();
input("asdf")	
