import glob
import colorsys
from PIL import Image
import time
def createCoords(fileName):
    coordinates_list = []
    image_list = []
    for filename in glob.glob(fileName):
        im=Image.open(filename)
        image_list.append(im)
    for all in image_list:
        avgx = 0
        avgy = 0
        valid_white = 0
        length = all.size[0]
        height = all.size[1]
        for x in range (0, length, 3):
            for y in range(0, height, 3):
                rgb = all.getpixel((x,y))
                hsv = colorsys.rgb_to_hsv(rgb[0], rgb[1], rgb[2])
                if (hsv[0] >= 0 and hsv[0] <=360 and hsv[1] >= 0 and hsv[1]<=0.1  and hsv[2] >= 190 and hsv[2] <=255):
                    avgx += x
                    avgy += y
                    valid_white += 1
        if (valid_white > 0):
            avgx = avgx/valid_white
            avgy = avgy/valid_white
            coordinates_list.append((avgx,avgy))
        else:
            coordinates_list.append((0,0))
        print((avgx, avgy))
    fileName2 = fileName[0:fileName.rfind("/")]
    fileName2 = fileName[0:fileName2.rfind("/")]
    fileName2 = fileName2 + "/coordinates.txt"
    file1 = open(fileName2, "w") 

    for all in coordinates_list:
        str1 = "(" + str(round(all[0])) + "," + str(round(all[1])) + ")"
        file1.write(str1)
        file1.write("\n")
    file1.close() 
#Given a sorted list of either x or y positions, sort 
#secondary values in ascending order
#Ex: sortSecondary(((1,3), (1,2), (2,1)), 1) ---> (1,2), (1,3), (2,1)
def sortSecondary(coordList, position):
    secondaryPosition = 0
    if (position == 0):
        secondaryPosition = 1
    for x in range(0, len(coordList)):
        if (x < len(coordList) - 2):
            t = x + 1
            while (coordList[x][position] == coordList[t][position]):
                if (coordList[x][secondaryPosition] > coordList[t][secondaryPosition]):
                    pair1 = list(coordList[x])
                    pair2 = list(coordList[t])
                    pair1[secondaryPosition] = coordList[t][secondaryPosition]
                    pair2[secondaryPosition] = coordList[x][secondaryPosition]
                    coordList[x] = tuple(pair1)
                    coordList[t] = tuple(pair2)
                t = t + 1
    return coordList

#Given filePath as String, return given coordinates sorted according 
#to ascending x value
def sortX(filePath):
    currentLED = 0
    f = open(filePath, "r") 
    coordList = []
    s = f.readline()
    while (s != ""):
        newTup = list(eval(s))
        newTup.append(currentLED)
        newTup = tuple(newTup)
        coordList.append(newTup)
        s = f.readline()
        currentLED = currentLED + 1
    coordList.sort(key=lambda a:a[0])
    f.close()
    coordList = sortSecondary(coordList, 0)

    #Empty coordinates text file
    f = open(filePath, "r+") 
    f.seek(0) 
    f.truncate() 
    f.close()

    #Write new sorted coordinates into text file
    f = open(filePath, "w") 
    for all in (coordList):
        f.write(str(all))
        f.write("\n")
    f.close()

#Given filePath as String, return given coordinates sorted according 
#to ascending y value
def sortY(filePath):
    currentLED = 0
    f = open(filePath, "r") 
    coordList = []
    s = f.readline()
    while (s != ""):
        newTup = list(eval(s))
        newTup.append(currentLED)
        newTup = tuple(newTup)
        coordList.append(newTup)
        s = f.readline()
        currentLED = currentLED + 1
    coordList.sort(key=lambda a:a[1])
    f.close()
    coordList = sortSecondary(coordList, 1)

    #Empty coordinates text file
    f = open(filePath, "r+") 
    f.seek(0) 
    f.truncate() 
    f.close()

    #Write new sorted coordinates into text file
    f = open(filePath, "w") 
    for all in (coordList):
        f.write(str(all))
        f.write("\n")
    f.close()
    time.sleep(1)  #Delay to prevent issues with opening and closing files
    reverseCoords(filePath)


def reverseCoords(filePath):
    f = open(filePath, "r") 
    coordList = []
    s = f.readline()
    while (s != ""):
        coordList.append(eval(s))
        s = f.readline()
    f = open(filePath, "r+") 
    f.seek(0) 
    f.truncate() 
    f.close()
    f = open(filePath, "w") 
    coordList.reverse()
    for all in (coordList):
        f.write(str(all))
        f.write("\n")
    f.close()
createCoords('C:/Users/joelj/OneDrive/Desktop/BinaryChristmasTree/Test/*.png')
# sortY("C:/Users/joelj/OneDrive/Desktop/BinaryChristmasTree/coordinates.txt")
