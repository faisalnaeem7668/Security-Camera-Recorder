import cv2 as cv
from datetime import datetime
import time

from streamlit import stop

def recording(file,t=10*60):
    now = datetime.timestamp(datetime.now())
    stoptime = round(now + t)
    print('Recording Started At',now,stoptime, now-stoptime)
    cap = cv.VideoCapture(0) 
    frame_size = (int(cap.get(3)), int(cap.get(4)))
    fourcc = cv.VideoWriter_fourcc(*"XVID")
    filename=  f"{file}.avi"
    
    out = cv.VideoWriter(filename, fourcc, 20, frame_size)
    while True:
        _, frame = cap.read()       
        out.write(frame)
    
        if round(datetime.timestamp(datetime.now())) == stoptime:
            print("Recording Closed At",stoptime)
            break
        if cv.waitKey(1) == ord('q'):
            break
        

    out.release()
    cap.release()
    cv.destroyAllWindows()
    return f"{file}.avi"

