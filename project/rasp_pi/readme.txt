
Instructions to install Keras on Raspberry Pi...

https://medium.com/@abhizcc/installing-latest-tensor-flow-and-keras-on-raspberry-pi-aac7dbf95f2

Install Keras:
sudo apt-get install python3-numpy
sudo apt-get install libblas-dev
sudo apt-get install liblapack-dev
sudo apt-get install python3-dev 
sudo apt-get install libatlas-base-dev
sudo apt-get install gfortran
sudo apt-get install python3-setuptools
sudo apt-get install python3-scipy
sudo apt-get update
sudo apt-get install python3-h5py
sudo pip3 install keras 


Test your Keras installation by
python -c 'import keras; print(keras.__version__)'# python 2
python3 -c 'import keras; print(keras.__version__)'  # for Python 3


For Tensorflow there is an additional step necessary
it involves adding a /etc/pip.conf file that points to www.piwheels.org/simple
https://www.raspberrypi.org/magpi/tensorflow-ai-raspberry-pi/
https://www.raspberrypi.org/forums/viewtopic.php?t=219853

sudo nano /etc/pip.conf

and add
extra-index-url=https://www.piwheels.org/simple

and then run the pip3 install command.

for tensorflow - also need the following:
from  https://www.raspberrypi.org/magpi/tensorflow-ai-raspberry-pi/
sudo pip3 install --upgrade pip
sudo pip3 install --upgrade pip3
sudo pip3 install --upgrade piwheels
sudo pip3 install --upgrade tensorflow

Test your Tensorflow installation by
python -c 'import tensorflow as tf; print(tf.__version__)'  # for Python 2
python3 -c 'import tensorflow as tf; print(tf.__version__)'  # for Python 3
