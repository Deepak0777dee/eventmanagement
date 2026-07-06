from PIL import Image
import os
import shutil

source = r"C:\Users\D-ROCK\.gemini\antigravity-ide\brain\aee69407-1aac-40e3-85b0-e182f05e0a8e\interactive_map_bg_1783335037533.png"
dest = r"c:\Users\D-ROCK\Desktop\eventmanagement\images\map_bg.webp"

img = Image.open(source)
img.save(dest, "webp")
print("Image converted to webp successfully!")
