from setuptools import setup

APP = ['Calculator.py']
DATA_FILES = ['+.gif','-.gif', 'divide.gif', 'mult.gif']
OPTIONS = {
 'iconfile':'calc.icns',
 'argv_emulation': True,
 'packages': ['tkinter'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)