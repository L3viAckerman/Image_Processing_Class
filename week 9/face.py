import cv2 as cv 
import numpy as np 

(low_H, low_S, low_V) = (0, 54, 169)
(high_H, high_S, high_V) = (14, 255, 255)
images = []

# Read image
for i in range(3):
    image = cv.imread(str(i+1) + '.jpg')
    images.append(image)

def find_face(img, color_img):
    cnts,_ = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key=lambda x: cv.contourArea(x), reverse=True)
    if cv.contourArea(cnts[0]) / cv.contourArea(cnts[1]) >= 2:
        for i in range(1):
            x,y,w,h = cv.boundingRect(cnts[i])
            cv.rectangle(color_img,(x,y),(x+w,y+h),(0,255,0),2)
        # cv.drawContours(color_img, [cnts[0]], 0, (0,255,0), 3)
    else:
        for i in range(2):
            x,y,w,h = cv.boundingRect(cnts[i])
            cv.rectangle(color_img,(x,y),(x+w,y+h),(0,255,0),2)

    cv.imshow(window_name, color_img)
    
    return img

window_name = 'Image'

cv.namedWindow(window_name, cv.WINDOW_NORMAL)


def remove_noise(img):
    kernel = (15, 15)
    img = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
    return img




for i in range(3):
    image_hsv = cv.cvtColor(images[i], cv.COLOR_BGR2HSV)
    frame_threshold = cv.inRange(image_hsv, (low_H, low_S, low_V), (high_H, high_S, high_V))
    frame_threshold = find_face(frame_threshold, images[i])
    # frame_threshold = remove_noise(frame_threshold)
    # cv.imshow(window_name, frame_threshold)
    key = cv.waitKey(0)



