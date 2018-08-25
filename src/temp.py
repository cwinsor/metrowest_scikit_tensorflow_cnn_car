from gpiozero import InputDevice
from gpiozero import OutputDevice
from picamera import PiCamera
from time import sleep
from time import time

train = True

pin_left  = 26
pin_right = 13

if train == True:

	pin_l = InputDevice(pin_left,True)
	pin_r = InputDevice(pin_right,True)

	camera = PiCamera()
    	camera.resolution = (640, 480)
    	camera.framerate = 24
	camera.rotation = 180
	camera.raw_format='rgb'
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
		
		fb = open('/home/pi/tempdir/pictures/control%s' % i, 'a+')
		fb.write(pinvals) 
		fb.close()
		camera.capture('/home/pi/tempdir/pictures/image%s.jpg' % i, use_video_port=True)
	
		i = i + 1
		
		b = time()
		consumed = b - a
		remaining = loop_target_time - consumed
		if remaining > 0.0:
			sleep(remaining)
		else:
			print("warning - loop of %f seconds exceeded the target of %f seconds" %(consumed, loop_target_time))
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

