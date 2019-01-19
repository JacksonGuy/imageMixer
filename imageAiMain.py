import pyautogui as gui
#import numpy as np
import os, pygame
from PIL import Image

"""
remove this code
pic = Image.open('image.jpeg')
pic = pic.convert('RGB')
pic = pic.resize((800,600))

pic1 = Image.open('image1.jpeg')
pic1 = pic1.convert('RGB')
pic1 = pic1.resize((800,600))
"""

width,height = 800,600

pygame.init()
screen = pygame.display.set_mode((width,height))
#screen.set_alpha(None)

class pixel():
    def __init__(self,x,y,RGB):
        self.x, self.y = x,y
        self.RGB = (RGB) #tuple
        self.RGB = list(self.RGB) #now a list

def make_new_array(picture):
    a = []
    for y in range(0,height):
        for x in range(0,width):
            RGB = picture.getpixel((x,y))
            px = pixel(x,y,RGB)
            a.append(px)
    return(a)

#array1 = make_new_array(pic) #array of pixels and their colors for the first pic
#array2 = make_new_array(pic1)

pics = []
for pic in os.listdir("Images"):
    pic = Image.open("Images/" + str(pic))
    pic = pic.convert('RGB')
    pic = pic.resize((800,600))
    pics.append(pic)

arrayMain = make_new_array(pics[0]) #make array with starting pixels
pics.remove(pics[0])

def make_new_pic():
    picPtr = 0
    for pic in pics: #every pic in list
        a1 = make_new_array(pic) #make array of pixels from picture
        pixPtr = 0
        for pix, pixel in zip(a1, arrayMain): #iterate over every pixel in picture and pixels already in main array
            pixel.RGB[0] += pix.RGB[0] 
            pixel.RGB[1] += pix.RGB[1]
            pixel.RGB[2] += pix.RGB[2]

            pixPtr += 1
            print("Picture: " + str(picPtr) + ", Pixel: " + str(pixPtr))

make_new_pic()

for pixel in arrayMain: #draw pixels
    pixel.RGB[0] = pixel.RGB[0]/len(pics)+1
    pixel.RGB[1] = pixel.RGB[1]/len(pics)+1
    pixel.RGB[2] = pixel.RGB[2]/len(pics)+1
    if pixel.RGB[0] > 255: 
        pixel.RGB[0] = pixel.RGB[0] - (pixel.RGB[0]-255)
    if pixel.RGB[1] > 255: 
        pixel.RGB[1] = pixel.RGB[1] - (pixel.RGB[1]-255)
    if pixel.RGB[2] > 255: 
        pixel.RGB[2] = pixel.RGB[2] - (pixel.RGB[2]-255)
    print(pixel.RGB)
    screen.set_at((pixel.x, pixel.y), pixel.RGB)
    pygame.display.flip()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

"""
a = np.array([[1,2,3]])
b = np.array([[4,5,6]])
c = np.concatenate((a,b))
c
array([[1, 2, 3],
       [4, 5, 6]])
c[1][0]
4
c[0][0]
1
--------------------
a = np.array([[[1,2,3],[7,8,9]]])
b = np.array([[[1,2,3],[7,8,9]]])
d = np.concatenate((a,b))

d
array([[[1, 2, 3],          #this array for averaging example
        [7, 8, 9]],

       [[1, 2, 3],
        [7, 8, 9]]])

d[0][1][0]
7


array of pictures will consist of their colors
width = each pixel in picture
length = each picture

each array row has to be the same length, standard image size will be 800x600

[0,0,0],[1,1,1] this row contains the rgb value of (0,0) and (0,1) of pic 1
[1,2,3],[2,2,2] (0,0) and (0,1) of pic 2

to get average color for first pixel of pic 1 and 2 (use array from above)
(a[0,0] + b[1,0])/2
"""
