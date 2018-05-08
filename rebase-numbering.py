"""
Renumbers a sequence of image files so that they start at 1. Goes from:

    8.png
    9.png
    10.png
    ...

to:

    1.png
    2.png
    3.png
    ...
"""
import os
import glob
import sys
import re
from shutil import copyfile

numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

os.mkdir('{0}-out'.format(sys.argv[1]))

index = 1
for oldfile in list(sorted(glob.glob("{0}/*.png".format(sys.argv[1])), key=numericalSort)):
    newfile = '{0}-out/{1}.png'.format(sys.argv[1], index)
    print(newfile)
    copyfile(oldfile, newfile)
    index = index + 1
