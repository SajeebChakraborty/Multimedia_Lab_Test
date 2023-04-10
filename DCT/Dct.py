import numpy as np
from PIL import Image
from scipy.fftpack import dct

# Load the image and convert to grayscale
image = Image.open('image.jpg').convert('L')

# Convert the image to a NumPy array
image_array = np.array(image)

# Pad the image to ensure its dimensions are divisible by 8
h, w = image_array.shape
H, W = (h + 7) // 8 * 8, (w + 7) // 8 * 8
padded_image = np.zeros((H, W))
padded_image[:h, :w] = image_array

# Split the image into 8x8 blocks
blocks = padded_image.reshape(H // 8, 8, -1, 8).swapaxes(1, 2)

# Compute the 2D DCT for each block
dct_blocks = np.zeros_like(blocks)
for i in range(blocks.shape[0]):
    for j in range(blocks.shape[2]):
        dct_blocks[i, :, j, :] = dct(dct(blocks[i, :, j, :].T, norm='ortho').T, norm='ortho')

# Flatten the DCT coefficients for each block into a 1D array
dct_coeffs = dct_blocks.reshape(-1, 64)

# Quantize the DCT coefficients using a standard JPEG quantization table
quant_table = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                        [12, 12, 14, 19, 26, 58, 60, 55],
                        [14, 13, 16, 24, 40, 57, 69, 56],
                        [14, 17, 22, 29, 51, 87, 80, 62],
                        [18, 22, 37, 56, 68, 109, 103, 77],
                        [24, 35, 55, 64, 81, 104, 113, 92],
                        [49, 64, 78, 87, 103, 121, 120, 101],
                        [72, 92, 95, 98, 112, 100, 103, 99]])
quant_coeffs = np.round(dct_coeffs / quant_table.reshape(-1))

# Convert the quantized DCT coefficients back into blocks
quant_blocks = quant_coeffs.reshape(blocks.shape)

# Save the quantized DCT coefficients to a file
np.save('dct_coeffs.npy', quant_coeffs)
