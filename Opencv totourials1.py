import cv2 as cv
img = cv.imread(r"C:\Users\rahul\PycharmProjects\Yt videos\Opencv\pexels-shvetsa-4588011.jpg")
cv.imshow("Dog",img)


def size(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    hight = int(frame.shape[0]*scale)
    dimension = (width,hight)

    return cv.resize(frame,dimension,interpolation= cv.INTER_AREA)




    cv.waitKey(0)
# # capture = cv.VideoCapture(r"C:\Users\rahul\PycharmProjects\Yt videos\Opencv\3039978-uhd_3840_2160_30fps.mp4")
# #
# # while True:
# #     isTrue, frame = capture.read()
# #
# #
# #     if isTrue:
# #         cv.imshow('Video', frame)
# #         if cv.waitKey(20) & 0xFF == ord('d'):
# #             break
# #     else:
# #         break
# #
# # capture.release()
# # cv.destroyAllWindows()
# #
# # capture.release()
# capture = cv.VideoCapture(0)
#
# while True:
#     isTrue, frame = capture.read()
#
#     # if cv.waitKey(20) & 0xFF==ord('d'):
#     # This is the preferred way - if `isTrue` is false (the frame could
#     # not be read, or we're at the end of the video), we immediately
#     # break from the loop.
#     if isTrue:
#         cv.imshow('Video', frame)
#         if cv.waitKey(20) & 0xFF == ord('d'):
#             break
#     else:
#         break
#
# capture.release()
# cv.destroyAllWindows()