# setup.py
#still under development
# This script is used to package the application using py2app.
# Make sure to run this script in the terminal with the command:
# python setup.py py2app    
# 7/22 11:04pm mtn time
from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['watchdog', 'psutil', 'pyperclip', 'pynput'],
    # Optional: specify an icon file
    # 'iconfile': 'MyIcon.icns',
    # To hide the dock icon and menu bar, you could add:
    # 'plist': {'LSUIElement': True},
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
