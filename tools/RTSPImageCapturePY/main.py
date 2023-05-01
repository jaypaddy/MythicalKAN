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
import asyncio
import sys
from azure.iot.device import IoTHubModuleClient, Message

# global client
CLIENT = None
SENT_IMAGES=0

def create_client():
    client = IoTHubModuleClient.create_from_edge_environment()

    # Define function for handling received messages
    async def receive_message_handler(message):
        # NOTE: This function only handles messages sent to "input1".
        # Messages sent to other inputs, or to the default, will be discarded
        if message.input_name == "input1":
            print("the data in the message received on input1 was ")
            print(message.data)
            print("custom properties are")
            print(message.custom_properties)
            print("forwarding mesage to output1")
            await client.send_message_to_output(message, "output1")

    try:
        # Set handler on the client
        client.on_message_received = receive_message_handler
    except:
        # Cleanup if failure occurs
        client.shutdown()
        raise

    return client

def send_to_hub(strMessage):
    message = Message(bytearray(strMessage, 'utf8'))
    CLIENT.send_message_to_output(message, "scissors")
    global SENT_IMAGES
    SENT_IMAGES += 1
    print( "Total images sent: {}".format(SENT_IMAGES) )

def run_sample(camera_url, inference_url, blob_connstring, blobcontainername):
    # initialize the video stream and allow the cammera sensor to warmup
    file_prefix = os.environ.get("IOTEDGE_DEVICEID")
    sleep_time = int(os.environ.get("SLEEP_TIME",10))
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
        send_to_hub(json.dumps(prediction_output))
        print('[INFO] ' + "Prediction message sent for file: " + tgtfilename)

        time.sleep(sleep_time)

def main():
    try:
        if not sys.version >= "3.5.3":
            raise Exception( "The sample requires python 3.5.3+. Current version of Python: %s" % sys.version )
        print ( "IoT Hub Client for Python" )

        try:
            global CLIENT
            CLIENT = IoTHubModuleClient.create_from_edge_environment()
        except Exception as iothub_error:
            print ( "Unexpected error {} from IoTHub".format(iothub_error) )
            return
        print ( "IoT Hub module client initialized" )
        blob_connstring = os.environ.get("EDGE_BLOB_CONN_STRING")
        blobcontainername = os.environ.get("EDGE_BLOB_CONTAINER_NAME")
        camera_url = os.environ.get("EDGE_CAMERA_URL")
        inference_url = os.environ.get("EDGE_INFERENCE_URL")
        run_sample(camera_url=camera_url,
                inference_url=inference_url,
                blob_connstring=blob_connstring,
                blobcontainername=blobcontainername)
        
    except KeyboardInterrupt:
        print ( "IoT Edge module sample stopped" ) 





if __name__ == "__main__":
    main()



