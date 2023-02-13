import matplotlib.pyplot as plt
import PIL
import time
from matplotlib.image import imread
from PIL import Image

start = time.time()


image = imread("drift.jpg")
pixel_image = PIL.Image.open("drift.jpg")
pixel_image_rgb = pixel_image.convert("RGB")

width = image.shape[0]
height = image.shape[1]

def convertToBinary(x):
    rgb = ""
    real = [128, 64, 32, 16, 8, 4, 2, 1]

    for i in range (8):
        if x >= real[i]:
            rgb += "1"
            x = x - real [i]
        else:
            rgb += "0"
    return str(rgb)

def findPixel(pixel_image_rgb):
    final = ""
    f = open('enjoy.txt','w')
    for i in range (width):
        for j in range (height):
            
            pixel = pixel_image_rgb.getpixel((j, i))
            
            r,g,b = pixel[0], pixel[1], pixel[2]
            final = convertToBinary(r) + convertToBinary(g) + convertToBinary(b)
            f.write(final)
            
    f.close()


print("The width is " + str(width) + " and the height is " + str(height) + ", meaning that there are " +  str(width * height) + " pixels in total")
print("Each pixel contains 3 bytes (24 bits), therefore this image must have " + str(width * height * 24) + " 1's and 0's")
#print("This image's 'binary length' is " + str(len(findPixel(pixel_image_rgb))))
findPixel(pixel_image_rgb)



end = time.time()
print(end-start)

