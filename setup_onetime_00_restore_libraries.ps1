
# confirm at least we have python with pip
python --version
python -m pip --version

# create an empty virtualenv
python -m pip install virtualenv
python -m virtualenv --version
python -m virtualenv pymote_env --no-site-packages

# activate the (empty) virtualenv
.\pymote_env\Scripts\activate

# get the libraries specified in the requirements.txt file
pip install -r requirements.txt
