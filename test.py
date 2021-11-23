import cv2
from datetime import datetime, time

def recording_cv():
    cap = cv2.VideoCapture(0) 
    fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
    videoWriter = cv2.VideoWriter('video.avi', fourcc, 30.0, (640,480))
    ret, frame = cap.read()
    start_time = datetime.now()
    while True:
        ret, frame = cap.read()
        cv2.imshow('frame',frame)
        videoWriter.write(frame)
    cap.release()
    cv2.destroyAllWindows()




# import only system from os
from os import system, name

import time
from datetime import datetime, timedelta

# defining setcount function /setting the countdown
 
global hrs
global mins
global secs
global totalsecs
print('Set the countdown timer:')
hrs = int(input('hours: '))
mins = int(input('minutes: '))
 totalsecs = 3600 * hrs + 30 * mins + secs
cap = cv2.VideoCapture(0) 
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
videoWriter = cv2.VideoWriter('video.avi', fourcc, 30.0, (640,480))


while totalsecs != 0:

    sec = timedelta(seconds=int(totalsecs))
    d = datetime(1, 1, 1) + sec
    print("%d hours %d minutes %d seconds left" % (d.hour, d.minute, d.second))
    # delay for a second
     # decrement the local seconds total
 
    # clearing the previous statement
    ret, frame = cap.read()
    videoWriter.write(frame)

    cv2.imshow('frame',frame)
    cv2.putText(frame, str(totalsecs), (70,70), cv2.FONT_HERSHEY_SIMPLEX , 1, (255, 0, 0), 2, cv2.LINE_AA)# adding timer text

    totalsecs -= 1
    k = cv2.waitKey(1)
    if k & 0xFF == ord("q"): # quit all
        break
    if totalsecs == 0:
        break
  
cap.release()
  

if totalsecs == 0:
    print('Tadaa')
 
 



 

