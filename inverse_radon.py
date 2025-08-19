from __future__ import print_function, division
from skimage.transform import iradon_sart
from skimage.transform import iradon
import numpy as np
import matplotlib.pyplot as plt
import skimage
from scipy import ndimage, misc
from skimage.transform import radon, rescale
image = skimage.data.shepp_logan_phantom() #Original Image
theta = np.arange(0., 360., 1.0)
sinogram = radon(image, theta=theta, circle=True)
plt.title('Original Image')
plt.imshow(image, cmap = 'gray')
plt.figure()

plt.title("Radon transform\n(Sinogram)")
plt.xlabel("Projection angle (deg)")
plt.ylabel("Projection position (pixels)")
plt.imshow(sinogram, cmap='gray') #sinogram
plt.figure()
           
reconstruction_fbp1 = iradon(sinogram, theta=theta, filter_name='ramp')
plt.title("Reconstruction Filtered back projection with ramp filter")
plt.imshow(reconstruction_fbp1, cmap='gray')
plt.figure()

reconstruction_fbp2 = iradon(sinogram, theta=theta, filter_name='shepp-logan')
plt.title("Reconstruction with shepp-logan filter")
plt.imshow(reconstruction_fbp2, cmap='gray')
plt.figure()

reconstruction_fbp3 = iradon(sinogram, theta=theta, filter_name='cosine')
plt.title("Reconstruction with cosine filter")
plt.imshow(reconstruction_fbp3, cmap='gray')
plt.figure()

reconstruction_fbp4 = iradon(sinogram, theta=theta, filter_name='hamming')
plt.title("Reconstruction with hamming filter")
plt.imshow(reconstruction_fbp4, cmap='gray')
plt.figure()

reconstruction_fbp5 = iradon(sinogram, theta=theta, filter_name='hann')
plt.title("Reconstruction with hann filter")
plt.imshow(reconstruction_fbp5, cmap='gray')
plt.figure()


