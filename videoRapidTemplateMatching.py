import numpy as np
import cv2

CHAMPTION = 'cho'

template = 'screens/temp_'+CHAMPTION+'.png'
cap = cv2.VideoCapture('screens/twisted_fate_TestVid.mp4')
temp = cv2.imread(template)
#mask = cv2.imread('screens/mask_tf.png')
w = temp.shape[0]
h = temp.shape[1]
f = open("log.csv", "w")
tracker = cv2.TrackerCSRT_create();

while(cap.isOpened()):
    ret, frame = cap.read()
    cropped = frame[750:, 1600:]
    #cropped = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)

    #res = cv2.matchTemplate(cropped, temp, 4, None, mask) #when Mask is used
    res = cv2.matchTemplate(cropped, temp, 4)
    minVal1, maxVal1, minLoc1, maxLoc1 = cv2.minMaxLoc(res)
    f.write(str(maxVal1) + "," + str(maxLoc1)+"\n")
    top_left1 = maxLoc1
    bottom_right1 = (top_left1[0] + w, top_left1[1] + h)
    cv2.rectangle(cropped, top_left1, bottom_right1, 255, 2)


    cv2.imshow('frame', cropped)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
