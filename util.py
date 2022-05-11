from config import PHOTO_FOLDER_PATH
import cv2 as cv

#functie careia ii dam doar numele imaginii si o returneaza
def get_image(image_name):
    img_path = PHOTO_FOLDER_PATH + '\\' + image_name
    image = cv.imread(img_path)

    cv.imshow("original_image", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return image