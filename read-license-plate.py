import cv2
import imutils
import time
img = cv2.imread('sample1.png')
if img is None:
    print("Không thể mở ảnh sample1.png")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thres = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,31,10)

cv2.imshow('Thres',thres)
cv2.waitKey()

contours = cv2.findContours(thres, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=True)


number = 0
for c in contours:
    (x, y, w, h) = cv2.boundingRect(c)
    print(x, y, w, h)
    if (40<w<90) and(100<h<180) and (h/w>1.5):
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        number +=1
        crop = img[y:y+h,x:x+w]
        filename = f"plate_number_{int(time.time())}_{number}.png"
        cv2.imwrite(filename, crop)

print("Number of Contours found = " + str(number))



cv2.imshow('Pix',img)
cv2.imshow('Thres',thres)
cv2.waitKey()
cv2.destroyAllWindows()