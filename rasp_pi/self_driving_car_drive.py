from gpiozero import InputDevice
from gpiozero import OutputDevice
from picamera import PiCamera
from time import sleep
from time import time
import numpy as np

# Self-driving car for Metrowest Machine Learning Group.
#
# This python file runs on the Pi to drive the car.
#
# Images are captured from the front-facing camera.
# In realtime the CNN predicts the direction the
# track is heading.
#
# Based on predicted direction of track - a steering
# direction is applied to steering GPIO pins to
# steer the car.

pin_left  = 26
pin_right = 13

pin_l = OutputDevice(pin_left,True,True)
pin_r = OutputDevice(pin_right,True,True)

camera = PiCamera()
camera.resolution = (64, 64)
#  camera.framerate = 24
camera.rotation = 180
#  camera.raw_format='rgb'
camera.start_preview()
sleep(5)
camera.stop_preview()



while True:
    
    # capture image
    camera.capture(image, resize=(64, 64), use_video_port=True)

    # the CNN expects (was trained using) an array of float32 normalized images
    image = image.astype('float32')
    image /= 255
    image = image[np.newaxis, :]

    # predict direction of track (the desired steering direction)
    steering_out = model.predict(image)
    print(steering_out)

    # apply to GPIOs
    s_max = np.where(steering_out==steering_out.max())
    s_index = s_max[0][0]
    if s_index == 0:
        print("left")
        pin_l.off()
        pin_r.on()
    elif s_index == 1:
        print("center")
        pin_l.on()
        pin_r.on()
    elif s_index == 2:
        print("right")
        pin_l.on()
        pin_r.off()
    else:
        assert False, "something wrong in prediction %r" % s_index

    # hold for 0.5 sec - then release to center
    sleep(0.5)
    pin_l.on()
    pin_r.on()
    
    