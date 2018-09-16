# a library that loads the auto-driving car dataset
# the primary function to use is get_data()
# which loads the data from the raw files and returns
# a dictionary with the dataset.
#
# but there are also functions to save
# and restore the dataset using Pickle


# Get a list of "file numbers" within a directory
# files are named using a numbering scheme where the
# image file is paired with the control file based
# a "file number"
#    controlNNN.txt
#    imageNNN.jpg
# The routine returns a list of NNNs
import fnmatch
import re
def get_file_numbers(basedir, subdir):
    fullpath = os.path.join(basedir, subdir)
    # get all the file names
    names = os.listdir(fullpath)
    # filter to get a list of just the "control" files
    bar = fnmatch.filter(names, "control*")
    # use regular expression to get just the NNN part of the name
    m = [re.search('\d+', b).group(0) for b in bar]
    # convert to integer from string
    m = [ int(x) for x in m ]
    return m


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
                #print(npa.shape)
                #print(my_images.shape)
                my_images = np.append(my_images, npa, axis=0)

            filename = os.path.join(filepath, 'control' + str(fnum))
            with open(filename, 'rt') as file:
                line = file.read()
                if line == "01":
                    direction = 1
                elif line == "11":
                    direction = 3
                elif line == "10":
                    direction = 2
                else:
                    sys.exit("error - control data value of " + line + " is unexpected/invalid")
                    
            my_control = np.append(my_control, direction)

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

