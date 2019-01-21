import pickle
from keras.datasets import mnist
from metrowestcar_file_io import FileReader

import numpy as np


class DatasetArchitect(object):

    
    def describe_dataset(self, dataset):
        print(type(dataset))
        print(dataset.keys())
        print('There are ' + str(len(dataset['images_train'])) + ' images (training)')
        print('There are ' + str(len(dataset['images_test'])) + ' images (test)')
        print('There are ' + str(len(dataset['steering_train'])) + ' steering values (training)')
        print('There are ' + str(len(dataset['steering_test'])) + ' steering values (test)')
            

        print("The image array (training) is a " + str(dataset['images_train'].shape) + " of " + str(type(dataset['images_train'][0][0][0][0])))
        print("The image array (test)     is a " + str(dataset['images_test'].shape) + " of " + str(type(dataset['images_test'][0][0][0][0])))
        print("The steering array (training) is a " + str(dataset['steering_train'].shape) + " of " + str(type(dataset['steering_train'][0])))  
        print("The steering array (test)     is a " + str(dataset['steering_test'].shape) + " of " + str(type(dataset['steering_test'][0])))
        return
    
    def read_raw_data_from_files(self, dir_list):

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

    # reference:
    # https://stackoverflow.com/questions/4601373/better-way-to-shuffle-two-numpy-arrays-in-unison
    def shuffle_in_unison(self, a, b):
        assert len(a) == len(b)
        rng_state = np.random.get_state()
        np.random.shuffle(a)
        np.random.set_state(rng_state)
        np.random.shuffle(b)
    
        #shuffled_a = np.empty(a.shape, dtype=a.dtype)
        #shuffled_b = np.empty(b.shape, dtype=b.dtype)
        #permutation = np.random.permutation(len(a))
        #for old_index, new_index in enumerate(permutation):
        #    shuffled_a[new_index] = a[old_index]
        #    shuffled_b[new_index] = b[old_index]
        #return shuffled_a, shuffled_b

    def shuffle(self):
        self.shuffle_in_unison(self.image_array, self.steering_array)
        print('image array:')
        print(type(self.image_array))
        print(self.image_array.shape)
        print(type(self.image_array[0][0][0][0]))
        print('steering array:')
        print(type(self.steering_array))
        print(self.steering_array.shape)
        print(type(self.steering_array[0]))
        return

    # split 80/20 train/test
    def split_train_test(self):
        whole = self.steering_array.shape[0]
        self.cut = int(whole * 0.8)
        print("whole = ", self.steering_array.shape[0])
        print("cut   = ", self.cut, " ", whole-self.cut)
        return

    def organize_as_dictionary(self):
        self.my_dataset = {}   

        self.my_dataset['target_names'] = [1, 3, 2]
        self.my_dataset['images_train'] = self.image_array[:self.cut]
        self.my_dataset['images_test'] = self.image_array[self.cut:]
        self.my_dataset['steering_train'] = self.steering_array[:self.cut]
        self.my_dataset['steering_test'] = self.steering_array[self.cut:]
            
        self.my_dataset['DESCR'] = """

                The dataset is a collection of images and steering from a toy
                car as it is driven around a track.
                
                The track is set up on a concrete floor. A piece of tape defines
                the centerline and the car will be trained to follow this line.
                During training the steering values applied by the driver to
                keep the car on the track are captured.
                                
                The dataset is split into training and test subsets
                of size 2582 and 646 respectively.
                
                Images are square, size 64x64 using RGB encoding.
                This is kept as a 4-dimensional numpy array of numpy.uint8.
                The dimensions of this array are [N][64][64][3].
                The first dimension is image number.
                The next two dimensions are height, width.
                The final dimension is color.

                Steering values are categorical with 1=left, 3=straight 2=right.
                The data is kept as a 1-dimensional numpy array of numpy.uint32
                The array is size [N] which is the direction the car is
                being steered at the time of the correspondingly-numbered image.

                The structure of the dataset is:

                "DESCR" - an overview description of the dataset.
                "images_train"   - training images
                "images_test"    - testing image
                "steering_train" - training steering values
                "steering_test"  - testing steering values
                "target_names"   - a list of values of the steering class [1, 3, 2]

                The dataset is available from:
                https://github.com/cwinsor/metrowest_scikit_tensorflow_cnn_car.git
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

        
