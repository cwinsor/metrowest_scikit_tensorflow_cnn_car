# This is the Metrowest Car dataset.
#
# It is a set of images taken from a toy
# car that is being driven on an track.
# Tape on the floor establishes the centerline
# of the track, and the intent is the car will
# be trained to follow this centerline.
#
# Each image is labeled with a steering
# direction, with a value of (left/center/right).
# This is the target variable of our dataset.
#
# The training dataset is <N> images, and the test dataset is <M> images.
# Images are 28x28 pixel, black and white.
#
# During collection the car is driven on
# the track in either a clockwise or counter-clockwise
# direction.  Image and steering are samples on a 0.5 sec
# period.  Steering direction is categorical with
# values of 0,1,2 representing left/center/right respectively.
#
# Data from several driving sessions is captured and
# saved to disk.  During capture the image is threshold-detected
# at the mean value.
#
# When creating the database the images are shuffled to remove
# the sequencing and it split into Training/Test partitions.
# The resulting datasets avoid a clockwise or counter-clockwise preference,
# and ensure all driving sessions are equally represented.
#
# Methods witin the Dataset class are:
#
# data() - allows user to get the dataset
#
# The class also provides methods to create the
# dataset from the raw file data.  This is intended
# for use when constructing the dataset, not regular use.
#

#from keras.datasets import mnist

import pickle

class Dataset(object):

    # get the data (user)
    @staticmethod
    def data():
        # example - mnist
        #(x_train, y_train), (x_test, y_test) = mnist.load_data()
        #return  (x_train, y_train), (x_test, y_test)
    
        file_full_path = "../data/dataset"
        with open(file_full_path, 'rb') as data:
            dataset_in = pickle.load(data)
        return dataset_in

        
