from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.image_effect = 'hatch'
camera.awb_mode = 'sunlight'
camera.vflip = True
camera.hflip = True

camera.start_preview()

while True:
				sleep(10)

#sleep(10)
#camera.stop_preview()
