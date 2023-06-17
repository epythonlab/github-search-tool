"""
config.py

This module contains the configuration settings for the application.

Attributes:
- SECRET_KEY: A random string used for cryptographic purposes.
- basedir: The absolute path of the directory where the script runs.
- DEBUG: A boolean value indicating whether debug mode is enabled.
- TOKEN: The token used for authentication.

Usage:
- Import the Config class from this module to access the configuration settings.
- Modify the attributes of the Config class to customize the application's behavior.
"""
import os

class Config:
    """
    Config class containing the configuration settings for the application.
    """

    SECRET_KEY = os.urandom(32)
    # Grabs the folder where the script runs.
    basedir = os.path.abspath(os.path.dirname(__file__))
    # Enable debug mode.
    DEBUG = True
    # put your token here
    TOKEN = "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"
