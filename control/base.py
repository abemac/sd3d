import pigpio
import steppers


pi=pigpio.pi()

quad= steppers.Quad(0x27,pi)
quad2=steppers.Quad(0x20,pi)

b1,b2,b3,b4= quad.getSteppers()
rotation,r,updown,filament = quad2.getSteppers()
SPEED=steppers.SPEED_SLOW
b1.setSpeed(SPEED)
b2.setSpeed(SPEED)
b3.setSpeed(SPEED)
b4.setSpeed(SPEED)
rotation.setSpeed(35)
r.setSpeed(40)
updown.setSpeed(100)
filament.setSpeed(60)
updown.rotate(2)
#filament.rotate(-1)
#r.rotate(-1)
#b1.rotate(1)
#b2.rotate(1)
#b3.rotate(1)
#b4.rotate(1)
#quad.barrier()
#b1.rotate(1.75)
#b2.rotate(1.75)
#b3.rotate(1.75)
#b4.rotate(1.75)

#quad.barrier()
#b1.rotate(3)
#b2.rotate(-3)
#b3.rotate(-3)
#b4.rotate(3)

quad.barrier()
quad2.barrier()
quad.close()
quad2.close()

