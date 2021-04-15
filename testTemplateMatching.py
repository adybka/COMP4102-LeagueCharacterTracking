import numpy as np
import cv2

#imgs = np.load("3dtest_images_2424.npy")


temp = cv2.imread("screens/temp_ww.png")
w = temp.shape[0]
h = temp.shape[1]

test1 = cv2.imread("screens/wwTest1.png")
test2 = cv2.imread("screens/wwTest2.png")
test3 = cv2.imread("screens/wwTest3.png")

methods = [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED]

cv2.imshow("template", temp)
cv2.waitKey(0)
#methods 1, 4, 5
for method in methods:

    base1 = test1.copy()
    base2 = test2.copy()
    base3 = test3.copy()

    output1 = cv2.matchTemplate(base1, temp, method)
    output2 = cv2.matchTemplate(base2, temp, method)
    output3 = cv2.matchTemplate(base3, temp, method)

    minVal1, maxVal1, minLoc1, maxLoc1 = cv2.minMaxLoc(output1)
    minVal2, maxVal2, minLoc2, maxLoc2 = cv2.minMaxLoc(output2)
    minVal3, maxVal3, minLoc3, maxLoc3 = cv2.minMaxLoc(output3)
    print("Method" + str(method))
    if method == cv2.TM_SQDIFF or method == cv2.TM_SQDIFF_NORMED:
        top_left1 = minLoc1
        top_left2 = minLoc2
        top_left3 = minLoc3
        print("Image1 " + str(minVal1))
        print("Image2 " + str(minVal2))
        print("Image3 " + str(minVal3))
    else:
        top_left1 = maxLoc1
        top_left2 = maxLoc2
        top_left3 = maxLoc3
        print("Image1 " + str(maxVal1))
        print("Image2 " + str(maxVal1))
        print("Image3 " + str(maxVal1))
    bottom_right1 = (top_left1[0] + w, top_left1[1] + h)
    bottom_right2 = (top_left2[0] + w, top_left2[1] + h)
    bottom_right3 = (top_left3[0] + w, top_left3[1] + h)
    cv2.rectangle(base1, top_left1, bottom_right1, 255, 2)
    cv2.rectangle(base2, top_left2, bottom_right2, 255, 2)
    cv2.rectangle(base3, top_left3, bottom_right3, 255, 2)

    '''
    result = np.zeros(output.shape)

    for i in range(output.shape[0]):
        for j in range(output.shape[1]):
            if output[i][j] > 200
    '''
    cv2.imshow("1-" + str(method), base1)
    cv2.imshow("2-"+str(method), base2)
    cv2.imshow("3-"+str(method), base3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
