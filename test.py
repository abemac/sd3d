import pigpio
import steppers
import time
pi = pigpio.pi()

quad = steppers.Quad(0x20,pi)
s1 = quad.getStepper(1)
s1.setSpeed(50)
s1.rotate(2)
time.sleep(1)
s1.rotate(-2)

input("press [Enter] to exit")
quad.close();
