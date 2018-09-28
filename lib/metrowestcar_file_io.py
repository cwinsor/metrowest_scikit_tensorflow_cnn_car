# This library provides classes
# for reading/writing to/from files.

import numpy as np
import fnmatch
import re
from PIL import Image
import os



class FileReader(object):
    
    image_h = 0
    image_w = 0
    image_d = 0
    
    def __init__(self, h, w, d):
        self.data = [] 
        self.image_h = h
        self.image_w = w
        self.image_d = d
            
    # read an image from file
    # image is read and converted to numpy array
    def read_image_from_file(self, full_path):
        image = Image.open(full_path)
        numpy_image = np.array(image)
        return numpy_image

    def read_image_from_file_using_filenumber(self, dir_path, file_number):
        filename = os.path.join('image' + str(file_number) + '.jpg')
        full_path = os.path.join(dir_path, filename)        
        numpy_image = self.read_image_from_file(full_path)
        return numpy_image
    
    # read steering value from file
    # it is received as two bits and is low asserted!
    def read_steering_from_file(self, full_path):
        with open(full_path, 'rt') as file:
            line = file.read()
            if line == "01":
                steering = np.uint8(2)
            elif line == "11":
                steering = np.uint8(0)
            elif line == "10":
                steering = np.uint8(1)
            else:
                sys.exit("error - steering data value of " + line + " is unexpected/invalid" + "file=" + full_path)
        return steering


    def read_steering_from_file_using_filenumber(self, dir_path, file_number):
        filename = os.path.join('control' + str(file_number))
        full_path = os.path.join(dir_path, filename)        
        steering = self.read_steering_from_file(full_path)
        return steering
    
    
    # Get a list of "file numbers" within a directory
    #
    # Each image is paired with it's steering value
    # via a number in the file names:
    #    steeringNNN.txt
    #    imageNNN.jpg
    # The method returns a list of NNNs given a directory.
    import fnmatch
    import re
    def _get_file_numbers(self, fullpath):
        ### snipped ->  fullpath = os.path.join(basedir, subdir)
        # get all the file names
        names = os.listdir(fullpath)
        # filter to get a list of just the "steering" files
        bar = fnmatch.filter(names, "control*")
        # use regular expression to get just the NNN part of the name
        m = [re.search('\d+', b).group(0) for b in bar]
        # convert to integer from string
        m = [ int(x) for x in m ]
        
        self.list_of_file_numbers = m
        return m


    def read_images_from_directory_given_list(self, dir_path, list_of_file_numbers):

         # loop through the directories/files
        my_images = np.empty((0,self.image_h,self.image_w, self.image_d), np.uint8)
        
        for fnum in list_of_file_numbers:
            image = self.read_image_from_file_using_filenumber(dir_path, fnum)
            # add one dimension so the image so it can be appended
            image = image[np.newaxis]
            my_images = np.append(my_images, image, axis=0)
        return my_images


    def read_images_from_directory(self, dir_path):
        list_of_file_numbers = self._get_file_numbers(dir_path)
        images = self.read_images_from_directory_given_list(dir_path, list_of_file_numbers)
        return images
        
        
    def read_images_from_list_of_directories(self, dir_list):

        images = np.empty((0,self.image_h,self.image_w, self.image_d), np.uint8)
        # loop through the directories
        for dir_path in dir_list:
            print('loading images from ' + dir_path)
            more_images = self.read_images_from_directory(dir_path)
            images = np.append(images, more_images, axis=0)
        return images
      
    def read_steering_from_directory_given_list(self, dir_path, list_of_file_numbers):

         # loop through the directories/files
        my_steering = np.empty((0),np.uint8)
        
        for fnum in list_of_file_numbers:
            steering = self.read_steering_from_file_using_filenumber(dir_path, fnum) 
            my_steering = np.append(my_steering, steering)
        return my_steering

    def read_steering_from_directory(self, dir_path):
        list_of_file_numbers = self._get_file_numbers(dir_path)
        steering = self.read_steering_from_directory_given_list(dir_path, list_of_file_numbers)
        return steering
        
    def read_steering_from_list_of_directories(self, dir_list):

        steerings = np.empty((0),np.uint8)
        # loop through the directories
        for dir_path in dir_list:
            print('loading steering from ' + dir_path)
            more_steerings = self.read_steering_from_directory(dir_path)
            steerings = np.append(steerings, more_steerings, axis=0)
        return steerings

      