# the original geneostrat images are this size
IMAGE_RAW_H = 90
IMAGE_RAW_W = 180
IMAGE_D = 3

# during preprocessing we downsample raw data by FACTOR
# to get images of size CAMERA
DOWNSAMPLE_FACTOR_H = 2
DOWNSAMPLE_FACTOR_W = 2

# at runtime on the PI we specify the camera to capture images this size
CAMERA_H = 45
CAMERA_W = 90

# left/right steering thresholds
# the original geneostrat data has a target class that is numeric
# we need to convert that to nominal (3 values).  The following
# are the thresholds to do that
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
