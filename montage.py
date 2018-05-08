"""
Combine images from multiple directories into a 2x2 grid

python montage.py outDir inputDir1 inputDir2 inputDir3 inputDir4
"""
from PIL import Image
import os
import sys
import glob
from subprocess import call
from multiprocessing import Pool

POOL_SIZE = 8

outDir = sys.argv[1]
files = sys.argv[2:]

os.makedirs(outDir, exist_ok=True)

counts = {}

def do_process_frame(i):
    inFiles = []
    for dir in files:
        file = min(counts[dir], i)
        inFiles.append(os.path.join(dir, '{}.png'.format(file)))
    outFile = os.path.join(outDir, str(i) + '.png')
    call('montage {0} -geometry +0+0 -tile 2x2 {1}'.format(' '.join(inFiles), outFile), shell=True)

for dir in files:
    counts[dir] = len(glob.glob("{0}/*.png".format(dir)))

maxCount = max(counts.values())

toProcess = range(1, maxCount)

with Pool(POOL_SIZE) as pool:
    pool.map(do_process_frame, toProcess)