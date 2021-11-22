import cv2
from datetime import datetime, time

 

cap = cv2.VideoCapture(0)
 
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
videoWriter = cv2.VideoWriter('video.avi', fourcc, 30.0, (640,480))


ret, frame = cap.read()
start_time = datetime.now()
diff = (datetime.now() - start_time).seconds # converting into seconds
print(diff)
while diff!=5:
    ret, frame = cap.read()
    cv2.putText(frame, str(diff), (70,70), cv2.FONT_HERSHEY_SIMPLEX , 1, (255, 0, 0), 2, cv2.LINE_AA)# adding timer text
    cv2.imshow('frame',frame)
    diff = (datetime.now() - start_time).seconds
    print("diff",diff)
    videoWriter.write(frame)
    k = cv2.waitKey(1)
    if k & 0xFF == ord("q"): # quit all
        break
        
cap.release()
cv2.destroyAllWindows()