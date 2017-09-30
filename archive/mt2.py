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
motor_4A=12

GPIO.setup(motor_enable,GPIO.OUT)
GPIO.setup(motor_enable_2,GPIO.OUT)
GPIO.setup(motor_enable_btn,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(motor_1A,GPIO.OUT)
GPIO.setup(motor_2A,GPIO.OUT)
GPIO.setup(motor_3A,GPIO.OUT)
GPIO.setup(motor_4A,GPIO.OUT)
GPIO.output(motor_enable,1)
GPIO.output(motor_enable_2,1)



on=True;

def step_4 (p):
	if p==0:
		GPIO.output(motor_1A,0)
		GPIO.output(motor_2A,0)
		GPIO.output(motor_3A,0)
		GPIO.output(motor_4A,0)
	if p==1:
		GPIO.output(motor_1A,1)
		GPIO.output(motor_2A,0)
		GPIO.output(motor_3A,1)
		GPIO.output(motor_4A,0)
	if p==2:
		GPIO.output(motor_1A,0)
		GPIO.output(motor_2A,1)
		GPIO.output(motor_3A,1) 
		GPIO.output(motor_4A,0)
	if p==3:
		GPIO.output(motor_1A,0)
		GPIO.output(motor_2A,1)
		GPIO.output(motor_3A,0)
		GPIO.output(motor_4A,1)
	if p==4:
		GPIO.output(motor_1A,1)
		GPIO.output(motor_2A,0)
		GPIO.output(motor_3A,0)
		GPIO.output(motor_4A,1)
pas=1;
def steps_4(value):
	global pas
	if(value<0):
		for i in range (0,abs(value)):
			step_4(pas)
			time.sleep(.04)
			pas+=1
			if(pas>=5):
				pas=1;
	else:
		for i in range (0,abs(value)):
			step_4(pas)
			time.sleep(.04)
			if(pas==1):
				pas=5;
			pas-=1

start=time.time();
steps_4(200)
stop=time.time();
spr = stop-start
rps=1/spr
rpm=rps*60;
print (rpm)
step_4(0)
