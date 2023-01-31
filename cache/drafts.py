
import os

filename = '/home/aditya1117/PycharmProjects/pythonProject/Demo.csv'
print("The original filename:", filename)
filename = os.path.basename(filename)
print("The output filename:", filename)

import pathlib

filename = pathlib.Path('/home/aditya1117/PycharmProjects/pythonProject/Demo.csv')
print("The original filename:", filename)
filename = filename.stem
print("The output filename:", filename)
