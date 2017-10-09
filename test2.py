import pigpio
import steppers
import time
pi = pigpio.pi()

quad = steppers.Quad(0x20,pi)

s1 = quad.getStepper(1)
s1.setSpeed(steppers.SPEED_MEDIUM)
s1.rotate(5)

s1.barrier()
s1.setSpeed(steppers.SPEED_VERY_FAST)
s1.rotate(-5)
s1.barrier()

input("press [Enter] to exit")
quad.close();

