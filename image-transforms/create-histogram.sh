#!/usr/bin/env python
"""
Create a histogram
"""
from PIL import Image, ImageDraw
import os
import sys
import re
import math
from subprocess import check_output

GOOD_COLORS = ['#0000FFFF', '#00FF00FF', '#FF0000FF']

inFile = sys.argv[1]
outFile = sys.argv[2]


output = str(check_output('convert {0} -format %c histogram:info:'.format(inFile), shell=True))
colors = {}
sum = 0
for match in re.finditer(r'\s*(\d+):.+?(#\w+)', output):
    value = int(match.group(1))
    color = match.group(2)
    if not color in GOOD_COLORS:
        continue
    colors[color] = value
    sum += value

width = 100
height = 100

img = Image.new('RGB', (width, height), 'white')

start = 0
draw = ImageDraw.Draw(img)
for color, value in colors.items():
    end = math.ceil(value / float(sum) * width)

    draw.rectangle(((start, 0), (start + end, height)), fill=color)
    start += end
del draw

img.save(outFile)
