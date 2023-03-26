import time

import pyautogui  #pip install pyautogui

from PIL import Image, ImageGrab  #pip install pillow

from numpy import asarray


#pyautogui.keyDown('d')
def hitKey(key):
    pyautogui.keyDown(key)


#def draw():






def isCollide(data):
    for i in range(300,415):
        for j in range(600, 650):
            if data[i,j] < 100:       # when pixel is black in color
                return True

    return False


if __name__ == "__main__":
    time.sleep(3)
    hitKey("up")
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()  #data in form of arrray
        #print(asarray(image))

        if isCollide(data):
            hitKey("up")