import pigpio
import steppers


pi=pigpio.pi()

quad= steppers.Quad(0x20,pi)

s = quad.getStepper(1)
#s.setSpeed()
s.rotate(4)
s.barrier()
quad.close()

