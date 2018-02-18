# sudo crontab -e
# @reboot python /home/pi/projects/RaspberryPi-Peripherals/led_motion_img.py

from sense_hat import SenseHat
from gpiozero import MotionSensor
from helpers import led_anim

sense = SenseHat()
mot = MotionSensor(4)

def scan():
	while True:
		if mot.motion_detected:
			led_anim.look()
		else:
			led_anim.scan()

scan()
