import abc
import time
from threading import Thread
import queue
SPEED_VERY_FAST=300
SPEED_FAST=	225
SPEED_MEDIUM_FAST=175
SPEED_MEDIUM = 100
SPEED_MEDIUM_SLOW = 50
SPEED_SLOW=20
SPEED_VERY_SLOW=10



class _stepper:
	__metaclass__ = abc.ABCMeta;
	
	
	def __init__(self,pi,i2c):
		self.i2c=i2c;	
		self.pi=pi;
		self.ticksperrev=200;
		self.setSpeed(SPEED_MEDIUM);
		self.state=0;
		self.queue=queue.Queue()
		self._startWorkerThread()
		
	def setSpeed(self,rpm):
		self.delay=(60.0)/(rpm*self.ticksperrev);
		
	@abc.abstractmethod
	def update_GPIOs(self):
		"""implement this specific to each motor"""
		return;
	
		
	def _rotate_steps(self,numsteps):
		if(numsteps<0):
			for i in range (0,abs(numsteps)):
				self.state+=1
				if(self.state>=5):
					self.state=1;
				self.update_GPIOs()
				time.sleep(self.delay)		
		else:
			for i in range (0,abs(numsteps)):
				if(self.state<=1):
					self.state=5;
				self.state-=1
				self.update_GPIOs()
				time.sleep(self.delay)
				
	def _rotate_deg(self,degrees):
		steps=int(self.ticksperrev * (degrees/360.0))
		self._rotate_steps(steps)
		
	def _rotate_rot(self,rotations):
		steps=int(self.ticksperrev * rotations)
		self._rotate_steps(steps)
		
	def _rotate(self,rotations):
		self._rotate_rot(rotations)
	def rotate(self,rotations):
		self.queue.put(lambda: self._rotate(rotations))
	def _worker(self):
		while True:
			action = self.queue.get();
			action();
			self.queue.task_done()
	def _startWorkerThread(self):
		t = Thread(target=self._worker)
		t.daemon = True
		t.start()	
		
	def _off(self):
		self.state=0;
		self.update_GPIOs()

class Quad:
	IODIRA=0x00
	IODIRB=0x01
	OLATA=0x14
	OLATB=0x15
	OLATA_VAL=0x0
	OLATB_VAL=0x0
	def __init__(self,i2c_addr,pi):
		self.pi = pi;
		self.i2c = pi.i2c_open(1,i2c_addr)
		Quad.OLATA_VAL=0x0
		Quad.OLATB_VAL=0x0
		pi.i2c_write_byte_data(self.i2c,Quad.IODIRA,0x00) ;#Config IODIRA as all outputs
		pi.i2c_write_byte_data(self.i2c,Quad.IODIRB,0x00) ;#Config IODIRB as all outputs
		pi.i2c_write_byte_data(self.i2c,Quad.OLATA,0x00) ;#Set A outputs as 0
		pi.i2c_write_byte_data(self.i2c,Quad.OLATB,0x00) ;#Set B outputs as 0
		
		self.s1= self._stepper1(pi,self.i2c)
		self.s2= self._stepper2(pi,self.i2c)
		self.s3= self._stepper3(pi,self.i2c)
		self.s4= self._stepper4(pi,self.i2c)
		
	def close(self):
		self.pi.i2c_write_byte_data(self.i2c,Quad.OLATA,0x00) ;#Set A outputs as 0
		self.pi.i2c_write_byte_data(self.i2c,Quad.OLATB,0x00) ;#Set B outputs as 0
		self.pi.i2c_close(self.i2c)
		self.s1=None;
	
	def getStepper(self,num):
		if num==1:
			return self.s1
		elif num==2:
			return self.s2
		elif num==3:
			return self.s3
		elif num==4:
			return self.s4
		else:
			print ("num must be 1-4")
		
	class _stepper1(_stepper):
		
		def __init__(self,pi,i2c):
			super().__init__(pi,i2c)
			
		
		def update_GPIOs(self):
			if self.state==1:
				Quad.OLATB_VAL|=0b00001010
				Quad.OLATB_VAL&=0b11111010
			elif self.state==2:
				Quad.OLATB_VAL|=0b00000110
				Quad.OLATB_VAL&=0b11110110
			elif self.state==3:
				Quad.OLATB_VAL|=0b00000101
				Quad.OLATB_VAL&=0b11110101
			elif self.state==4:
				Quad.OLATB_VAL|=0b00001001
				Quad.OLATB_VAL&=0b11111001
			elif self.state==0:
				Quad.OLATB_VAL&=0b11110000
			self.pi.i2c_write_byte_data(self.i2c,Quad.OLATB,Quad.OLATB_VAL)
		
	class _stepper2(_stepper):
		
		def __init__(self,pi,i2c):
			super().__init__(pi,i2c)
			
		
		def update_GPIOs(self):
			if self.state==1:
				Quad.OLATB_VAL|=0b10100000
				Quad.OLATB_VAL&=0b10101111
			elif self.state==2:
				Quad.OLATB_VAL|=0b01100000
				Quad.OLATB_VAL&=0b01101111
			elif self.state==3:
				Quad.OLATB_VAL|=0b01010000
				Quad.OLATB_VAL&=0b01011111
			elif self.state==4:
				Quad.OLATB_VAL|=0b10010000
				Quad.OLATB_VAL&=0b10011111
			elif self.state==0:
				Quad.OLATB_VAL&=0b00001111
			self.pi.i2c_write_byte_data(self.i2c,Quad.OLATB,Quad.OLATB_VAL)
	
	class _stepper3(_stepper):
		
		def __init__(self,pi,i2c):
			super().__init__(pi,i2c)
		
		def update_GPIOs(self):
			if self.state==1:
				Quad.OLATA_VAL|=0b10100000
				Quad.OLATA_VAL&=0b10101111
			elif self.state==2:
				Quad.OLATA_VAL|=0b01100000
				Quad.OLATA_VAL&=0b01101111
			elif self.state==3:
				Quad.OLATA_VAL|=0b01010000
				Quad.OLATA_VAL&=0b01011111
			elif self.state==4:
				Quad.OLATA_VAL|=0b10010000
				Quad.OLATA_VAL&=0b10011111
			elif self.state==0:
				Quad.OLATA_VAL&=0b00001111
			self.pi.i2c_write_byte_data(self.i2c,Quad.OLATA,Quad.OLATA_VAL)
	
	class _stepper4(_stepper):
		
		def __init__(self,pi,i2c):
			super().__init__(pi,i2c)
			
		
		def update_GPIOs(self):
			if self.state==1:
				Quad.OLATA_VAL|=0b00001010
				Quad.OLATA_VAL&=0b11111010
			elif self.state==2:
				Quad.OLATA_VAL|=0b00000110
				Quad.OLATA_VAL&=0b11110110
			elif self.state==3:
				Quad.OLATA_VAL|=0b00000101
				Quad.OLATA_VAL&=0b11110101
			elif self.state==4:
				Quad.OLATA_VAL|=0b00001001
				Quad.OLATA_VAL&=0b11111001
			elif self.state==0:
				Quad.OLATA_VAL&=0b11110000
			self.pi.i2c_write_byte_data(self.i2c,Quad.OLATA,Quad.OLATA_VAL)
