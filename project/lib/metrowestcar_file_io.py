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
    def read_image_from_file(self, dirpath, trackname, filename):
        fullpath = dirpath + '\\' + trackname + '\\image\\' + filename
        image = Image.open(fullpath)
        numpy_image = np.array(image)
        return numpy_image

    def read_image_from_file_using_samplenumber(self, dirpath, trackname, samplenumber):
        filename = trackname + "_" + str(samplenumber) + '.jpg'     
        numpy_image = self.read_image_from_file(dirpath, trackname, filename)
        return numpy_image
    
    # read steering value from file
    # it is received as two bits and is low asserted!
    def read_steering_from_file(self, dirpath, trackname, filename):
        fullpath = dirpath + '\\' + trackname + '\\steer\\' + filename
        with open(fullpath, 'rt') as file:
            line = file.read()
            value = np.uint32(line)
            assert (value > 0) & (value < 800), "the steering value is invalid (" + line + "),(" + str(value) + ") --> " + fullpath
            return value

    def read_steering_from_file_using_samplenumber(self, dirpath, trackname, samplenumber):
        filename = trackname + "_" + str(samplenumber) + '.txt'      
        steering = self.read_steering_from_file(dirpath, trackname, filename)
        return steering
    
    
    # Get a list of "file numbers" within a directory
    #
    # Each image is paired with it's steering value
    # via a number in the file names:
    #    <track>/image/<track>_<NN>.jpg
    #    <track>/steer/<track>_<NN>.txt
    # The method returns a list of NNNs given a directory.
    import fnmatch
    import re
    def _get_sample_numbers(self, dirpath, trackname):
        fullpath = dirpath + '\\' + trackname + '\\steer\\'

        # get all the file names
        names1 = os.listdir(fullpath)
        
        # crop everything after "." then take whatever follows "_"
        names2 = [n.split(".", 1)[0] for n in names1]
        names3 = [n.split("_")[-1] for n in names2]

        return names3


    def read_images_from_directory_given_samplenumbers(self, dirpath, trackname, samplenumbers):
        
        # loop through the directories/files
        my_images = np.empty((0,self.image_h,self.image_w, self.image_d), np.uint8)
        
        for snum in samplenumbers:
            image = self.read_image_from_file_using_samplenumber(dirpath, trackname, snum)
            # add one dimension so the image so it can be appended
            image = image[np.newaxis]
            my_images = np.append(my_images, image, axis=0)
        return my_images

    def read_images_from_directory(self, dirpath, trackname):
        samplenumbers = self._get_sample_numbers(dirpath, trackname)
        images = self.read_images_from_directory_given_samplenumbers(dirpath, trackname, samplenumbers)
        return images
    
    def read_images_from_list_of_tracks(self, dirpath, tracklist):

        images = np.empty((0,self.image_h,self.image_w, self.image_d), np.uint8)
        # loop through the tracks
        for trackname in tracklist:
            print('loading images from ' + dirpath + "\\" + trackname)
            more_images = self.read_images_from_directory(dirpath, trackname)
            images = np.append(images, more_images, axis=0)
        return images
    
    def read_steerings_from_directory_given_samplenumbers(self, dirpath, trackname, samplenumbers):
        
        # loop through the directories/files
        my_steering = np.empty((0),np.uint32)
        
        for snum in samplenumbers:
            steering = self.read_steering_from_file_using_samplenumber(dirpath, trackname, snum) 
            my_steering = np.append(my_steering, steering)
        return my_steering

    def read_steerings_from_directory(self, dirpath, trackname):
        samplenumbers = self._get_sample_numbers(dirpath, trackname)
        steerings = self.read_steerings_from_directory_given_samplenumbers(dirpath, trackname, samplenumbers)
        return steerings
        
    def read_steerings_from_list_of_tracks(self, dirpath, tracklist):

        steerings = np.empty((0),np.uint32)
        # loop through the directories
        for trackname in tracklist:
            print('loading steerings from ' + dirpath + "\\" + trackname)
            more_steerings = self.read_steerings_from_directory(dirpath, trackname)
            steerings = np.append(steerings, more_steerings, axis=0)
        return steerings

