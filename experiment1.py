#!/usr/bin/python
from time import gmtime, strftime
from colour import Color

print "zentrale Farbgebeeinheit"

time = 0.0
baseSaturation = 1.0
baseLuminance = 0.4
modifier = 0.05

# zentraler zeitgeber, sollte immer <3600 und >0 sein und integer raustun

time = int(strftime("%M", gmtime())) * 60 + int(strftime("%S", gmtime()))
time = float(time)

baseHue = time / 360
baseColor = Color(hsl=(baseHue, baseSaturation, baseLuminance))

baseColorVar1 = Color(hsl=(baseColor.hue + modifier / 2, baseSaturation, baseLuminance))
baseColorVar2 = Color(hsl=(baseColor.hue - modifier / 2, baseSaturation, baseLuminance))
baseColorVar3 = Color(hsl=(baseColor.hue, baseSaturation, baseLuminance + modifier))
baseColorVar4 = Color(hsl=(baseColor.hue, baseSaturation, baseLuminance - modifier))

if (baseHue * 360) < 180:
   ContrastHue = (baseHue * 360 + 180)
elif (baseHue * 360) > 180:
   ContrastHue = (baseHue * 360 - 180)
ContrastHue = ContrastHue / 360

ContrastColor = Color(hsl=(ContrastHue, baseSaturation, (baseLuminance + 0.2)))

# Terminaloutput

print time 
print "baseColor ", baseColor.hex
print "baseColorVariant1 ", baseColorVar1
print "baseColorVariant2 ", baseColorVar2
print "baseColorVariant3 ", baseColorVar3
print "baseColorVariant4 ", baseColorVar4
print "ContrastColor ", ContrastColor.hex
print "###################################"


