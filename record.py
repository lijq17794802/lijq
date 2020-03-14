import os
import numpy as np
import cv2

'''
Looking for record-video.py? Check out lessons/record-video.py
'''

from utils import CFEVideoConf, image_resize

video = "http://admin:admin@192.168.1.7:8081/"  # 此处@后的ipv4 地址需要改为app提供的地址
cap = cv2.VideoCapture(video)

save_path = 'saved-media/video.avi'
frames_per_seconds = 24.0
config = CFEVideoConf(cap, filepath=save_path, res='720p')
out = cv2.VideoWriter(save_path, config.video_type, frames_per_seconds, config.dims)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()