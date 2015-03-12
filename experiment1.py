#!/usr/bin/python
from time import gmtime, strftime
from colour import Color

print "zentrale Farbgebeeinheit"

time = 0.0
baseSaturation = 1.0
baseLuminance = 0.5

# zentraler zeitgeber, sollte immer <3600 und >0 sein und integer raustun

time = int(strftime("%M", gmtime())) * 60 + int(strftime("%S", gmtime()))
time = float(time)

baseHue = time / 360
baseColor = Color(hsl=(baseHue, baseSaturation, baseLuminance))
if (baseHue * 360) < 180:
   ContrastHue = (baseHue * 360 + 180)
elif (baseHue * 360) > 180:
   ContrastHue = (baseHue * 360 - 180)
ContrastHue = ContrastHue / 360
baseColorRed = int(baseColor.red * 255)
baseColorGreen = int(baseColor.green * 255)
baseColorBlue = int(baseColor.blue * 255)
ContrastColor = Color(hsl=(ContrastHue, baseSaturation, (baseLuminance + 0.1)))
print time, baseColor.hex, ContrastColor.hex

