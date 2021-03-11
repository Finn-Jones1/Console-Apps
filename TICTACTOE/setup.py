from setuptools import setup

APP = ['TicTacToe HARD.py']
DATA_FILES = []
OPTIONS = {
 'iconfile':'Tic.icns',
 'argv_emulation': True,
 'packages': ['tkinter'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)