import RPi.GPIO as GPIO
import time

class Stepper:
	OUTPUT_I2C=0
	OUTPUT_DIRECT=1
		
	def __init__(self,pin_1A,pin_2A,pin_3A,pin_4A,output_type):
		self.output_type=output_type;
		self.pin_1A=pin_1A;
		self.pin_2A=pin_2A;
		self.pin_3A=pin_3A;
		self.pin_4A=pin_4A;
		
		
	
	
