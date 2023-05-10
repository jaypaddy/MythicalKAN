#!/usr/bin/perl
$RTSP_URL="rtsp://admin:GrandCam1913!@10.0.0.38:554";
print "RTSP_URL:$RTSP_URL";
# Replace the string RTSP_URL with values in the variable RTSP_URL
#$ESCAPEDRTSPURL =~ s/!/\\\!/g ;
#print "ESCAPEDRTSPURL:$ESCAPEDRTSPURL";
$templateyaml=`cat ../../solutions/scissors/.deployment/manifests/kustomize/overlay/configMap.template.yaml`;
$templateyaml =~ s/RTSPURL/"$RTSP_URL"/g; 
open(FH, '>', "configMap.yaml") or die $!;
print FH $templateyaml;
close(FH);
