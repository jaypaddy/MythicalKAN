#!/bin/bash
RTSPURL="rtsp://admin:GrandCam1913!@10.0.0.38:554"
echo $ESCAPEDRTSPURL
sed -e "s|\"RTSP_URL\"|\"$RTSPURL\"|g" \
    ./configMap.template.yaml \
    > ./configMap.yaml
cat ./configMap.yaml