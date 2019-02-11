
# references:
# https://media.readthedocs.org/pdf/picamera/pi-display/picamera.pdf
# https://picamera.readthedocs.io/en/release-1.10/recipes2.html#unencoded-image-capture-rgb-format
# https://www.raspberrypi.org/forums/viewtopic.php?t=107874

import picamera
import picamera.array
from gpiozero import InputDevice
from gpiozero import OutputDevice
from picamera import PiCamera
import keras
from keras import models

import time
from time import sleep
from time import time
import numpy as np
import os
import math
import my_globals as mygl

print("keras version " + keras.__version__)

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

print("left")
pin_l.off()
pin_r.on()
sleep(1.0)
            
print("right")
pin_l.on()
pin_r.off()
sleep(1.0)

print("center")
pin_l.on()
pin_r.on()
sleep(1.0)

i = 0
from PIL import Image

with picamera.PiCamera() as camera:

    # the camera rounds up to the next even multiple of 16 or 32 (height, width respectively)
    # so... pad upward, capture the larger image.  Later we will downsample 
    # see example media.readthedocs.org/pdf/picamera/latest/picamera.pdf 4.1
    CAM_HEIGHT =  (math.floor( (mygl.CAMERA_H - 1) / 16) + 1) * 16
    CAM_WIDTH  =  (math.floor( (mygl.CAMERA_W - 1) / 32) + 1) * 32

    #print(" CAMERA_H " + str(mygl.CAMERA_H) + " CAM_HEIGHT " + str(CAM_HEIGHT))
    #print(" CAMERA_W " + str(mygl.CAMERA_W) + " CAM_WIDTH  " + str(CAM_WIDTH))

    print("camera preview start")
    camera.resolution = (CAM_WIDTH, CAM_HEIGHT)
    camera.rotation = 180
    camera.start_preview()
    sleep(5)
    camera.stop_preview()
    print("camera preview is complete")

    print('CNN model start')

    save_dir = os.path.join(os.environ['PROJECT_HOME'], 'project/model/saved_models/')
    model_name = 'metrowest_keras_trained_model.h5'
    model_path = os.path.join(save_dir, model_name)

    # close the file if was earlier left open - see https://github.com/h5py/h5py/issues/332
    # print("model_path=" + str(model_path))
    # import h5py
    # f2 = h5py.File(model_path, 'w')
    # f2.close()
    # print("write closed")
    # sleep(1)
    # f2 = h5py.File(model_path, 'a')
    # f2.close()
    # print("all closed")
    # sleep(1)

    print("model_path=" + str(model_path))
    model = keras.models.load_model(model_path)
    print('CNN model load is complete')

    i = 0
    while True:

        image = np.empty((CAM_HEIGHT, CAM_WIDTH, 3), dtype=np.uint8)
        #camera.capture(image, 'rgb', use_video_port=True)
        camera.capture(image, 'rgb')

        #im = Image.fromarray(image, mode='RGB')
        #im.save('/home/pi/tempdir/image_' + str(i) + '_0.jpeg')

        image = image.reshape(CAM_HEIGHT, CAM_WIDTH, 3)   # necessary?

        #im = Image.fromarray(image, mode='RGB')
        #im.save('/home/pi/tempdir/image_' + str(i) + '_1.jpeg')

        image = image[0:mygl.CAMERA_H, 0:mygl.CAMERA_W, : ]  # here we should scale, not crop

        #im = Image.fromarray(image, mode='RGB')
        #im.save('/home/pi/tempdir/image_' + str(i) + '_2.jpeg')
        #i += 1

        # the CNN expects (was trained using) an array of float32 normalized images
        image = image.astype('float32')
        image /= 255
        image = image[np.newaxis, :]

        # predict direction of track (the desired steering direction)
        steering_out = model.predict(image)[0]
        s_max = np.where(steering_out==steering_out.max())
        s_index = s_max[0][0]

    
        # apply to GPIOs
        if s_index == 1:
            print("left")
            pin_l.off()
            pin_r.on()
        elif s_index == 2:
            print("right")
            pin_l.on()
            pin_r.off()
        elif s_index == 3:
            print("center")
            pin_l.on()
            pin_r.on()
        else:
            print("something wrong in prediction")
            #assert False, "something wrong in prediction %r" % s_index

        # hold for a bit
        #sleep(1.0)
        #pin_l.on()
        #pin_r.on()
    
