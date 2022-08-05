from distutils import text_file
import numpy as np
from PIL import Image

def write_pixel(t, handle):
    handle.write("%d, "%t)

def write_pixel_col(t, handle):
    handle.write("%d %d, "%(t[0],t[1]))


def img_to_array(path,chroma):
    text_file_handle = open("out.txt","w")

    im = Image.open(path)

    width, height = im.size

    for column in range(0,width):
        for row in range(0,height):
            if (chroma == 1):
                write_pixel(im.getpixel((column,row)), text_file_handle)
            else:
                write_pixel_col(im.getpixel((column,row)), text_file_handle)
            text_file_handle.write("\n")

    text_file_handle.close()
    print ("Data Succesfully updated")


path = "gray.jpg"
chroma = int(input("Enter 1 if image is grayscale. Otherwise Enter 2 : "))

img_to_array(path,chroma)

