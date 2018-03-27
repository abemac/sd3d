import pigpio
import time
pi=pigpio.pi()

pi.set_mode(23,pigpio.OUTPUT)
pi.set_mode(24,pigpio.INPUT)

pi.set_pull_up_down(23,pigpio.PUD_OFF)
pi.set_pull_up_down(24,pigpio.PUD_DOWN)
start,end=0,0
pi.write(23,0)
def echo(gpio,level,tick):
	global end,start
	end=tick
	print(str((end-start)/148.0/12.0 )+" feet")
def trigger(gpio,level,tick):
	global start
	start=tick
	
	
pi.callback(24,pigpio.FALLING_EDGE,echo)
pi.callback(23,pigpio.FALLING_EDGE,trigger)
time.sleep(.001)

while True:
	pi.gpio_trigger(23,10,1)
	time.sleep(1)
input("press enter to close\n")





