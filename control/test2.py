import pigpio
import steppers
import time
pi = pigpio.pi()

quad = steppers.Quad(0x20,pi)


s1,s2,s3,s4 = quad.getSteppers()


speed=200
s1.setSpeed(speed)
s2.setSpeed(speed)
s3.setSpeed(speed)
s4.setSpeed(speed)


s1.rotate(10)
s2.rotate(10)
s3.rotate(10)
s4.rotate(10)

quad.barrier();	
s1.rotate(-5)
s1.barrier()

input("press [Enter] to exit")
quad.close();

