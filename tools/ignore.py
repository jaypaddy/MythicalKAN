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

# Capture a RTSP stream using OpenCV
def run_loop(camera_url, inference_url, blob_connstring, blobcontainername):
    # initialize the video stream and allow the cammera sensor to warmup
    file_prefix = os.environ.get("IOTEDGE_DEVICEID")

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
        bloboperator.upload_file(srcfilename=imgfilename, 
                                 tgtfilename=file_prefix + "_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg", 
                                 blobcontainername=blobcontainername)
        time.sleep(5)
    return


def main():
    blob_connstring = os.environ.get("EDGE_BLOB_CONN_STRING")
    blobcontainername = os.environ.get("EDGE_BLOB_CONTAINER_NAME")
    camera_url = os.environ.get("EDGE_CAMERA_URL")
    inference_url = os.environ.get("EDGE_INFERENCE_URL")
    run_loop(camera_url=camera_url,
             inference_url=inference_url,
             blob_connstring=blob_connstring,
             blobcontainername=blobcontainername
             )

if __name__ == "__main__":
    main()



