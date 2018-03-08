import pigpio
import steppers


pi=pigpio.pi()

quad= steppers.Quad(0x20,pi)

r = quad.getStepper(1)
r.setSpeed(40)
r.rotate(1)
r.rotate(-1)
r.rotate(1)
r.rotate(-1)
r.rotate(1)
r.rotate(-1)
r.setSpeed(80)
r.rotate(.5)
r.rotate(-.5)
r.rotate(.5)
r.rotate(-.5)
r.rotate(1)
r.rotate(-1)
r.rotate(1)
r.rotate(-1)

z= quad.getStepper(2)
z.setSpeed(80)
z.rotate(.5)
z.rotate(-.5)
z.rotate(.5)
z.rotate(-.5)
z.rotate(.5)
z.rotate(-.5)
z.rotate(.5)
z.rotate(-.5)
z.rotate(1)
z.rotate(-1)
z.rotate(1)
z.rotate(-1)
z.rotate(2)
z.rotate(-2)
z.rotate(4)
z.rotate(-4)
	
quad.barrier()
quad.close()

