import neopixel
import time
import board
import cv2
import time
import os
from PIL import Image
import colorsys
from picamera import PiCamera

def Capture3D(num_pixels, planeofR):
    pixel_pin = board.D18
    ORDER = neopixel.GRB
    pixels = neopixel.NeoPixel(
        pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
    )
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    directory = r'/home/pi/Desktop/BinaryChristmasTree/XYPics'
    os.chdir(directory)
    
    integerLength = len(str(num_pixels))
    pixels.fill((0,0,0))
    pixels.show()
    for img_counter in range(num_pixels):
        valid_white = 0
        pixels[img_counter] = (255, 255, 255)
        pixels.show()
        time.sleep(0.5)
        img_name = "{}.png".format(img_counter)
        img_name = img_name.zfill(integerLength + 4)
        img_name = planeofR + img_name
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        directory = r'/home/pi/Desktop/BinaryChristmasTree/XYPics'
        cv2.imwrite(img_name, frame)
        
        print(img_counter, "WRITTEN")
        
        pixels[img_counter] = (0,0,0)
        time.sleep(0.5)        
    cam.release()
    cv2.destroyAllWindows()
Capture3D(550, 'A')