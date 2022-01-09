from PIL import Image
import time
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
                    print (coordList[x][position])
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
    return sortSecondary(coordList, 0)
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
    return sortSecondary(coordList, 1)

def reverseCoords(filePath):
    f = open(filePath, "r") 
    coordList = []
    s = f.readline()
    while (s != ""):
        coordList.append(eval(s))
        s = f.readline()
    f = open("C:/Users/joelj/OneDrive/Desktop/BinaryChristmasTree/coordinates.txt", "r+") 
    f.seek(0) 
    f.truncate() 
    f.close()
    f = open("C:/Users/joelj/OneDrive/Desktop/BinaryChristmasTree/coordinates.txt", "w") 
    coordList.reverse()
    for all in (coordList):
        f.write(str(all))
        f.write("\n")
    f.close()
sortedY = sortY("C:/Users/joelj/OneDrive/Desktop/BinaryChristmasTree/coordinates.txt")
print (sortedY)
f = open("C:/Users/joelj/OneDrive/Desktop/BinaryChristmasTree/coordinates.txt", "r+") 
f.seek(0) 
f.truncate() 
f.close()

f = open("C:/Users/joelj/OneDrive/Desktop/BinaryChristmasTree/coordinates.txt", "w") 

for all in (sortedY):
    f.write(str(all))
    f.write("\n")

f.close()
time.sleep(1)
reverseCoords("C:/Users/joelj/OneDrive/Desktop/BinaryChristmasTree/coordinates.txt")


