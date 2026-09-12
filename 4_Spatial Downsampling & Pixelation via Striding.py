import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

# Step factor
N = 8

# Find sample.jpg in the same folder as this Python file
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "sample.jpg")

# 1. Load input image into NumPy array
img = np.array(Image.open(image_path))

# Make sure image has RGB channels
if img.ndim != 3 or img.shape[2] != 3:
    raise ValueError("Input image must be an RGB image.")

# Original dimensions and memory
original_shape = img.shape
original_memory = img.nbytes

# 2. Downsample using NumPy striding
downsampled = img[::N, ::N, :]

# Downsampled dimensions and memory
downsampled_shape = downsampled.shape
downsampled_memory = downsampled.nbytes

# 3. Re-expand using np.repeat() across axes 0 and 1
reexpanded = np.repeat(
    np.repeat(downsampled, N, axis=0),
    N, axis=1
)

# Crop to exactly match the original dimensions
reexpanded = reexpanded[:img.shape[0], :img.shape[1], :]

# 4. Calculate reductions

# Percentage reduction per spatial axis
row_reduction = (1 - downsampled.shape[0] / img.shape[0]) * 100
column_reduction = (1 - downsampled.shape[1] / img.shape[1]) * 100

# Memory reduction
memory_savings = (1 - downsampled_memory / original_memory) * 100

# 5. Print analysis
print(f"--- DOWNSAMPLING ANALYSIS (N = {N}) ---")
print(
    f"Original Shape : {original_shape} | "
    f"Memory: {original_memory:,} bytes"
)
print(
    f"Downsampled Shape : {downsampled_shape} | "
    f"Memory: {downsampled_memory:,} bytes"
)
print(
    f"Re-expanded Shape : {reexpanded.shape} | "
    f"Visual: Blocky Pixelation"
)
print(
    f"Dimension Reduction: "
    f"{row_reduction:.2f}% reduction per axis"
)
print(
    f"Memory Savings : "
    f"{memory_savings:.2f}% data reduction"
)

# 6. Display original and pixelated images
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(reexpanded)
plt.title(f"Pixelated Image (N = {N})")
plt.axis("off")

plt.tight_layout()
plt.show()
