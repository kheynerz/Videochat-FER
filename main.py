import cv2 
import matplotlib.pyplot as plt 


"""
import tensorflow as tf 
import os
import pandas as pd
import numpy as np
"""


#OPEN CV CAN be used to read images and crop faces

if __name__ == "__main__":
    img_array = cv2.imread('train/angry/Training_3908.jpg')
    print(img_array)
    plt.imshow(img_array)
    plt.show()