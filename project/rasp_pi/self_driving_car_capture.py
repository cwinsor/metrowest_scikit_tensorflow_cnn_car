from gpiozero import InputDevice
from gpiozero import OutputDevice
from picamera import PiCamera
from time import sleep
from time import time
import numpy as np
from datetime import datetime
import os

# Self-driving car for Metrowest Machine Learning Group.
#
# This python file runs on the Pi to collect data.
#
# The file captures the steering values of a human
# driver and saves these along with images from the
# front-facing camera.  The raw data is saved to flatfile.
#
# left/right control signals come in on GPIO pins.  The
# camera is the standard Raspberry Pi

pin_left  = 26
pin_right = 13

timestamp = str(datetime.today()).split()
savepath = '../data_raw/' + timestamp[0] + "-" + timestamp[1]
os.makedirs(savepath)

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
	
	fb = open(savepath + '/control%s' % i, 'a+')
	fb.write(pinvals) 
	fb.close()

	camera.capture(savepath + '/image%s.jpg' % i, resize=(64, 64), use_video_port=True)

	i = i + 1

	b = time()
	consumed = b - a
	print("consumed " + str(consumed))
	remaining = loop_target_time - consumed
	if remaining > 0.0:
		sleep(remaining)
	else:
		print("warning - loop of %f seconds exceeded the target of %f seconds" %(consumed, loop_target_time))
	a = b
