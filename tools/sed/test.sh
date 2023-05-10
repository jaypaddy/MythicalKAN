#!/usr/bin/perl
$RTSP_URL="rtsp://admin:GrandCam1913!@10.0.0.39:554";
$templateyaml=`cat ./configMap.template.yaml`;
$templateyaml =~ s/RTSPURL/"$RTSP_URL"/g; 
open(FH, '>', "configMap.yaml") or die $!;
print FH $templateyaml;
close(FH);
