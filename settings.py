# config.py
# Configuration, just like it says on the cover
import os

class Config(object):

    SECRET_KEY = os.urandom(32)
    # Grabs the folder where the script runs.
    basedir = os.path.abspath(os.path.dirname(__file__))
    # Enable debug mode.
    DEBUG = True
    # put your token here
    TOKEN = "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"