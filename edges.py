import cv2

img = cv2.imread('lena.jfif')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_sobelx= cv2.Sobel(img_gray,-1,1,0)
img_sobely= cv2.Sobel(img_gray,-1,0,1)
img_sobel = cv2.addWeighted(img_sobelx,0.5,img_sobely,0.5,0)

img_scharr = cv2.Scharr(img_gray,-1,1,0)
img_laplacian= cv2.Laplacian(img_gray,-1)
img_canny = cv2.Canny(img_gray,50,100)


cv2.imshow('Original iamge',img)
cv2.waitKey(0)

cv2.imshow('Gray iamge',img_gray)
cv2.waitKey(0)

cv2.imshow('Sobelx image',img_sobelx)
cv2.waitKey(0)

cv2.imshow('Sobely image',img_sobely)
cv2.waitKey(0)

cv2.imshow('Sobel image',img_sobel)
cv2.waitKey(0)

cv2.imshow('Scharr iamge',img_scharr)
cv2.waitKey(0)

cv2.imshow('Laplacian image',img_laplacian)
cv2.waitKey(0)
cv2.imshow('Canny image',img_canny)

cv2.waitKey(0)
cv2.destroyAllWindows()