import numpy as np
import cv2 as cv
import sys


def binarize(img):
    gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # aplicam Gaussian Blur imaginii noastre
    gaussian_blured_image = cv.GaussianBlur(gray_image, (5, 5), 0)

    # binarizam imaginea folosind algoritmul Otsu de binarizare
    ret, th = cv.threshold(gaussian_blured_image, 0, 255,
                           cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

    cv.imshow("binarized_image", th)
    cv.waitKey(0)
    cv.destroyAllWindows()

    return th

#cropare imagine
def adjust_ROI(img):
    (h, w) = img.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    M = cv.getRotationMatrix2D((cX, cY), 2, 1.0)
    rotated = cv.warpAffine(img, M, (w, h))
    croped_image = rotated[390:915, 100:940]

    cv.imshow("rotated_image", croped_image)
    cv.waitKey(0)
    cv.destroyAllWindows()

    return croped_image


