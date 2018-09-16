# This library provides classes
# for reading/writing to/from files.

import numpy as np
import fnmatch
import re

class FileReader(object):
    
    def __init__(self):
        self.data = [] 
            
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
                steering = 2
            elif line == "11":
                steering = 0
            elif line == "10":
                steering = 1
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
        my_images = np.empty((0,480,640,3),int)
        
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

        images = np.empty((0,480,640,3),int)
        # loop through the directories
        for dir_path in dir_list:
            print('loading from ' + dir_path)
            more_images = self.read_images_from_directory(dir_path)
            images = np.append(images, more_images, axis=0)
        return images
      
    def read_steering_from_directory_given_list(self, dir_path, list_of_file_numbers):

         # loop through the directories/files
        my_steering = np.empty((0),int)
        
        for fnum in list_of_file_numbers:
            steering = self.read_steering_from_file_using_filenumber(dir_path, fnum) 
            my_steering = np.append(my_steering, steering)
        return my_steering

    def read_steering_from_directory(self, dir_path):
        list_of_file_numbers = self._get_file_numbers(dir_path)
        steering = self.read_steering_from_directory_given_list(dir_path, list_of_file_numbers)
        return steering
        
    def read_steering_from_list_of_directories(self, dir_list):

        steerings = np.empty((0),int)
        # loop through the directories
        for dir_path in dir_list:
            print('loading from ' + dir_path)
            more_steerings = self.read_steering_from_directory(dir_path)
            steerings = np.append(steerings, more_steerings, axis=0)
        return steerings

        
        
# read images and control from files
# concatenate into a dataset
import os
import numpy as np
from PIL import Image
def get_data(subdir_base):

    subdir_list = [
#        'pictures_01_two_loops_left',
#        'pictures_02_three_loops_right',
#        'pictures_03_three_loops_left',
#        'pictures_04_four_loops_right',
        'pictures_test',
    ]

    my_dataset = {}    
    my_dataset['DESCR'] = """

        The dataset is 800 image and steering values from a toy
        car as it is driven around a track.  The track is a
        piece of white tape on a concrete floor. The steering values
        are the steering applied by the driver to keep the
        car on the track.

        The dictionary structure of the dataset is:

        "images" - A 4-dimensional numpy array of integers,
        of size (800, 480, 640, 3). The first dimension is the image
        number, the remaining are w=640 h=480 and 3 for RGB.

        "steering" - A 1-dimensional numpy array of integers
        of size (800).  The value is the direction the car is
        being steered at the time of the corresponding image.
        The values are "categorical"
        with 1=left, 3=straight 2=right.

        "target_names" - a list of values of the steering class [1, 3, 2]

        "DESCR" - an overview description of the dataset.
    """

    my_dataset['target_names'] = [1, 3, 2]


    # loop through the directories/files
    my_images = np.empty((0,480,640,3),int)
    my_control = np.empty((0),int)
    for subdir in subdir_list:
        print('loading from ' + subdir)
        filenumbers = get_file_numbers(subdir_base, subdir)
        for fnum in filenumbers:
            #print(f)

            filepath = os.path.join(subdir_base, subdir)

            filename = os.path.join(filepath, 'image' + str(fnum) + '.jpg')
            with Image.open(filename) as image:
                npa = np.asarray(image)
                npa = npa[np.newaxis]
                print(npa.shape)
                print(my_images.shape)
                my_images = np.append(my_images, npa, axis=0)

            filename = os.path.join(filepath, 'control' + str(fnum))
            with open(filename, 'rt') as file:
                line = file.read()
                if line == "01":
                    steering = 1
                elif line == "11":
                    steering = 3
                elif line == "10":
                    steering = 2
                else:
                    sys.exit("error - control data value of " + line + " is unexpected/invalid")
                    
            my_control = np.append(my_control, steering)

    my_dataset['images'] = my_images
    my_dataset['target'] = my_control

    print(type(my_dataset))
    print(my_dataset.keys())
    print('There are ' + str(len(my_dataset['images'])) + ' images')
    print('There are ' + str(len(my_dataset['target'])) + ' targets')
    
    print("The image array is a " + str(my_dataset['images'].shape) + " of " + str(type(my_dataset['images'])))
    print("The class array is a " + str(my_dataset['target'].shape) + " of " + str(type(my_dataset['target'])))
              
          
    
    #print(type(my_dataset['images']))
    #print(type(my_dataset['images'][0]))
    #print(my_dataset['images'][0].size)  # (width, height) tuple

    #print(my_dataset['target'][0])


    return my_dataset


# save to pickle file
import pickle
def save_to_pickle_file(filename):
    with open(filename, 'wb') as output:
        pickle.dump(my_dataset, output)
    

# restore from pickle file
import pickle
def restore_from_pickle_file(filename):
    with open(filename, 'rb') as data:
        dataset_in = pickle.load(data)

    print('There are ' + str(len(dataset_in['images'])) + ' samples')
    print(type(dataset_in))
    print(dataset_in.keys())
    print(dataset_in['images'][0].shape)

    return dataset_in

