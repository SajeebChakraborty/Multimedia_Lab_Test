import numpy as np
from scipy.fftpack import dct, idct
import matplotlib.pyplot as plt

# Generate a random gray level image of size 16x16
image = np.random.randint(0, 256, size=(16, 16))

# Apply DCT on the image
dct_image = dct(dct(image.T, norm='ortho').T, norm='ortho')

# Plot the transformed image
plt.figure()
plt.imshow(dct_image, cmap='gray')
plt.title('DCT Transformed Image')
plt.show()

# Apply IDCT on the transformed image
idct_image = idct(idct(dct_image.T, norm='ortho').T, norm='ortho')

# Plot the reconstructed image
plt.figure()
plt.imshow(idct_image, cmap='gray')
plt.title('IDCT Reconstructed Image')
plt.show()
