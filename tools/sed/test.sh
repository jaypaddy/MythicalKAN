# Description: Test script for sed.exe
RTSPURL=`cat ./a.txt`
# Replace the string RTSPURL with values in the variable RTSPURL
echo $RTSPURL > rtspurl.txt
ESCAPEDRTSPURL=`sed "s|!|\\\!|g" rtspurl.txt`
# Escape
sed -e "s|RTSPURL|$ESCAPEDRTSPURL|g" ./escape.txt 



