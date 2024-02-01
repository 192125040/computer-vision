import cv2
image = cv2.imread("E:/Computer_Vision/Ex3.jpg", cv2.IMREAD_GRAYSCALE)  
edges = cv2.Canny(image, threshold1=30, threshold2=100)
cv2.imshow('Original Image', image)
cv2.imshow('Canny Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
