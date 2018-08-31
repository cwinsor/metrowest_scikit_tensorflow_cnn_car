# metrowest_scikit_tensorflow_cnn_car
Self-driving car using Convolutional Neural Network.

See the .pdf or .doc for details on the project.

To set up your environment:

One time:
Set up yourworkarea and virtualenv (specifying python 3) - refer to the O'Reilly Scikit learn book - page 41

cd $ML_PATH
git clone https://github.com/cwinsor/metrowest_scikit_tensorflow_cnn_car.git


The git includes documentation, example data, and src directory.

The documentation has an overview of the project, details about the car, and procedure to train the CNN. 

Within the source directory are 2 files
- "self_driving_car.py" is python run on the Raspberry Pi used to collect data, and later, to drive the car.
- "train_cnn.py" is python run on the workstation or cloud server and trains the CNN.

