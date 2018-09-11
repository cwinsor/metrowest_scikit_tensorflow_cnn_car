# metrowest_scikit_tensorflow_cnn_car

Self-driving car using Convolutional Neural Network.

See the .pdf or .doc for details on the project.

To set up your environment:

One time:
Set up yourworkarea and virtualenv (specifying python 3) - refer to the O'Reilly Scikit learn book - page 41

cd $ML_PATH
git clone https://github.com/cwinsor/metrowest_scikit_tensorflow_cnn_car.git


The git includes documentation, example data, and src directory.
auto_driving_car_project.docx/.pdf - documentation
data_out                       - raw data from the car consisting of "control" and "image" files
jupyter_notebooks_scikit_learn - not directly related to the car project - these are exercises from O'Reilly "Hands on Machine Learning with Scikit-Learn"
README.md                      - readme file
src\
    data_loader.py             - python library file used to read the raw data and return it as a database (python dictionary wiht data in numpy arrays)
    self_driving_car.py        - python script to run on the Raspberry PI to capture data from the car, and later, drive the car using the CNN and live images

