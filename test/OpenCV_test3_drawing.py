import cv2

img = cv2.imread("assets/peaceful_scenic.jpg")
#BORDER
img = cv2.copyMakeBorder(img, 20, 20, 20, 20, borderType = cv2.BORDER_CONSTANT, value = (100,0,0))

#LINE
img = cv2.line(img, (575,704), (527,823), color=(0,200,0), thickness = 10)

#ARROW
img = cv2.arrowedLine(img, (517,610), (470, 905), color=(0,0,150), thickness = 10) 

#CIRCLE
img = cv2.circle(img, center=(329,493), color=(100,100,200), radius = 40, thickness = 3)

#ELLIPSE

#RECTANGLE

#TEXT


cv2.imshow("This is what you want",img)
cv2.waitKey(0)
cv2.destroyAllWindows()