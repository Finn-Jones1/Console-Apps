from setuptools import setup

APP = ['PythonCleaner.py']
DATA_FILES = []
OPTIONS = {
 'iconfile':'clean.icns',
 'argv_emulation': True,
 'packages': ['tkinter'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)