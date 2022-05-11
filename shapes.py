import cv2 as cv
from matplotlib import image
from image_processing import binarize


def get_shapes(img):
    image = img
    binarized_image = binarize(img)
    # cautam contururile din poza
    contours, _ = cv.findContours(binarized_image, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    cv.drawContours(image, contours, -1, (0, 255, 0), 3)
    

    return contours, image