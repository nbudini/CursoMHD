import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import random

# Define image size
image_size = 101

# Create randomly distributed delta functions as ideal point sources
delta = np.zeros((image_size, image_size))
for x in range(6):
    delta[int(random.choice(np.linspace(1,101,101))), int(random.choice(np.linspace(1,101,101)))] = 1

# Define a simple Gaussian blur PSF
sigma = 5  # Adjust sigma for different blur levels
x = np.linspace(-image_size // 2, image_size // 2, image_size)
y = np.linspace(-image_size // 2, image_size // 2, image_size)
X, Y = np.meshgrid(x,y)
psf = np.exp(-(X**2 + Y**2) / (2 * sigma**2))
#psf /= np.max(psf)  # Normalize PSF for total intensity of 1

# Simulate the blurred image by convolving the point source with the PSF
blurred_image = signal.convolve2d(delta, psf, 'same')

# Plot the ideal point source, PSF, and blurred image
plt.figure(figsize=(10, 6))

# Plot ideal point sources (delta function)
plt.subplot(1, 3, 1)
plt.imshow(delta, cmap='hot')
plt.title('Ideal Point Sources')
plt.axis('off')

# Plot the PSF
plt.subplot(1, 3, 2)
plt.imshow(psf, cmap='hot')
plt.title('Point Spread Function (PSF)')
plt.axis('off')

# Plot the blurred image
plt.subplot(1, 3, 3)
plt.imshow(blurred_image, cmap='hot')
plt.title('Output Image')
plt.axis('off')

# Adjust layout and titles
plt.suptitle('PSF Visualization')
plt.tight_layout()
plt.show()
