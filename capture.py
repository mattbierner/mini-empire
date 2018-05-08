"""
Capture frames of the minimap every two seconds or so
"""
from PIL import Image, ImageGrab
import time
import os
from os import path
import sys
import tempfile 
import math
import win32gui

def _get_windows_bytitle(title_text, exact = False):
    def _window_callback(hwnd, all_windows):
        all_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
    windows = []
    win32gui.EnumWindows(_window_callback, windows)
    if exact:
        return [hwnd for hwnd, title in windows if title_text == title]
    else:
        return [hwnd for hwnd, title in windows if title_text in title]

def screenshot(hwnd, outFile):
    import win32ui
    import win32con
    from time import sleep
    try:
        if not hwnd:
            hwnd = win32gui.GetDesktopWindow()
        l,t,r,b=win32gui.GetWindowRect(hwnd)
        h= math.floor((b-t) * 2)
        w=math.floor((r-l) * 2)
        hDC = win32gui.GetWindowDC(hwnd)
        myDC = win32ui.CreateDCFromHandle(hDC)
        newDC = myDC.CreateCompatibleDC()

        myBitMap = win32ui.CreateBitmap()
        myBitMap.CreateCompatibleBitmap(myDC, w, h)

        newDC.SelectObject(myBitMap)

        win32gui.SetForegroundWindow(hwnd)
        sleep(0.1) #lame way to allow screen to draw before taking shot
        newDC.BitBlt((0,0),(w, h) , myDC, (0,0), win32con.SRCCOPY)
        myBitMap.Paint(newDC)
        myBitMap.SaveBitmapFile(newDC, outFile)
        return outFile
    finally:
        win32gui.DeleteObject(myBitMap.GetHandle())
        myDC.DeleteDC()
        newDC.DeleteDC()

outdir = sys.argv[1]
os.makedirs(outdir, exist_ok=True)

hwd = _get_windows_bytitle('Age of Empires')[0]

i = 0
while True:
    outFile = path.join(outdir, str(i)) + '.bmp'
    screenshot(hwd, outFile)
    img = Image.open(outFile)

    # Crop to minimap
    area = (1042, 656, 1370, 824)
    cropped_img = img.crop(area)
    cropped_img.save(path.join(outdir, str(i)) + '.png')

    os.remove(outFile)

    i = i + 1
    time.sleep(2)
