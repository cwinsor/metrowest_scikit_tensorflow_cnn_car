# metrowest_scikit_tensorflow_cnn_car

Self-driving car using Convolutional Neural Network.  The project was done with the
Metrowest Boston Developers Machine Learning Group.

Refer to cnn_auto_driving_car_project.pdf for details about the project.

The project utilizes TensorFlow and Kiras Python libraries. A good reference
is "Hands-On Machine learning with Scikit-Learn & TensorFlow" (Geron) from O'Reilly.
This includes steps to set up a virtualenv using PIP and full instructions and
examples on Tensorflow and Scikit.

This git repository is available via:
git clone https://github.com/cwinsor/metrowest_scikit_tensorflow_cnn_car.git

The repository includes the following documentation, data, and Python source:

cnn_auto_driving_car_project.pdf  - documentation about the project
model\Learn To Drive.ipynb - jupyter notebook which trains the CNN
model\weights.hdf5 - weights file for the trained CNN
rasp_pi\self_driving_car_capture.py - file run on the Raspberry Pi to capture image and steering data
rasp_pi\self_driving_car_drive.py   - file run on the Raspberry Pi to drive the car using the trained CNN
rasp_pi\self_driving_car_test.py    - file used during development to verify GPIO and camera functionality.
lib\    - user and architect libraries and examples as follows:
lib\test*.ipynb              - jupyter notebooks with examples demonstrating use of libraries
lib\metrowestcar_dataset.py  - user library to read dataset
lib\metrowestcar_display.py  - user library to display annotated images
lib\metrowestcar_dataset_architect.py - architect library to build dataset from raw data files
lib\metrowestcar_file_io.py           - architect library to read raw data files
data\      directory where the dataset is kept
data_raw\  directory where raw flatfile data is kept


