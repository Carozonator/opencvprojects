# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img_rgb = cv2.imread('mueble.png')
# img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# template = cv2.imread('boton.png',0)
# w, h = template.shape[::-1]

# res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
# threshold = 0.8
# loc = np.where( res >= threshold)
# for pt in zip(*loc[::-1]):
#     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (207,104,118), 1)

# cv2.imwrite('res.png',img_rgb)



import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview")
