import RPi.GPIO as GPIO
import time

class Stepper:
	OUTPUT_I2C=0
	OUTPUT_DIRECT=1
	
	SPEED_VERY_FAST=.002  #about 140 rpm
	SPEED_FAST=	.0025	  #about 115 rpm
	SPEED_MEDIUM_FAST=.003     #about 95 rpm
	SPEED_MEDIUM = .005    #about 60 rpm
	SPEED_MEDIUM_SLOW = .01  #about 30 rpm
	SPEED_SLOW=.02 			#about 15 rpm
	SPEED_VERY_SLOW=.04     #about 7 rpm
	
	def __init__(self,pin_1A,pin_2A,pin_3A,pin_4A,output_type,stepsperrev=200):
		self.output_type=output_type;
		self.pin_1A=pin_1A;
		self.pin_2A=pin_2A;
		self.pin_3A=pin_3A;
		self.pin_4A=pin_4A;
		self.speed = Stepper.SPEED_MEDIUM;
		self.ticksperrev = stepsperrev;
		self.state=0;
		GPIO.setup(pin_1A,GPIO.OUT)
		GPIO.setup(pin_2A,GPIO.OUT)
		GPIO.setup(pin_3A,GPIO.OUT)
		GPIO.setup(pin_4A,GPIO.OUT)
		
	def setSpeed(self,speed):
		self.speed = speed;
	
	def update_GPIOs (self):
		if self.state==1:
			GPIO.output(self.pin_1A,1)
			GPIO.output(self.pin_2A,0)
			GPIO.output(self.pin_3A,1)
			GPIO.output(self.pin_4A,0)
		elif self.state==2:
			GPIO.output(self.pin_1A,0)
			GPIO.output(self.pin_2A,1)
			GPIO.output(self.pin_3A,1) 
			GPIO.output(self.pin_4A,0)
		elif self.state==3:
			GPIO.output(self.pin_1A,0)
			GPIO.output(self.pin_2A,1)
			GPIO.output(self.pin_3A,0)
			GPIO.output(self.pin_4A,1)
		elif self.state==4:
			GPIO.output(self.pin_1A,1)
			GPIO.output(self.pin_2A,0)
			GPIO.output(self.pin_3A,0)
			GPIO.output(self.pin_4A,1)
		elif self.state==0:
			GPIO.output(self.pin_1A,0)
			GPIO.output(self.pin_2A,0)
			GPIO.output(self.pin_3A,0)
			GPIO.output(self.pin_4A,0)
	
	def rotate_steps(self,numsteps):
		if(numsteps<0):
			for i in range (0,abs(numsteps)):
				self.state+=1
				if(self.state>=5):
					self.state=1;
				self.update_GPIOs()
				time.sleep(self.speed)		
		else:
			for i in range (0,abs(numsteps)):
				if(self.state<=1):
					self.state=5;
				self.state-=1
				self.update_GPIOs()
				time.sleep(self.speed)
				
	def rotate_deg(self,degrees):
		steps=int(self.ticksperrev * (degrees/360.0))
		self.rotate_steps(steps)
	def rotate_rot(self,rotations):
		steps=int(self.ticksperrev * rotations)
		self.rotate_steps(steps)
	def rotate(self,rotatons):
		self.rotate_rot(rotatons)
