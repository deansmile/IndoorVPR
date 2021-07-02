import cv2
import time
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cv2.namedWindow("test")
img_counter=0
while True:
    start_time = time.time()
    ret, frame = cap.read()
    cv2.imshow("test",frame)
    img_name="image/image_{}.png".format(img_counter)
    cv2.imwrite(img_name, frame)
    img_counter+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    time.sleep(0.5 - time.time() + start_time) 

cap.release()

cv2.destroyAllWindows()