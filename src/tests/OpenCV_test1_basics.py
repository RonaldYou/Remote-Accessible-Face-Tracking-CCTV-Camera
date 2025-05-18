import cv2

img = cv2.imread("assets/peaceful_scenic.jpg", cv2.IMREAD_UNCHANGED)
print(img.shape)
print(img[0,0])

cv2.imshow("This is what you want", img)
cv2.waitKey(0)
cv2.destroyAllWindows()