
'''
myjptr
Resize images and set all extensions same
'''

import numpy as np
import cv2
import os
from PIL import Image

dir_path = os.getcwd()


for filename in os.listdir(dir_path):
    
    image = cv2.imread(filename)
    
    if image is not None:
            resized = cv2.resize(image, (400,400),interpolation=cv2.INTER_AREA)
            cv2.imwrite(filename,resized)
    else:
        print("image not loaded")
        print(filename)

    if filename.endswith(".jpg"):
        
        continue  
        
    else:
        name, extension = os.path.splitext(os.path.join(dir_path + filename))
        im = cv2.imread(filename)
        cv2.imwrite(name + '.jpg',im)
        os.remove(name+extension)
