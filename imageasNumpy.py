import os.path
from skimage.io import imread

file_path="checker_bilevel.png"
img = imread(file_path)
print(img)
print(type(img))
print(img.ndim)
print(img.shape)
print(img.size)
print(img.itemsize)
print(img.all)
print(img.nbytes)

 
''' assuming you have read the image in variable img '''
# Transpose
img_t = img.T
print(img_t)
# Reshape
img_reshape = img.reshape(5, 20)
# Sort
img_srt = img.copy()
img_srt.sort(axis = 0) 
# Compression
img_cmp = img.copy()
img_cmp = img_cmp.compress([True,False,True,0,1,1,1,0,0,1],axis = 0)
print(img_cmp.shape)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
file_path="checker_bilevel.png"
img = imread(file_path)
plt.imshow(img, cmap="Greys")
plt.imshow(img)
plt.show()

img_slice= img.copy()
img_slice=img_slice[788:300,360:480]
plt.figure()
plt.imshow(img_slice)
plt.show()


 
img_slice[np.greater_equal(img_slice[:,0],100) & np.less_equal(img_slice[:,0],150)] = 0
plt.figure()
plt.imshow(img_slice)
plt.show()
