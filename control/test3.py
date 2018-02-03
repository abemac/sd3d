import pigpio
import steppers
import time
pi = pigpio.pi()

quad = steppers.Quad(0x20,pi)

def rotsbymm(mm):
	mmperrot=47
	return mm/mmperrot

s = quad.getStepper(4)

speed=20
s.setSpeed(speed)
s.rotate(.25)
s.rotate(-.25)
s.rotate(.25)
s.rotate(-.25)
s.rotate(.25)
s.rotate(-.25)
s.rotate(.25)
s.rotate(-.25)
s.rotate(.25)
s.rotate(-.25)
s.rotate(.25)
s.rotate(-.25)
s.rotate(.25)
s.rotate(-.25)
s.rotate(.25)
s.rotate(-.25)


speed=50
s.setSpeed(speed)
s.rotate(.25)
s.rotate(-.25)
s.rotate(.25)
s.rotate(-.25)
s.rotate(.25)
s.rotate(-.25)
s.rotate(.25)
s.rotate(-.25)
s.rotate(.25)
s.rotate(-.25)
s.rotate(.25)
s.rotate(-.25)
s.rotate(.25)
s.rotate(-.25)
s.rotate(.25)
s.rotate(-.25)

speed=100
s.setSpeed(speed)
s.rotate(.25)
s.rotate(-.25)
s.rotate(.25)
s.rotate(-.25)
s.rotate(.25)
s.rotate(-.25)
s.rotate(.25)
s.rotate(-.25)
s.rotate(.25)
s.rotate(-.25)
s.rotate(.25)
s.rotate(-.25)
s.rotate(.25)
s.rotate(-.25)
s.rotate(.25)
s.rotate(-.25)



quad.barrier()
quad.close();
