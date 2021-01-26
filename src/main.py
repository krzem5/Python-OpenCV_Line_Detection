import cv2
import numpy as np



cap=cv2.VideoCapture(0)
while True:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    try:
        edges=cv2.Canny(gray,50,150,apertureSize=3)
        lines=cv2.HoughLines(edges,1,np.pi/180,200)
        for r,theta in lines[0]:
            a=np.cos(theta)
            b=np.sin(theta)
            x0=a*r
            y0=b*r
            x1=int(x0+1000*(-b))
            y1=int(y0+1000*(a))
            x2=int(x0-1000*(-b))
            y2=int(y0-1000*(a))
            cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    except:
        pass
    cv2.imshow('img',img)
    k=cv2.waitKey(30) & 0xff
    if k==27:break
cap.release()
cv2.destroyAllWindows()
img=cv2.imread('image.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,50,150,apertureSize=3)
lines=cv2.HoughLines(edges,1,np.pi/180,200)
for r,theta in lines[0]:
    a=np.cos(theta)
    b=np.sin(theta)
    x0=a*r
    y0=b*r
    x1=int(x0+1000*(-b))
    y1=int(y0+1000*(a))
    x2=int(x0-1000*(-b))
    y2=int(y0-1000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imwrite('linesDetected.jpg',img)
# cap=cv2.VideoCapture(0)
# _,img=cap.read()
# cap.release()
# img=cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,thresh=cv2.threshold(gray,127,255,1)
# _,contours,h=cv2.findContours(thresh,1,2)
# for cnt in contours:
#     approx=cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
#     if len(approx)==4:
#         cv2.drawContours(img,[cnt],0,(0,0,255),-1)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

