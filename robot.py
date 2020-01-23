from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import time
import cv2
from motors import Motors


camera = PiCamera()
try:
  camera.resolution = (640,480)
  camera.framerate = 32
  rawCapture = PiRGBArray(camera, size=(640, 480))
  time.sleep(0.1)
  motors = Motors()
  motors.setup_motors()

  base_pwm = 13

  for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # cv2.imwrite("/tmp/raw.jpg", frame.array)
    gray = cv2.cvtColor(frame.array, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite("/tmp/gray.jpg", gray)
    ret,tresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)
    M = cv2.moments(tresh)

    if M["m00"] > 0:
        cx = int(M["m10"] / M["m00"])
        value = 640/2 - cx
        print(value)
        if value > 0:
            motors.move_right_motor(True, base_pwm + 2)
            motors.move_left_motor(True, 0)#base_pwm - 2)
            if value > 100:
                 motors.move_right_motor(True, base_pwm)
                 motors.move_left_motor(False, base_pwm)
        else:
            motors.move_right_motor(True, 0)#base_pwm - 2)
            motors.move_left_motor(True, base_pwm + 2)
            if value < -100:
                 motors.move_right_motor(False, base_pwm)
                 motors.move_left_motor(True, base_pwm)

    # cv2.imwrite("/tmp/thresholded.jpg", tresh)
    rawCapture.truncate(0)
  pass
finally:
  camera.close()
