#!/usr/bin/env python3

from PIL import Image

# Open webp image
im = Image.open(r'C:\Users\nhorn\Documents\Code\PhotoConverter\Github.webp')

# Make same size white background to paste it onto
bg = Image.new('RGB', im.size, 'white')

# Check if image has an alpha channel
if im.mode == 'RGBA':
    # Use the alpha channel as a mask for pasting
    mask = im.split()[3]  # The alpha channel is the 4th channel
    # Paste the webp with alpha onto the white background using the alpha channel as a mask
    bg.paste(im, (0, 0), mask)
else:
    # If no alpha channel, paste without a mask
    bg.paste(im)

bg.save(r'C:\Users\nhorn\Documents\Code\PhotoConverter\Github.jpg')


