import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

# 1. Find sample.jpg in the same folder as this Python file
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "sample.jpg")

# Load input image
img = np.array(Image.open(image_path))

# 2. Extract 2D channel intensity grids using Axis 2 slicing
red = img[:, :, 0]
green = img[:, :, 1]
blue = img[:, :, 2]

# 3. Create isolated 3D color arrays
red_only = np.zeros_like(img)
green_only = np.zeros_like(img)
blue_only = np.zeros_like(img)

red_only[:, :, 0] = red
green_only[:, :, 1] = green
blue_only[:, :, 2] = blue

# 4. Channel Extraction Summary
print("--- CHANNEL EXTRACTION SUMMARY ---")
print(f"Original Image Shape : {img.shape}")
print(f"Red Channel 2D Shape : {red.shape} | Mean Intensity: {red.mean():.2f}")
print(f"Green Channel 2D Shape: {green.shape} | Mean Intensity: {green.mean():.2f}")
print(f"Blue Channel 2D Shape : {blue.shape} | Mean Intensity: {blue.mean():.2f}")

# 5. Display 2 × 3 subplot
fig, axes = plt.subplots(2, 3, figsize=(14, 8))

# Top row - isolated color images
axes[0, 0].imshow(red_only)
axes[0, 0].set_title("Red-Only")

axes[0, 1].imshow(green_only)
axes[0, 1].set_title("Green-Only")

axes[0, 2].imshow(blue_only)
axes[0, 2].set_title("Blue-Only")

# Bottom row - grayscale intensity maps
axes[1, 0].imshow(red, cmap="gray")
axes[1, 0].set_title("Red Intensity")

axes[1, 1].imshow(green, cmap="gray")
axes[1, 1].set_title("Green Intensity")

axes[1, 2].imshow(blue, cmap="gray")
axes[1, 2].set_title("Blue Intensity")

# Hide axes
for ax in axes.flat:
    ax.axis("off")

plt.tight_layout()

print("Display Window : Matplotlib 2x3 Subplot Grid Rendered.")

plt.show()

