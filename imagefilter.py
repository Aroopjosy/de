import cv2 as cv
import sys
import numpy as np 

preview = 0
blur = 1
features = 2
canny = 3
# print(sys.argv)
features_pram = dict( maxCorners = 500,
                       qualityLevel = 0.2,
                       minDistance = 15,
                       blockSize = 9)

s=0
if(len(sys.argv) > 1):
    s= sys.argv[1]

# print(sys.argv)
window = 'image preview'
cv.namedWindow(window, cv.WINDOW_NORMAL)
image_filter = preview
alive = True
result =None

source = cv.VideoCapture(s)
while alive:
    has_frame, frame = source.read()
    if not has_frame:
        break
    frame = cv.flip(frame, 1)
    if image_filter == preview:
        result = frame
    elif image_filter == canny:
        result = cv.Canny(frame,80, 150)
    elif image_filter == blur:
        result = cv.blur(frame, (13,13))
    elif image_filter == features:
        result = frame
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        corners = cv.goodFeaturesToTrack(frame_gray, **features_pram)
        if corners is not None:
            for x, y in np.int32(corners).reshape(-1, 2):

                cv.circle(result, (x,y), 10, (0,255, 0),1)
    cv.imshow(window, result)

    key = cv.waitKey(1)
    if key == ord('Q') or key == ord('q') or key == 27:
        alive = False
    elif key == ord('C') or key == ord('c'):
        image_filter = canny
    elif key == ord('B') or key == ord('b'):
        image_filter = blur
    elif key == ord('F') or key == ord('f'):
        image_filter = features
    elif key == ord('P') or key == ord('p'):
        image_filter = preview

source.release()
cv.destroyWindow(window)