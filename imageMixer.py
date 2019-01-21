import pyautogui as gui
import os, pygame
from PIL import Image

width,height = 640,400

pygame.init()
screen = pygame.display.set_mode((width,height))
screen.set_alpha(None)

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

pics = []
for pic in os.listdir("Images"):
    pic = Image.open("Images/" + str(pic))
    pic = pic.convert('RGB')
    pic = pic.resize((640,400))
    pics.append(pic)

arrayMain = make_new_array(pics[0]) #make array with starting pixels
pics.remove(pics[0]) #remove first picture

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
        picPtr += 1

make_new_pic()

for pixel in arrayMain: #draw pixels
    pixel.RGB[0] = pixel.RGB[0]/(len(pics)+1) #add one because we removed the first picture
    pixel.RGB[1] = pixel.RGB[1]/(len(pics)+1)
    pixel.RGB[2] = pixel.RGB[2]/(len(pics)+1)
    if pixel.RGB[0] > 255: 
        pixel.RGB[0] = pixel.RGB[0] - (pixel.RGB[0]-255)
    if pixel.RGB[1] > 255: 
        pixel.RGB[1] = pixel.RGB[1] - (pixel.RGB[1]-255)
    if pixel.RGB[2] > 255: 
        pixel.RGB[2] = pixel.RGB[2] - (pixel.RGB[2]-255)
    screen.set_at((pixel.x, pixel.y), pixel.RGB)
    
pygame.display.flip()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
