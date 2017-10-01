import pigpio
import steppers
import time
pi = pigpio.pi()

quad = steppers.Quad(0x20,pi)
s1 = quad.getStepper(4)
s1.setSpeed(300)
s1.rotate(5)
time.sleep(1)
s1.rotate(-5)

input("press [Enter] to exit")
quad.close();
