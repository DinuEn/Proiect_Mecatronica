import cv2 as cv
from shapes import get_shapes
from util import get_image
from image_processing import adjust_ROI


def main():
    original_image = get_image('poza_cerc4.bmp')
    rotated_image = adjust_ROI(original_image)
    contours, image = get_shapes(rotated_image)

    print("Imaginea are " + str(len(contours)) + " contururi")
    index = 1

    for contour in contours:
        rightmost = tuple(contour[contour[:,:,0].argmax()][0])
        font = cv.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (rightmost)
        fontScale = 1
        fontColor = (255, 0, 0)
        thickness = 3
        lineType = 2
        
        

        cv.putText(image, str(index),
                    bottomLeftCornerOfText,
                    font,
                    fontScale,
                    fontColor,
                    thickness,
                    lineType)

        index = index + 1

    cv.imshow("contours", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

    print("Introduceti numarul celor 2 contururi de comparat")
    first_number = int(input())
    second_number = int(input())
    print(cv.matchShapes(contours[first_number-1],
          contours[second_number-1], 1, 0.0))


if __name__ == "__main__":
    main()
