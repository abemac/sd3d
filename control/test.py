import pigpio
import steppers
import time
pi = pigpio.pi()

quad = steppers.Quad(0x20,pi)

s2 = quad.getStepper(2)
s1 = quad.getStepper(1)
s3 = quad.getStepper(3)
s4 = quad.getStepper(4)


speed=150
s1.setSpeed(speed)
s2.setSpeed(speed)
s3.setSpeed(speed)
s4.setSpeed(speed)

s2.rotate(1)
s2.rotate(-1)
#s2.off();


s1.rotate(1)
s1.rotate(-1)
#s1.off()


s3.rotate(1)
s3.rotate(-1)


s4.rotate(1)
s4.rotate(-1)



s2.rotate(1)
s1.rotate(1)
s3.rotate(-1)
s4.rotate(-1)


s2.rotate(-1)
s1.rotate(1)
s3.rotate(1)
s4.rotate(-1)

s2.rotate(-1)
s1.rotate(-1)
s3.rotate(1)
s4.rotate(1)

quad.barrier()
input("press [Enter] to exit")
quad.close();
