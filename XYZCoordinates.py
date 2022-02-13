import glob
import colorsys
from PIL import Image
import time
import os
from pathlib import Path

#Going through all pictures in the folder, 'choose' the brightest sector for each LED
#Among the four sectors, AC, keep one delete one
#Criteria for brightest is the picture with the most bright white pixels 
def mergePics(folder):
    Alist = []
    Apath = []
    Clist = []
    Cpath = []
    for filename in glob.glob(folder):
        im=Image.open(filename)
        temp = filename[filename.rindex("\\") + 1]
        if (temp == 'A'):
            Alist.append(im)
            Apath.append(filename)
        elif (temp == 'B'):
            os.remove(filename)
        elif (temp == 'C'):
            Clist.append(im)
            Cpath.append(filename)
        elif (temp == 'D'):
            os.remove(filename)
    sectorList = []
    sectorList.append(Alist)
    sectorList.append(Clist)

    for x in range(len(Alist)):
        maxBrights = 0
        maxImageIndex = 0
        for number in range(len(sectorList)):
            length = sectorList[number][x].size[0]
            height = sectorList[number][x].size[1]
            tempBrights = 0
            for l in range (0, length, 3):
                for h in range(0, height, 3):
                    rgb = sectorList[number][x].getpixel((l,h))
                    hsv = colorsys.rgb_to_hsv(rgb[0], rgb[1], rgb[2])
                    if (hsv[0] >= 0 and hsv[0] <=360 and hsv[1] >= 0 and hsv[1]<=0.1  and hsv[2] >= 190 and hsv[2] <=255):
                        tempBrights = tempBrights + 1
            if (tempBrights > maxBrights):
                maxBrights = tempBrights
                maxImageIndex = number
                
        if (maxImageIndex == 0):
            os.remove(Cpath[x])
        if (maxImageIndex == 1):
            os.remove(Apath[x])
            
          


# mergePics(r"C:\Users\joelj\OneDrive\Desktop\BinaryChristmasTree\XYPics\*.png")
#Depending on the sector, modify the Z coordinates accordingly
#A = 0 degrees
#C = 180 degrees
def createXYZ(folder):
    image_list = []
    coordinates_list = []
    for filename in glob.glob(folder):
        im=Image.open(filename)
        image_list.append((im, filename[filename.rindex("\\") + 1], filename))
    for all in (image_list):
        avgx = 0
        avgy = 0
        valid_white = 0
        length = all[0].size[0]
        height = all[0].size[1]
        for x in range (0, length, 3):
            for y in range(0, height, 3):
                rgb = all[0].getpixel((x,y))
                hsv = colorsys.rgb_to_hsv(rgb[0], rgb[1], rgb[2])
                if (hsv[0] >= 0 and hsv[0] <=360 and hsv[1] >= 0 and hsv[1]<=0.1  and hsv[2] >= 190 and hsv[2] <=255):
                    avgx += x
                    avgy += y
                    valid_white += 1
        if (valid_white > 0):
            avgx = avgx/valid_white
            avgy = avgy/valid_white
            filename2 = all[2]
            counter =  int(filename2[(filename2.rindex("\\") + 2) : filename2.rindex(".")])
            if (all[1] == "A"):
                coordinates_list.append((avgx, avgy, (-0.385 * avgy) + 250, counter))
            # elif (all[1] == "B"):
            #     coordinates_list.append(((avgy + 1942) / 2.825, avgy, avgx, counter))
            elif (all[1] == "C"):
                coordinates_list.append((length - avgx, avgy, 500 - (250 + (avgy * -0.385)), counter))
            # elif (all[1] == "D"):
            #     coordinates_list.append(((avgy - 1730) / -2.825, avgy, avgx, counter))
        else:
            counter =  int(filename2[(filename2.rindex("\\") + 2) : filename2.rindex(".")])
            coordinates_list.append((coordinates_list[len(coordinates_list) - 1][0] + 10, coordinates_list[len(coordinates_list) - 1][1] + 10, coordinates_list[len(coordinates_list) - 1][2] + 10, counter))
    fileName2 = folder[0:folder.rfind("\\")]
    fileName2 = folder[0:fileName2.rfind("\\")]
    fileName2 = fileName2 + "/coordinates.txt"
    file1 = open(fileName2, "w") 

    for all in coordinates_list:
        str1 = "(" + str(round(all[0])) + "," + str(round(all[1])) + "," + str(round(all[2])) + "," + str(round(all[3])) + ")"
        file1.write(str1)
        file1.write("\n")
    file1.close() 

def enhanceZ(filePath):
    f = open(filePath, "r") 
    coordList = []
    s = f.readline()
    while (s != ""):
        newTup = list(eval(s))
        newTup = tuple(newTup)
        coordList.append(newTup)
        s = f.readline()
    for x in range(coordList):
        coordList[x][2] = 
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
    f = open(filePath, "r") 
    coordList = []
    s = f.readline()
    while (s != ""):
        newTup = list(eval(s))
        newTup = tuple(newTup)
        coordList.append(newTup)
        s = f.readline()
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
    f = open(filePath, "r") 
    coordList = []
    s = f.readline()
    while (s != ""):
        newTup = list(eval(s))
        newTup = tuple(newTup)
        coordList.append(newTup)
        s = f.readline()
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
# mergePics(r"C:\Users\joelj\OneDrive\Desktop\BinaryChristmasTree\XYPics\*.png")
createXYZ(r"C:\Users\joelj\OneDrive\Desktop\BinaryChristmasTree\XYPics\*.png")
sortX(r"C:\Users\joelj\OneDrive\Desktop\BinaryChristmasTree\coordinates.txt")