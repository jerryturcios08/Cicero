from camera import VideoCamera
import cv2
import sys
import os
from PIL import Image
import pytesseract
def gen(camera):
    count=0
    while True:
        frame = camera.get_frame()
        #new code
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        filename = "{}.png".format(os.getpid())
        cv2.imwrite(filename, gray)
# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
        text = pytesseract.image_to_string(Image.open(filename))
        os.remove(filename)
        print(text)
 
# show the output images
        cv2.imshow("Image", frame)
        cv2.imshow("Output", gray)
        cv2.waitKey(0)
        if cv2.waitKey(1) & 0xFF == ord('q'):
           break
		


if __name__ == '__main__':               
        gen(VideoCamera())
