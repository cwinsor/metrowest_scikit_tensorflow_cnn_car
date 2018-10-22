# This library provides classes
# to handle the display

# The class is used to draw a single
# images on screen
from PIL import Image, ImageDraw
import os
import time
import numpy as np

class Displayer():
    
    def __init__(self):
        self.data = []
    
    def display_image(self, image_as_numpy_array):
        im = Image.fromarray(np.uint8(image_as_numpy_array))
        im.show()
        return
    
    def display_thumbnail(self, image_as_numpy_array):
        im = Image.fromarray(np.uint8(image_as_numpy_array))
        size = 32, 32
        im.thumbnail(size)
        im.show()
        return
    
    def display_resized(self, image_as_numpy_array, width, height):
        im = Image.fromarray(np.uint8(image_as_numpy_array))
        im = im.resize((width, height), Image.ANTIALIAS)
        im.show()
        return   
        
    def _draw_pointer_on_image(self, draw, im_h, im_w, direction):
        
        # establish 4 points and pointers... format for line sequence is is [(x,y),(x,y)...]
        high  =  (im_w/2,    im_h/4)
        left  =  (im_w/4,    im_h/2)
        right =  (im_w*3/4,  im_h/2)
        low   =  (im_w/2,    im_h*3/4)
        pointer_left     = [low, left, high]
        pointer_straight = [left, high, right]
        pointer_right    = [high, right, low]
        pointer_box      = [high, right, low, left, high]

        if direction == 1:
            pointer = pointer_left
        elif direction == 2:
            pointer = pointer_right
        elif direction == 3:
            pointer = pointer_straight
        else:
            pointer = pointer_box

        draw.line(pointer)
        return

    def display_annotated_image(self, image_as_numpy_array, direction):
        im = Image.fromarray(np.uint8(image_as_numpy_array))
        draw = ImageDraw.Draw(im)        
        self._draw_pointer_on_image(draw, im.size[1], im.size[0], direction)
        im.show()
        return
            
    def display_annotated_thumbnail(self, image_as_numpy_array, direction):
        im = Image.fromarray(np.uint8(image_as_numpy_array))
        size = 128, 128
        im.thumbnail(size)
        draw = ImageDraw.Draw(im)        
        self._draw_pointer_on_image(draw, im.size[1], im.size[0], direction)
        im.show()
        return


