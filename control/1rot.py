import pigpio
import steppers


pi=pigpio.pi()

quad= steppers.Quad(0x20,pi)


z= quad.getStepper(2)
z.setSpeed(100)
z.rotate(4)
z.rotate(-4)
	
quad.barrier()
quad.close()

