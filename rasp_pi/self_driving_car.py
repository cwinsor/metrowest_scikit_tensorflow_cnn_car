from gpiozero import InputDevice
from gpiozero import OutputDevice
from picamera import PiCamera
from time import sleep
from time import time
import numpy as np

# Self-driving car for Metrowest Machine Learning Group.
#
# This python file runs on the Pi. First it is used to
# collect image and directional data. The data is used for
# offline batch training of the CNN.
# Later this file is used to drive the car - 
# applying the trained CNN to the task of driving the car.

# The "train" switch selects mode:
# train=1  --> Pi captures image and captures left/right control signals at GPIO - data is written to file
# train=0  --> Pi captures image andi uses CNN to drive left/right control at GPIO
train = True

pin_left  = 26
pin_right = 13

if train == True:

	picturepath = '../data/picturesX'

	pin_l = InputDevice(pin_left,True)
	pin_r = InputDevice(pin_right,True)

	camera = PiCamera()
	camera.resolution = (64, 64)
	#  camera.framerate = 24
	camera.rotation = 180
	#  camera.raw_format='rgb'
	camera.start_preview()
	sleep(5)
	camera.stop_preview()
	
	i = 0
	loop_target_time = 0.5
	a = time()
	while True:
		pLeft = 0 if pin_l.value else 1
		pRigh = 0 if pin_r.value else 1
		pinvals = str(pLeft) + str(pRigh)
		print(pinvals)
		
		fb = open(picturepath + '/control%s' % i, 'a+')
		fb.write(pinvals) 
		fb.close()
		#  camera.capture(picturepath + '/image%s.jpg' % i, use_video_port=True)
		#  camera.capture(picturepath + '/image%s.jpg' % i)
		#  camera.capture(picturepath + '/image%s.jpg' % i, resize=(64, 64))
		camera.capture(picturepath + '/image%s.jpg' % i, resize=(64, 64), use_video_port=True)
		#  output = np.empty((64, 64, 3), dtype=np.uint8)
		#  camera.capture(output, 'rgb', use_video_port=True)
	
		i = i + 1
		
		b = time()
		consumed = b - a
		print("consumed " + str(consumed))
		#  remaining = loop_target_time - consumed
		#  if remaining > 0.0:
		#		sleep(remaining)
		# else:
		#		print("warning - loop of %f seconds exceeded the target of %f seconds" %(consumed, loop_target_time))
		a = b

if train == False:

	pin_l = OutputDevice(pin_left,True,True)
	pin_r = OutputDevice(pin_right,True,True)
	
	while True:
		print("center")
		pin_l.on()
		pin_r.on()
		sleep(1)

		print("right")
		pin_l.on()
		pin_r.off()
		sleep(1)

		print("center")
		pin_l.on()
		pin_r.on()
		sleep(1)
	
		print("left")
		pin_l.off()
		pin_r.on()
		sleep(1)

