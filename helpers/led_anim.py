# Animations for the sensehat 8x8 led grid

# Alan Ness
# https://github.com/Avidness

from sense_hat import SenseHat
import led_images as images
import time
import random

sense = SenseHat()

def cat_blink():
	set_img(images.cat_eyes_closed, .5)
	set_img(images.cat_eyes_half, .1)
	set_img(images.cat_eyes_open, .5)
	set_img(images.cat_eyes_half, .1)
	set_img(images.cat_eyes_closed, .5)

def crab_walk():
	set_img(images.crab_start, .25)
	set_img(images.crab_end, .25)

def look():
	set_img(images.eye_default, .1)
	set_img(random_eye(), .5)

def random_eye():
	eye_positions = [ images.eye_default, images.eye_left, images.eye_right, images.eye_up, images.eye_down, images.eye_left_down, images.eye_left_up, images.eye_right_up, images.eye_right_down ]
	return random.choice(eye_positions)

def scan():
				#	set_img(images.eye_default, .1)
	set_img(images.eye_right, .5)
	set_img(images.eye_default, .1)
	set_img(images.eye_left, .5)
	set_img(images.eye_default, .1)

def set_img(image, wait_time):
	sense.set_pixels(image)
	sense.flip_v()
	time.sleep(wait_time)
