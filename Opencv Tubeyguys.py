import cv2 as cv
pic = r"C:\Users\rahul\PycharmProjects\Yt videos\Opencv\Tuubeyguys.jpg"
pictures = cv.imread(pic)
cv.imshow("Tubeyguys",pictures)
x = cv.cvtColor(pictures,cv.COLOR_BGR2GRAY)
cv.imshow("x,x",x)
cv.waitKey(0)

cv.destroyAllWindows()