import pigpio
import steppers
import time
pi = pigpio.pi()

quad = steppers.Quad(0x20,pi)

s = quad.getStepper(1)

speed=50
s.setSpeed(speed)

s.rotate(1)
s.rotate(-1)
quad.barrier()
input("press [Enter] to exit")
quad.close();
