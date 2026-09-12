import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Create a 300 x 400 x 3 image matrix filled with zeros
image = np.zeros((300, 400, 3), dtype=np.uint8)

# Get the middle points
row_end = 300
col_end = 400
row_mid = row_end // 2
col_mid = col_end // 2

# Top-left: Red
image[0:row_mid, 0:col_mid] = [255, 0, 0]

# Top-right: Green
image[0:row_mid, col_mid:col_end] = [0, 255, 0]

# Bottom-left: Blue
image[row_mid:row_end, 0:col_mid] = [0, 0, 255]

# Bottom-right: White
image[row_mid:row_end, col_mid:col_end] = [255, 255, 255]

# Display matrix information
print("\n--- SYNTHETIC METRIX METRICS ---")
print("Array Shape (H, W, C) :", image.shape)
print("Data Type :", image.dtype)
print("Total Elements :", image.size, "Values")
print("Memory Footprint :", image.nbytes, "bytes (351.56 KB)")

# Display the image
plt.imshow(image)
plt.axis("off")
plt.show()