from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import time
import cv2

camera = PiCamera()
try:
  camera.resolution = (180,128)
  camera.framerate = 32
  rawCapture = PiRGBArray(camera, size=(180, 128))
  time.sleep(0.1)

  for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    hsv = cv2.cvtColor(frame.array, cv2.COLOR_BGR2HSV)
    median = cv2.medianBlur(hsv,5)
    thresholded = cv2.inRange(median, np.array([0,0,0]), np.array([180,128,255]))

    # show the frame
    cv2.imshow("Frame", thresholded)
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)

    if key == ord("q"):
      break
  pass
finally:
  camera.close()
