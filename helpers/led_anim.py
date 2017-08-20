# Animations for the sensehat 8x8 led grid

# Alan Ness
# https://github.com/Avidness

import led_images

def cat_blink():
  sense.set_pixels(led_images.cat_eyes_closed)
	time.sleep(.5)
	sense.set_pixels(led_images.cat_eyes_half)
	time.sleep(.1)
	sense.set_pixels(led_images.cat_eyes_open)
	time.sleep(.5)
	sense.set_pixels(led_images.cat_eyes_half)
	time.sleep(.1)
	sense.set_pixels(led_images.cat_eyes_closed)
	time.sleep(.5)

def crab_walk():
	sense.set_pixels(crab1)
	time.sleep(.25)
	sense.set_pixels(crab2)
	time.sleep(.25)
