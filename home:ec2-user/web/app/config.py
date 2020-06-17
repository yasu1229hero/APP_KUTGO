# Code written by Fitra
# Function    : to save the config of secret key
# Output      : secret key

import os

class Config(object):
	# get or save the random md5 secret key
    SECRET_KEY = os.environ.get('SECRET_KEY') or '65a6b5e4a3204bdd87adb7b1a98eafaa'