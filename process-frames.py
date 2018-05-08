"""
Applies one or more scripts to a directory of frames

python process-frames.py inDir ourDir image-transforms/do-mask.sh image-transforms/remove-background.sh
"""
from PIL import Image
import os
import sys
from subprocess import call
from multiprocessing import Pool

POOL_SIZE = 8

inDir = sys.argv[1]
outDir = sys.argv[2]
steps = sys.argv[3:]

os.makedirs(outDir, exist_ok=True)

toProcess = []

for subdir, dirs, files in os.walk(inDir):
    for file in files:
        if file.endswith('.png'):
            toProcess.append(file)

def do_process_frame(file):
    inFile = os.path.join(inDir, file)
    for step in steps:
        outFile = os.path.join(outDir, file)
        call(['bash', step, inFile, outFile])
        inFile = outFile

with Pool(POOL_SIZE) as pool:
    pool.map(do_process_frame, toProcess)