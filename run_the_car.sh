#!/bin/bash -e

# This script can be used to automatically run the car
# when the Pi boots up. It is intended to be called using
# a systemd service unit the systemd service files are 
# in /etc/systemd/
#
# For details on how to set up a systemd service unit refer to 
# https://linuxconfig.org/how-to-automatically-execute-shell-script-at-startup-boot-on-systemd-linux
#
# Commands to monitor status of systemctl/systemd are:
# sudo systemctl daemon-reload
# sudo systemctl start metrowest-car-start-it-running.service
# sudo systemctl status metrowest-car-start-it-running.service
# sudo systemctl stop metrowest-car-start-it-running.service


export PROJECT_HOME="/home/pi/metrowest_scikit_tensorflow_cnn_car"

echo "here1 - before activate env"
echo $(which python)
source ${PROJECT_HOME}/project/rasp_pi/setup_everytime_pi_00_activate_env.sh
echo "here2 - after activate env, before add lib"
echo $(which python)
source ${PROJECT_HOME}/project/rasp_pi/setup_everytime_pi_01_add_lib_to_path.sh
echo "here3"
python ${PROJECT_HOME}/project/rasp_pi/self_driving_car_drive.py > /home/pi/metrowest_scikit_tensorflow_cnn_car/run_output.log 2>&1
#python ${PROJECT_HOME}/project/rasp_pi/self_driving_car_drive.py
echo "here4"


