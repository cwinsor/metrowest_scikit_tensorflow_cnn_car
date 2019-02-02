import pickle
from keras.datasets import mnist
from metrowestcar_file_io import FileReader

import numpy as np


class DatasetArchitect(object):

    #def __init__(self):

               
    def describe_dataset(self, dataset):
        print(type(dataset))
        print(dataset.keys())

        print("(training) image array is    " + str(dataset['images_train'].shape) + " of " + str(type(dataset['images_train'][0][0][0][0])))
        print("(training) steering array is " + str(dataset['steering_train'].shape) + " of " + str(type(dataset['steering_train'][0])))  
        print("(test) image array is    " + str(dataset['images_test'].shape) + " of " + str(type(dataset['images_test'][0][0][0][0])))
        print("(test) steering array is " + str(dataset['steering_test'].shape) + " of " + str(type(dataset['steering_test'][0])))
        return
    
    def read_raw_data_from_files(self, dirpath, tracklist):
        import my_globals as mygl

        file_reader = FileReader(mygl.IMAGE_RAW_H, mygl.IMAGE_RAW_W, mygl.IMAGE_D)
        image_array_pre_downsample = file_reader.read_images_from_list_of_tracks(dirpath, tracklist)
        steering_array_pre_threshold = file_reader.read_steerings_from_list_of_tracks(dirpath, tracklist)

        # threshold the steering values
        self.steering_array = np.empty((0),np.uint32)

        count_l = 0
        count_s = 0
        count_r = 0
        for steering_value in steering_array_pre_threshold:
            if steering_value < mygl.THRESHOLD_LEFT:
                signal = mygl.SIGNAL_LEFT
                count_l += 1
            elif mygl.THRESHOLD_RIGHT < steering_value:
                signal = mygl.SIGNAL_RIGHT
                count_r += 1
            else:
                signal = mygl.SIGNAL_STRAIGHT
                count_s += 1
            self.steering_array = np.append(self.steering_array, np.uint32(signal))

        # downsample the image
        self.image_array = image_array_pre_downsample [:, 0::mygl.DOWNSAMPLE_FACTOR, 0::mygl.DOWNSAMPLE_FACTOR]


        print('image array (pre-downsample):')
        print(type(image_array_pre_downsample))
        print(image_array_pre_downsample.shape)
        print(type(image_array_pre_downsample[0][0][0][0]))
        print("")

        print('image array (post-downsample):')
        print(type(self.image_array))
        print(self.image_array.shape)
        print(type(self.image_array[0][0][0][0]))
        print("")

        print('steering array (pre_threshold):')
        print(type(steering_array_pre_threshold))
        print(steering_array_pre_threshold.shape)
        print(type(steering_array_pre_threshold[0]))
        print("")

        print('steering array (thresholded):')
        print(type(self.steering_array))
        print(self.steering_array.shape)
        print(type(self.steering_array[0]))
        print("#left =     " + str(count_l))
        print("#straight = " + str(count_s))
        print("#right =    " + str(count_r))


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
        self.whole = self.steering_array.shape[0]
        self.cut = int(self.whole * 0.8)
        print("whole = ", self.whole)
        print("cut   = ", self.cut, " ", self.whole-self.cut)
        return

    def organize_as_dictionary(self):
        self.my_dataset = {}   

        self.my_dataset['target_names'] = [1, 3, 2]
        self.my_dataset['images_train'] = self.image_array[:self.cut]
        self.my_dataset['images_test'] = self.image_array[self.cut:]
        self.my_dataset['steering_train'] = self.steering_array[:self.cut]
        self.my_dataset['steering_test'] = self.steering_array[self.cut:]
            
        self.my_dataset['DESCR'] = f"""

                The dataset is a collection of images and steering from a toy
                car as it is driven around a track.
                
                The track is defined as a piece of red tape on a light colored
                carpet.  The tape is the centerline and the car will be trained
                to follow this line.
                During training the car is controlled by an operator. Steering
                position and images from a front-facing camera are captured.
                The data is used to train a CNN, where the target class is the
                steering position, and attributes are the pixel image values.
                                
                The dataset is {self.whole} samples split into training and test
                subsets of size {self.cut} and {self.whole-self.cut} respectively.
                
                Images are {mygl.IMAGE_FINAL_H}(h) by {mygl.IMAGE_FINAL_W}(w) by {IMAGE_D}
                with the third dimension being numpy.uint8 RGB encoding.
                Images are kept is kept in a numpy array - so the image training array
                is 4-dimensionalal {self.cut}x{mygl.IMAGE_FINAL_H}x{mygl.IMAGE_FINAL_W}x{IMAGE_D}

                Steering values are categorical with 1=left, 3=straight 2=right.
                The data is kept as a 1-dimensional numpy array of numpy.uint32.

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

        
