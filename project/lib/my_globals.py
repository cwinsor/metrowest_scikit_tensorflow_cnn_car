IMAGE_RAW_H = 90
IMAGE_RAW_W = 180
IMAGE_D = 3

DOWNSAMPLE_FACTOR = 3
IMAGE_FINAL_H = 30
IMAGE_FINAL_W = 60



THRESHOLD_LEFT = 390
THRESHOLD_RIGHT = 404

# left/right steering values
# this reflects the wiring of the controller
# which is 2 bits, open drain, low asserted
# e.g.
#   both high is no solenoids = straight
#   bit 1 pulled low = left solenoid
#   bit 0 pulled low = right solenoid
SIGNAL_LEFT = 1
SIGNAL_RIGHT = 2
SIGNAL_STRAIGHT = 3
