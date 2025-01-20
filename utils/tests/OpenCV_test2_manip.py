import cv2
import numpy as np 

img = cv2.imread("assets/peaceful_scenic.jpg")


#RESIZE
img = cv2.resize(img, (400, 800))
img = cv2.resize(img, (0,0), fx = 2, fy = 1)

#CROP
height, width = img.shape[0], img.shape[1]
img = img[int(height/3) : height,50 : -50]  #img is 2D Array
                                            # ":" is slice notation
                                            # 0,0 is top left of img


#ROTATE
height, width = img.shape[0], img.shape[1]
img = cv2.rotate(img, cv2.ROTATE_180)

M = cv2.getRotationMatrix2D(center=(width/2, height/2), angle = 150, scale = 1) #rotation matrix, maps the pixels to where they need to be

img = cv2.warpAffine(img, M, (width,height))

#TRANSLATE
tx = width / 5
ty = height / 2
 #translation matrix
M = np.array([
    [1,0,tx],
    [0,1,ty]
]) #does matrix mulitplication in warpAffine function

img = cv2.warpAffine(img, M, (width,height))


cv2.imshow("This is what you want", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
