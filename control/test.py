import pigpio
import steppers
import time
pi = pigpio.pi()

quad = steppers.Quad(0x20,pi)


s1 = quad.getStepper(1)
s3 = quad.getStepper(3)



s1.rotate(1)
s1.rotate(-1)
#s1.off()
s1.barrier()


s3.rotate(1)
s3.rotate(-1)

quad.barrier()
input("press [Enter] to exit")
quad.close();
