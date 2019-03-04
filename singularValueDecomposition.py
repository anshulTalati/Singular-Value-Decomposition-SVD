# -*- coding: utf-8 -*-
"""
Spyder Editor

@creator : anshulTalati
"""

# Import all the library , numpy is used for matrix operations and PIl is used for image to pixel array conversion and vice versa  
from PIL import Image
import numpy as np

# Reading the Image into Matrix.
im = Image.open('ruler.512.tiff')
imageArray = np.array(im)

# Taking the input of Rank from the user for image Regeneration.
rank = int(input("Please Enter the value of rank you to use to generate the image \n ") )

# Calling svd function of nupy to calcuate the u, s and vtranspose.
u , s, vh = np.linalg.svd(imageArray)

# modifing the S-matrix acc. to the Given Rank and diagonal matrix
s = s[:rank]
smat = np.diag(s)

# Applying the rank to Matrices u and v
u = u[:,:rank]
vh = vh[:rank,:]


# matrix multiplication and generating the array for the image generation 
umuls= np.dot(u, smat )
R = np.dot(np.dot(u, smat ),vh )
print R.shape

# Generation Image from the Array.
im1 = Image.fromarray(np.uint8(R),'L')
im1.show()
