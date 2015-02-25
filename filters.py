import numpy as np
import cv2

def Gaussian(image, ksize, sigmaX, sigmaY):
    image = cv2.GaussianBlur(image, ksize, sigmaY)
    return image

def Median(image, ksize):
    image = cv2.medianBlur(image, ksize)
    return image

def bilFilter(image, d, sigmaColor, sigmaSpace):
    image = cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)
    return image

"""
def Kuwakara(image, ksize):
    height, width, depth = image.shape
    out = np.zeros(image.shape, np.uint8)
    dt = ksize / 2
    if image.nChannels == 1:
        for y in range(2 * dt, height - 2 * dt):
            ptr = image.imageData + y * image.widthStep
            p_out = out
            cv2.get
    return image

"""