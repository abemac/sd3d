import pigpio
import steppers
import time
pi = pigpio.pi()

quad = steppers.Quad(0x20,pi)

s1 = quad.getStepper(1)
s1.setSpeed(steppers.SPEED_MEDIUM)
s1.rotate_deg(90)

s2 = quad.getStepper(2)
s2.setSpeed(500)
#s2.rotate(2)


input("press [Enter] to exit")
quad.close();

