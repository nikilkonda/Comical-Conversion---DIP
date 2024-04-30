import cv2


def remove_background(image_path):

    image = cv2.imread(image_path)


    if image is None:
        print("Error: Unable to load image.")
        return None


    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    gray = cv2.equalizeHist(gray)


    edges = cv2.Canny(gray, 30, 150)


    mask = cv2.bitwise_not(edges)


    result_image = cv2.bitwise_and(image, image, mask=mask)

    return result_image



image_path = 'image4.jpeg'


result_image = remove_background(image_path)


if result_image is not None:

    cv2.imshow('Background Removed', result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
