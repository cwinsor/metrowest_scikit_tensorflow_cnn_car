import pickle
from keras.datasets import mnist
from metrowestcar_file_io import FileReader

from os import getcwd
from os.path import abspath
from os.path import join
import numpy as np


class DatasetArchitect(object):

    
    def describe_dataset(self, dataset):
        print(type(dataset))
        print(dataset.keys())
        print('There are ' + str(len(dataset['images'])) + ' images')
        print('There are ' + str(len(dataset['target'])) + ' targets')

        print("The image array is a " + str(dataset['images'].shape) + " of " + str(type(dataset['images'])))
        print("The class array is a " + str(dataset['target'].shape) + " of " + str(type(dataset['target'])))
        return
    
    def read_raw_data_from_files(self):

        # the original raw data files are in...
        dir_list = [
            join(abspath(getcwd()), "../data/picturesX"),
            join(abspath(getcwd()), "../data/picturesX"),
        ]

        file_reader = FileReader(64, 64, 3)
        self.image_array = file_reader.read_images_from_list_of_directories(dir_list)
        self.steering_array = file_reader.read_steering_from_list_of_directories(dir_list)

        print('image array:')
        print(type(self.image_array))
        print(self.image_array.shape)
        print(type(self.image_array[0][0][0][0]))
        print('steering array:')
        print(type(self.steering_array))
        print(self.steering_array.shape)
        print(type(self.steering_array[0]))
        return

    def shuffle(self):
        return
    
    def split_train_test(self):
        return

    def organize_as_dictionary(self):
        self.my_dataset = {}   

        self.my_dataset['target_names'] = [1, 3, 2]
        self.my_dataset['images'] = self.image_array
        self.my_dataset['target'] = self.steering_array
        
        self.my_dataset['DESCR'] = """

                The dataset is <N> image and steering values from a toy
                car as it is driven around a track.  The track is a
                piece of tape on a concrete floor. The steering values
                are the steering applied by the driver to keep the
                car on the track.
                
                The dataset is available from:
                https://github.com/cwinsor/metrowest_scikit_tensorflow_cnn_car.git

                The structure of the dataset is:

                "DESCR" - an overview description of the dataset.
               
                "images" - A 4-dimensional numpy array of integers,
                of size (<N>, height, width, depth). The first dimension is the image
                height(64), width(64) and depth(3) for RGB.

                "steering" - A 1-dimensional numpy array of integers
                of size <N>.  The value is the direction the car is
                being steered at the time of the corresponding image.
                The values are "categorical"
                with 1=left, 3=straight 2=right.

                "target_names" - a list of values of the steering class [1, 3, 2]

 
            """
        self.describe_dataset(self.my_dataset)
        return 

    # save to pickle file
    import pickle
    def save_to_pickle_file(self,filename):
        with open(filename, 'wb') as output:
            pickle.dump(self.my_dataset, output)
            
    # restore from pickle file
    import pickle
    def restore_from_pickle_file(self,filename):
        with open(filename, 'rb') as data:
            dataset_in = pickle.load(data)
        self.describe_dataset(dataset_in)
        return dataset_in

        
