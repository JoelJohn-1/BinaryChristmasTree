import glob
import colorsys
from PIL import Image
def coordinates():
    index = 0
    coordinates_list = []
    image_list = []
    for filename in glob.glob('C:/Users/joelj/OneDrive/Desktop/BinaryChristmasTree/LEDPics/*.png'):
        im=Image.open(filename)
        image_list.append(im)
    for all in image_list:
        avgx = 0
        avgy = 0
        valid_white = 0
        length = all.size[0]
        height = all.size[1]
        for x in range (0, length, 5):
            for y in range(0, height, 5):
                rgb = all.getpixel((x,y))
                hsv = colorsys.rgb_to_hsv(rgb[0], rgb[1], rgb[2])
                if (hsv[0] >= 0 and hsv[0] <= 360 and hsv[1] >= 0 and hsv[1]<=25 and hsv[2] >= 150 and hsv[2] <=255):
                    #Hue 0 to 100%, Sat 0 to 10% & Val 50% to 100%
                    avgx += x
                    avgy += y
                    valid_white += 1
        avgx = avgx/valid_white
        avgy = avgy/valid_white
        coordinates_list.append((avgx,avgy))
        index = index + 1
    return coordinates_list

list = coordinates()
print(list)
file1 = open("C:/Users/joelj/OneDrive/Desktop/BinaryChristmasTree/coordinates.txt", "w") 

for all in list:
    str1 = "(" + str(round(all[0])) + "," + str(round(all[1])) + ")"
    file1.write(str1)
    file1.write("\n")
file1.close() 