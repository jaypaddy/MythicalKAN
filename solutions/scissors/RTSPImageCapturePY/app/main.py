# Capture a RTSP stream using OpenCV
# and save it to a file
# Usage: python rtspcapture.py <rtsp url> <output file>
# Example: python rtspcapture.py rtsp://

# import the necessary packages
import os
import numpy
from imutils.video import VideoStream
import argparse
import datetime
import time
import cv2
from PIL import Image
from urllib.request import urlopen
import requests
import json
from bloboperator import BlobOperator
import sys
from metrics import GaugeMetric, CounterMetric, start_metrics_server
from env import scope_keys, scope_values, app_name, prometheus_port, sleep_time, file_prefix
from env import camera_url, blob_connstring, blobcontainername, inference_url
from env import cmetric, gmetric


def run_sample(camera_url, inference_url, blob_connstring, blobcontainername):
    # initialize the video stream and allow the cammera sensor to warmup
    # connect to Blob
    bloboperator = BlobOperator( blob_connstring )
    if bloboperator.connect_to_blob() == False:
        print("[ERROR] Failed to connect to Blob")
        return
    print("[ERROR] Connected to Blob")
    print("[INFO] starting video stream...")
    vs = VideoStream(src=camera_url).start()      

    while True:
        # grab an image from the video stream
        frame = vs.read()
        print("[INFO] reading video stream...")
        # save the image to disk
        imgfilename = "./img.jpg"
        cv2.imwrite(imgfilename, frame)
        print("[INFO] saving image...")
        # post the image to the server
        headers = {'Content-Type': 'application/octet-stream'}
        with open(imgfilename, 'rb') as f:
            r = requests.post(inference_url, headers=headers, data = f)
        print("[INFO] posting image...")
        prediction_output = json.loads(r.text)
        #loop through predictions
        for prediction in prediction_output["predictions"]:
            print('[INFO] ' + prediction["tagName"] + ': ' + str(prediction["probability"]))
        tgtfilename=file_prefix + "_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"
        bloboperator.upload_file(srcfilename=imgfilename, 
                                 tgtfilename=tgtfilename, 
                                 blobcontainername=blobcontainername)
        prediction_output["blobfilename"] = tgtfilename
        print('[INFO] ' + "Prediction message sent for file: " + tgtfilename)
        cmetric.inc(1, scope_values)
        gmetric.set(.5, scope_values)

        time.sleep(sleep_time)

def main():
    try:
        start_metrics_server(prometheus_port)
        print("camera_url: " + camera_url)
        run_sample(camera_url=camera_url,
                inference_url=inference_url,
                blob_connstring=blob_connstring,
                blobcontainername=blobcontainername)
        
    except KeyboardInterrupt:
        print ( "RTSPImageCapture stopped" ) 





if __name__ == "__main__":
    main()



