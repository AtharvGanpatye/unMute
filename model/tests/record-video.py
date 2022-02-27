from turtle import color
import os
import cv2
import sys
import time

N_FRAMES = 30
SKIP_FACTOR = N_FRAMES // 30

if len(sys.argv) != 3:
    print("ERROR : Enter Name of Sign & Number As Command Line Argument!\n> python3 record-video.py bye 30")
    sys.exit() 

sign = str(sys.argv[1])
n = int(sys.argv[2])

cap = cv2.VideoCapture(0)
cod = cv2.VideoWriter_fourcc(*'XVID')

if not os.path.isdir(sign):
    os.mkdir(sign)

# time.sleep(1)
for j in range(n):

    out = cv2.VideoWriter(f'./{sign}/{sign}-{j}.mp4', cod, 8.0, (640,480))
    for i in range(N_FRAMES):
        ret, frame = cap.read()
        if i%SKIP_FACTOR == 0:
            out.write(frame)
        
        if i == 0:
            cv2.putText(frame, 'STARTING COLLECTION', (120,200), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0, 0), 4, cv2.LINE_AA)
            time.sleep(1)
        cv2.putText(frame, 'Collecting frames for {} Video Number {}'.format(sign, j+1), (15,12), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.imshow('OpenCV Feed', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
out.release()
cv2.destroyAllWindows()
