import pigpio
import steppers
pi = pigpio.pi()

quad = steppers.Quad(0x20,pi)
s1 = quad.getStepper(1)
s1.setSpeed(steppers.SPEED_FAST)
s1.rotate(1)
input("press [Enter] to exit")
quad.close();
