# Encode.py

import PIL
from PIL import Image
import requests
from io import BytesIO
from PIL import ImageFilter
from PIL import ImageEnhance
from IPython.display import display
import numpy as np

# This is actually pseudocode, reference only
def GetFrameAsArray(PILImage):
	result = []
	for x in range(PILImage.width):
		for y inrange(PILImage.height):
			scanline = []
			scanline.append(PILImage.getpixel((x, y)))
	return result