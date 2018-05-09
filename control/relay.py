import pigpio
import sys
pi=pigpio.pi()

pi.set_mode(4,pigpio.OUTPUT)
pi.set_mode(17,pigpio.OUTPUT)

if sys.argv[1]=="open":
	pi.write(4,1)
	pi.write(17,0)
elif sys.argv[1]=="close":
	pi.write(4,0)
	pi.write(17,0)
