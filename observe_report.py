# Waits for motion
# Takes pictures (w/ flash) ever x seconds when motion is detected

# Alan Ness 
# https://github.com/Avidness

from sense_hat import SenseHat
from gpiozero import MotionSensor
import time
import led_images
import camera

sense = SenseHat()
mot = MotionSensor(4)
sense.set_rotation(180)
time_since_pic = 0
pic_interval = 10
pic_count = 0

while True:
	if mot.motion_detected:
		# Yes motion
		sense.set_pixels(led_images.green_dot)

		# Take a pic every x seconds
		if time_since_pic == 0 or time_since_pic >= pic_interval:
			imagepath = 'public/photo' + str(pic_count) + '.jpg'
			pic_count += 1
			sense.set_pixels(led_images.flash)
			camera.take_photo(imagepath)
			sense.set_pixels(led_images.green_dot)
			# Reset counter
			time_since_pic = 0
	else: 
		# No motion
		sense.set_pixels(led_images.red_dot)
		time_since_pic = pic_interval

	# Keep the clock ticking
	time.sleep(1)
	time_since_pic += 1
