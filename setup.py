# setup.py
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
