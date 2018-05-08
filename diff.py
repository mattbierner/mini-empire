"""
Create a simple diff of frames
"""
from PIL import Image
import os
import sys
from subprocess import call
from multiprocessing import Pool

POOL_SIZE = 8

inDir = sys.argv[1]
outDir = sys.argv[2]
end = sys.argv[3]

os.makedirs(outDir, exist_ok=True)

toProcess = []

for subdir, dirs, files in os.walk(inDir):
    for file in files:
        if file.endswith('.png'):
            toProcess.append(file)

def do_process_frame(i):
    previous = os.path.join(inDir, str(i - 1) + '.png')
    inFile = os.path.join(inDir, str(i) + '.png')
    outFile = os.path.join(outDir, str(i) + '.png')
    call(['bash', 'diff.sh', previous, inFile, outFile])

toProcess = range(2, end)

with Pool(POOL_SIZE) as pool:
    pool.map(do_process_frame, toProcess)