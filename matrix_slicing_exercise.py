import matplotlib.pyplot as plt
from skimage.io import imread
import numpy as np

file_path="phantom.png"
img= imread(file_path)
plt.figure(figsize=(6, 6))
plt.title("Original Image")
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.imshow(img)
plt.show()


# Perform black and white thresholding
threshold = 0.15
new_img = np.where(img <= threshold, 0, 1)

plt.figure(figsize=(6, 6))
plt.title("Thresholded Image")
plt.imshow(new_img, cmap='gray')
plt.axis('off')
plt.show()

mirror_image=np.fliplr(img)
plt.figure(figsize=(6, 6))
plt.title("Mirror Image")
plt.imshow(mirror_image, cmap='gray')
plt.axis('off')
plt.show()


# Compress the flipped image along both axes by 50%
compressed_x = mirror_image[:, ::2]
compressed_xy = compressed_x[::2, :]

# Show the compressed image
plt.figure(figsize=(6, 6))
plt.title("Compressed Image")
plt.imshow(compressed_xy, cmap='gray')
plt.axis('off')
plt.show()