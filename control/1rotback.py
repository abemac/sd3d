import pigpio
import steppers


pi=pigpio.pi()

quad= steppers.Quad(0x20,pi)

s = quad.getStepper(1)
#s.setSpeed()
s.rotate(-1)
s.barrier()
quad.close()

