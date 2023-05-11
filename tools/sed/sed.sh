#!/bin/bash
RTSPURL="rtsp://admin:GrandCam1913!@10.0.0.38:554"
CLOUD_BLOB_CONN_STRING="ABC"
echo $ESCAPEDRTSPURL
sed -e "s|\"RTSP_URL\"|\"$RTSPURL\"|g" \
    ./configMap.template.yaml \
    > ./configMap.1.yaml
sed -e "s|CLOUDBLOBCONNSTRING|\"$CLOUD_BLOB_CONN_STRING\"|g" \
    ./configMap.1.yaml \
    > ./configMap.yaml    
cat ./configMap.yaml