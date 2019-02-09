#!/bin/bash

cd project/rasp_pi/
source setup_everytime_pi_00_activate_env.sh
source setup_everytime_pi_01_add_lib_to_path.sh
python3 self_driving_car_drive.py &

