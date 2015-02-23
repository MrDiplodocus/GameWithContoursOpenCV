import numpy as np
import cv2

def Gaussian(image):
    image = cv2.GaussianBlur(image, (5, 5), 0)
    return image

def Median(image):
    image = cv2.medianBlur(image, 5)
    return image

def bilFilter(image):
    image = cv2.bilateralFilter(image, 9, 75, 75)
    return image