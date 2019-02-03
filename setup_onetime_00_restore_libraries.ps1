

## NEED TO RUN THIS AS ADMIN - VIRTUALENV SEEMS TO REQUIRE ADMIN

# reference:  https://packaging.python.org/guides/installing-using-pip-and-virtualenv/

# confirm at least we have python with pip
python --version
python -m pip --version

# add virtualenv if user doesn't have it
#python -m pip uninstall virtualenv
python -m pip install virtualenv
python -m virtualenv --version
# create an empty virtualenv
python -m virtualenv pymote_env --no-site-packages

# activate the (empty) virtualenv
.\pymote_env\Scripts\activate

# confirm where python is found (the environment is being used)
# and the version of python
Get-Command python

# list what the blank environment has
pip list

# get the libraries specified in the requirements.txt file
pip install -r requirements.txt
