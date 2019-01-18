import pyautogui as gui
import numpy as np
import os, pygame
from PIL import Image

imageFile = open("image.txt","w")

pic = Image.open('image.jpeg')
pic = pic.convert('RGB')

width,height = pic.size
W_width, W_height = width,height

pygame.init()
screen = pygame.display.set_mode((W_width,W_height))
screen.set_alpha(None)

for y in range(0,height):
    for x in range(0,width):
        RGB = pic.getpixel((x,y))


        #screen.set_at((x,y), RGB)

#pygame.display.flip()

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