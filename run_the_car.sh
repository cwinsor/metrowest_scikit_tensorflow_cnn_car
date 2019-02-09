#!/bin/bash -e

export PROJECT_HOME="/home/pi/metrowest_scikit_tensorflow_cnn_car"

alias setup_00="source ${PROJECT_HOME}/project/rasp_pi/setup_everytime_pi_00_activate_env.sh"
alias setup_01="source ${PROJECT_HOME}/project/rasp_pi/setup_everytime_pi_01_add_lib_to_path.sh"
alias run_it="python3 ${PROJECT_HOME}/project/rasp_pi/self_driving_car_drive.py &"

setup_00
setup_01
echo "python is " $(which python)
run_it
