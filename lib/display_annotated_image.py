# The class is used to draw images with an arrow
# indicating the direction of steering.
# Constructor takes in a numpy dataset with image and
# steering arrays.
# The method display_example() function takes an index
# to those arrays and draws the annotated image on screen.

# The method uses PIL (Pillow) to draw lines forming
# the left/right arrow.
from PIL import Image, ImageDraw
import os
import time

class DisplayAnnotatedImages:

def __init__(self, dataset):
    self.data = []
    self.my_dataset = dataset
    
def display_example(self, img_num):
    i_ndarray = my_dataset['images'][img_num]
    #print(type(i_ndarray))
    im = Image.fromarray(i_ndarray)
    #size = 128, 128
    #im.thumbnail(size)

    draw = ImageDraw.Draw(im)

    # establish 4 points and pointers... format for line sequence is is [(x,y),(x,y)...]
    hig   =  (im.size[0]/2,    im.size[1]/4)
    left  =  (im.size[0]/4,    im.size[1]/2)
    right =  (im.size[0]*3/4,  im.size[1]/2)
    low   =  (im.size[0]/2,    im.size[1]*3/4)
    pointer_left     = [low, left, high]
    pointer_straight = [left, high, right]
    pointer_right    = [high, right, low]
    pointer_box      = [high, right, low, left, high]

    steering = my_dataset['target'][img_num] 
    if steering == "left":
        pointer = pointer_left
    elif steering == "right":
        pointer = pointer_right
    elif steering == "straight":
        pointer = pointer_straight
    else:
        pointer = pointer_box
 
    draw.line(pointer)
    im.show()
    