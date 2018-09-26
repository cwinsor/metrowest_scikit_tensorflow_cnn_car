# This is the Metrowest Car dataset
# Data is 28x28 black/white images
# paired with steering data.
#
# It is split into test/training subsets
# with <N> test and <M> training instances
#
# The "data()" method allows user to get the dataset
#
# The class also provides methods to create the
# dataset from the raw file data.  This is intended
# for use when constructing the dataset, not regular use.
#

import numpy as np
import fnmatch
import re
import pickle
from keras.datasets import mnist

class Dataset(object):

    # get the data (user)
    @staticmethod
    def data():
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        return  (x_train, y_train), (x_test, y_test)
    
#    # save to pickle file
#    def save_to_pickle_file(filename):
#    with open(filename, 'wb') as output:
#        pickle.dump(my_dataset, output)
#        
#    # restore from pickle file
#    def restore_from_pickle_file(filename):
#    with open(filename, 'rb') as data:
#        dataset_in = pickle.load(data)
#
#    print('There are ' + str(len(dataset_in['images'])) + ' samples')
#    print(type(dataset_in))
#    print(dataset_in.keys())
#    print(dataset_in['images'][0].shape)
#
#    return dataset_in

