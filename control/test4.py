import pigpio
import steppers
import time
pi = pigpio.pi()

quad = steppers.Quad(0x20,pi)

def rotsbymm(mm):
	mmperrot=47
	return mm/mmperrot

s = quad.getStepper(4)

speed=150
s.setSpeed(speed)
s.rotate(rotsbymm(50))
s.rotate(rotsbymm(-50))
s.rotate(rotsbymm(50))
s.rotate(rotsbymm(-50))
s.rotate(rotsbymm(50))
s.rotate(rotsbymm(-50))
s.rotate(rotsbymm(50))
s.rotate(rotsbymm(-50))
s.rotate(rotsbymm(50))
s.rotate(rotsbymm(-50))
s.rotate(rotsbymm(50))
s.rotate(rotsbymm(-50))


quad.barrier()
quad.close();
