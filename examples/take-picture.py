import cv2.cv2 as cv2
from time import sleep
from djitellopy import Tello

tello = Tello()
tello.connect()

tello.streamon()

sleep(2)

frame_read = tello.get_frame_read()

cv2.imwrite("picture.png", frame_read.frame)

