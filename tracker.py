import numpy as np
import cv2

#Champion list: karma, cho, tf, kayn, fiora
CHAMPTION = 'cho'

template = 'screens/temp_'+CHAMPTION+'.png'
cap = cv2.VideoCapture('screens/twisted_fate_TestVid.mp4')
temp = cv2.imread(template)
#mask = cv2.imread("screens/mask_'+CHAMPTION+'.png")
w = temp.shape[0]
h = temp.shape[1]
f = open("log", "w")
f.write("--------Template: " + template.split("/")[1] + "---------\n")
tracker = cv2.TrackerCSRT_create();
success = False
frameCount = 0

while(cap.isOpened()):

    ret, frame = cap.read()
    cropped = frame[750:, 1600:]

    if success:
        (trackSuccess, box) = tracker.update(cropped)
        if trackSuccess:
            (x, y, w, h) = [int(v) for v in box]
            cv2.rectangle(cropped, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if (frameCount+1) % 200 == 0:
                success=False
            else:
                success=trackSuccess
    else:
        #
        #res = cv2.matchTemplate(cropped, temp, 4, None, mask) #when Mask is used
        res = cv2.matchTemplate(cropped, temp, 4) #No Mask
        minVal1, maxVal1, minLoc1, maxLoc1 = cv2.minMaxLoc(res)
        f.write("Match Val: " + str(maxVal1) + ", Max Location: " + str(maxLoc1))
        if maxVal1 < 3500000.0:
            f.write(", MATCH FAIL On frame: " + str(frameCount) + "\n")
            success=False
        else:
            f.write(", MATCH SUCCESS On frame: " + str(frameCount) +"\n")
            top_left1 = maxLoc1
            bottom_right1 = (top_left1[0] + w, top_left1[1] + h)
            tracker.init(cropped, (top_left1[0], top_left1[1], 25, 25))
            success=True

    frameText = "Frame: " + str(frameCount)
    cropped = cv2.putText(cropped, frameText, (50,50), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255))
    cv2.imshow('frame', cropped)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    frameCount+=1

f.close()
cap.release()
cv2.destroyAllWindows()
