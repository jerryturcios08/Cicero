#!/usr/bin/python3

from camera import VideoCamera
import cv2
import sys
import os
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import numpy as np
import pyttsx

import time
#import denoising

from os import system
def gen(camera):
    count=0
    frame = camera.get_frame()
    while True:
        frame = camera.get_frame()
        #new code
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       
        """
        gray = cv2.medianBlur(gray, 3)
        gray = np.float64(gray)
        noise = np.random.randn(*gray.shape)*10
        noisy=1+noise
        noisy = np.uint8(np.clip(noisy,0,255))
        dst = cv2.fastNlMeansDenoisingMulti(noisy, 2, 5, None, 4, 7, 35)
        """

        filename = "{}.png".format(os.getpid())
        cv2.imwrite(filename, gray)

        """
        im = Image.open(filename) # the second one 
        im = im.filter(ImageFilter.MedianFilter())
        enhancer = ImageEnhance.Contrast(im)
        im = enhancer.enhance(2)
        im = im.convert('1')
        im.save('temp2.jpg')
        filename2 = "{}.png".format(os.getpid())
        os.system('python denoising.py filename filename2')  
        cv2.imwrite(filename, filename2)
        cv2.imwrite(filename, dst)
        """
     
        # load the image as a PIL/Pillow image, apply OCR, and then delete
        # the temporary file
        text = pytesseract.image_to_string(Image.open(filename))
        os.remove(filename)
        print(text)
        text2=text.encode('utf-8').strip()
        #engine = pyttsx.init()
        if(len(text2)>0):
           #os.system(text2.split()[0])
           speech = text2
           system('say ' + '"' + speech + '"')

           """
           #engine.say(text)           
           #engine.runAndWait()
           """

           time.sleep(5)

        """
        #engine = pyttsx.init()
        #engine.say(text)
        #engine.runAndWait()
        #os.remove('temp2.jpg')
        #frame = camera.get_frame()
        # show the output images
        #cv2.imshow("Image", frame)
        #cv2.imshow("Output", gray)
        #cv2.waitKey(0)
        """

        if cv2.waitKey(1) & 0xFF == ord('q'):
           break

if __name__ == '__main__':               
        gen(VideoCamera())
