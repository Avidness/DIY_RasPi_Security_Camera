# crontab -e
# @reboot python /home/pi/projects/RaspberryPi-Peripherals/sense_led_status.py

from sense_hat import SenseHat
from gpiozero import MotionSensor
import time

sense = SenseHat()
mot = MotionSensor(4)

red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
mix = [255,0,100]
white = [255,255,255]
blank = [0.0,0]

def blink(x, y):
	sense.clear(0,0,0)
	if mot.motion_detected:
		sense.set_pixel(y, x, mix)
	else:
		sense.set_pixel(y, x, red)
	time.sleep(.1)

def scan():
	go_right = True
	go_down = True

	while True:
		for x in reversed(range(8)) if go_down else range(8):
			for y in reversed(range(8)) if go_right else range(8):
				blink(x, y)
			go_right = not go_right
		go_down = not go_down

scan()
