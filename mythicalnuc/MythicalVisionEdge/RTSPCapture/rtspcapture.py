# Capture a RTSP stream using OpenCV
# and save it to a file
# Usage: python rtspcapture.py <rtsp url> <output file>
# Example: python rtspcapture.py rtsp://

# import the necessary packages
from imutils.video import VideoStream
import cv2
from PIL import Image
from urllib.request import urlopen


# initialize the video stream and allow the cammera sensor to warmup
print("[INFO] starting video stream...")
vs = VideoStream(src="rtsp://admin:GrandCam1913!@10.0.0.35:554").start()

# grab an image from the video stream
frame = vs.read()
# save the image to disk
p = "./img.jpg"
cv2.imwrite(p, frame)




