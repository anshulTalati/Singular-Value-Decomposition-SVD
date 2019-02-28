# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PIL import Image
im = Image.open('ruler.512.tiff')
#im.show()

#import math
import numpy as np
imageArray = np.array(im)
#imageArray.shape
#imageArray.size

#imageArray = np.array([[2,4],[1,3],[0,0],[0,0]])
print imageArray 

imageArray_T = imageArray.transpose()
 
print imageArray_T

w, v = np.linalg.eig(np.dot(imageArray, imageArray_T))

x, y = np.linalg.eig(np.dot(imageArray_T, imageArray))

z= np.sqrt(w)

#S= np.array(z)
print v.shape
print y.shape 
print z.shape

R = np.dot(v, z, y)

#
#mage.fromarray(imarray)
#<Image.Image image mode=L size=330x44 at 0x2786518>