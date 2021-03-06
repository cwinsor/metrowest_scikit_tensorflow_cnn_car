#!/bin/bash

# confirm at least we have python with pip
python3 --version
python3 -m pip --version

# add virtualenv if user doesn't have it
python3 -m pip install --user virtualenv
python3 -m virtualenv pi_env --no-site-packages

# activate the (empty) virtualenv
source ./pi_env/bin/activate

# confirm where python is found (the environment is being used)
# and the version of python
which python3
python3 --version

# list what the blank environment has
pip3 list

### tensorflow - per  https://github.com/samjabrahams/tensorflow-on-raspberry-pi
### sudo apt install libatlas-base-dev

# get the libraries specified in the requirements.txt file
pip3 install -r requirements.txt

### note hack...
echo 'hack to get h5py able to be found...i see https://stackoverflow.com/questions/45624116/load-weights-require-h5py'
sudo apt-get install libhdf5-dev


Test your Keras installation by
###python -c 'import keras; print(keras.__version__)'# python 2
python3 -c 'import keras; print(keras.__version__)'  # for Python 3


### pi camera...
sudo pip install picamera
sudo pip install -U picamera


