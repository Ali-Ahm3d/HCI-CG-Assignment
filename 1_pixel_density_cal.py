import math

# Input
horizontal_pixels = int(input("Enter horizontal resolution (pixels): "))
vertical_pixels = int(input("Enter vertical resolution (pixels): "))
diagonal = float(input("Enter physical diagonal size (inches): "))

# Total pixel count
total_pixels = horizontal_pixels * vertical_pixels

# Aspect ratio
gcd = math.gcd(horizontal_pixels, vertical_pixels)
aspect_width = horizontal_pixels // gcd
aspect_height = vertical_pixels // gcd

# Calculate DPI
dpi = math.sqrt(horizontal_pixels**2 + vertical_pixels**2) / diagonal

# Display results
print("\n--- DISPLAY METRICS ANALYSIS ---")
print(f"Total Pixel Count: {total_pixels:,}")
print(f"Aspect Ratio: {aspect_width}:{aspect_height}")
print(f"Calculated DPI: {dpi:.2f}" " DPI")

# Density classification
if dpi < 100:
    density = "Low density (Standard Monitor)"
elif dpi <= 200:
    density = "Medium density (HD display)"
else:
    density = "High density (Retina mobile)"
print(f"Density Category: {density}\n")