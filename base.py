import numpy as np
import cv2
# 开启ip摄像头
video = "http://admin:admin@192.168.1.7:8081/"  # 此处@后的ipv4 地址需要改为app提供的地址
cap = cv2.VideoCapture(video)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()