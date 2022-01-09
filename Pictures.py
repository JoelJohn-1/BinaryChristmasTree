import cv2
import time
import os
from PIL import Image

def Capture(total):
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    directory = r'C:\Users\joelj\OneDrive\Desktop\BinaryChristmasTree\LEDPics'
    os.chdir(directory)
    img_counter = 0
    integerLength = len(str(total))  
    #Delay until first movement is detected
    blackFrameS = 'C:/Users/joelj/OneDrive/Desktop/BinaryChristmasTree/LEDPics/BlackFrame.png'
    bfFrame=Image.open(blackFrameS)
    firstFrameNotFound = True
    while firstFrameNotFound:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        directory = r'C:/Users/joelj/Desktop/BinaryChristmasTree/LEDPics'
        cv2.imwrite('currentFrame.png', frame)
        currentFrame = Image.open('C:/Users/joelj/OneDrive/Desktop/BinaryChristmasTree/LEDPics/currentFrame.png')
        differentPixels = 0
        for x in range (0, bfFrame.size[0], 10):
            if (firstFrameNotFound == False):
                break
            for y in range(0, bfFrame.size[1], 10):
                bfPixels = bfFrame.getpixel((x,y))
                currentPixels = currentFrame.getpixel((x,y))
                if (currentPixels[0] - bfPixels[0] > 40 and currentPixels[1] - bfPixels[1] > 29 and currentPixels[2] - bfPixels[2] > 29):
                    differentPixels = differentPixels + 1
                if (differentPixels > 2):
                    firstFrameNotFound = False
                    break
        directory = r'C:/Users/joelj/Desktop/BinaryChristmasTree/LEDPics'
        os.remove('C:/Users/joelj/OneDrive/Desktop/BinaryChristmasTree/LEDPics/currentFrame.png')
    
    #Begin taking photos 
    for x in range(0, total):
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)
        k = 288
        if x == total:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            directory = r'C:/Users/joelj/Desktop/BinaryChristmasTree/LEDPics'
            img_name = "{}.png".format(img_counter)
            img_name = img_name.zfill(integerLength + 4)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
        time.sleep(1)
    cam.release()
    cv2.destroyAllWindows()

Capture(50)

