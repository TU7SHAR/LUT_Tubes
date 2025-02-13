import cv2
import numpy as np
import random

# Load the image
image = cv2.imread('image.png')

# Check if the image is loaded properly
if image is None:
    raise ValueError("Image not found. Please check the file path.")

# Create a 3-channel LUT to add a hazy background and sharp foreground
lookup_table = np.zeros((256, 1, 3), dtype=np.uint8)
for i in range(256):
    lookup_table[i, 0, 0] = min(255, int(i * 0.8) + 20)  # Red channel
    lookup_table[i, 0, 1] = min(255, int(i * 0.8) + 20)  # Green channel
    lookup_table[i, 0, 2] = min(255, int(i * 0.8) + 20)  # Blue channel

# Apply the LUT to the image
output_image = cv2.LUT(image, lookup_table)

# Save the output image
r_name = "output_img"+str(random.randint(1,10000))+".jpg"
print(r_name)
cv2.imwrite(r_name, output_image)
