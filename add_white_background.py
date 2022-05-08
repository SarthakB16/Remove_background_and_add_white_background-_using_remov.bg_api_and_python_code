
import numpy as np
import cv2
from PIL import Image

# creating array using np.zeroes()
array = np.zeros([500, 500, 3],
                 dtype = np.uint8)
  
# setting RGB color values as 255,255,255
array[:, :] = [255, 255, 255] 
  
# displaying the image
cv2.imshow("image", array)
cv2.waitKey(0)
cv2.imwrite('white-bg.png',array)


img1 = Image.open(r"white-bg.png")
img2 = Image.open(r"no-bg.png")
  
# Pasting img2 image on top of img1 
# starting at coordinates (0, 0) 
# simulating an raster overlay
img1.paste(img2, (0,0), mask = img2)
img1.save("final_picture.png")
img1.show()
