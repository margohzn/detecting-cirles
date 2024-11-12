import cv2
import numpy as np

ghost_image = cv2.imread("ghost.png")
blob_image = cv2.imread("blobs.jpeg")

#detection of shapes - 1.image reading 2.turn image to greyscale 3.blurring image 4.detecting shape from blurred image 5.drawing detected shapes

#converting colored image to greysclae
grayscale_ghost = cv2.cvtColor(ghost_image, cv2.COLOR_BGR2GRAY)

greyscale_blur_ghost = cv2.blur(grayscale_ghost, (3,3))

detected_circle = cv2.HoughCircles(greyscale_blur_ghost, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 1, maxRadius = 40)

if detected_circle is not None:
    detected_circle = np.uint16(np.around(detected_circle))
    for i in detected_circle[0,:]:
        a, b, r = i[0], i[1], i[2]
        cv2.circle(ghost_image, (a,b), 1, (2,255,0), 2)
        cv2.circle(ghost_image, (a,b), r, (2,255,0), 2)
        cv2.imshow("Ghost Image", ghost_image)
        cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows