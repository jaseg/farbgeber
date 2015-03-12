#!/usr/bin/python
import time
from time import gmtime, strftime
from colour import Color

print "zentrale Farbgebeeinheit"

timevalue = 0.0
baseSaturation = 1.0
baseLuminance = 0.4
modifier = 0.05
programmcycles = 0

# zentraler zeitgeber, sollte immer <3600 und >0 sein und integer raustun

while (programmcycles < 3600):

   timevalue = int(strftime("%M", gmtime())) * 60 + int(strftime("%S", gmtime()))
   timevalue = float(timevalue)

   baseHue = timevalue / 360
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

# print timevalue 
# print "baseColor ", baseColor.hex
# print "baseColorVariant1 ", baseColorVar1
# print "baseColorVariant2 ", baseColorVar2
# print "baseColorVariant3 ", baseColorVar3
# print "baseColorVariant4 ", baseColorVar4
# print "ContrastColor ", ContrastColor.hex
# print "###################################"

# Weboutput

   htmlpreface = """<html><head><title>visuelle Ausgabeeinheit des zentralen Farbgebers</title><meta http-equiv="refresh" content="1" />
<style type="text/css">
"""
   htmlcontent = """</style></head><body><h1>visuelle Ausgabeeinheit des zentralen Farbgebers</h1>
<div class="baseColorVar1">baseColorVariant1</div>
<div class="baseColorVar2">baseColorVariant2</div>
<div class="baseColorVar3">baseColorVariant3</div>
<div class="baseColorVar4">baseColorVariant4</div>
<div class="Contrastcolor">Contrastcolor</div>"""
   zeitzeile = "<h1>Color-Seed " + str(timevalue) + " " + strftime("%H:%M:%S", gmtime()) + "Uhr</h1>"
   htmlclosing = """</body></html>"""

   css1 = "body { background-color:" + baseColor.hex + "; color:" + ContrastColor.hex + "; }"
   css2 = ".baseColorVar1 { background-color:" + baseColorVar1.hex + "; width:100%; height:40px; padding: 40px; font-size:20px; } \n\r"
   css3 = ".baseColorVar2 { background-color:" + baseColorVar2.hex + "; width:100%; height:40px; padding: 40px; font-size:20px; } \n\r"
   css4 = ".baseColorVar3 { background-color:" + baseColorVar3.hex + "; width:100%; height:40px; padding: 40px; font-size:20px; } \n\r"
   css5 = ".baseColorVar4 { background-color:" + baseColorVar4.hex + "; width:100%; height:40px; padding: 40px; font-size:20px; } \n\r"
   css6 = ".Contrastcolor { background-color:" + ContrastColor.hex + "; width:10%; height:900px; position:absolute; right:300px; top:0px; color:#ff00a1; padding: 40px; font-size:20px; } \n"
   
   f = open('output1.html','w')
   outputtxt = str(htmlpreface) + str(css1) + str(css2) + str(css3) + str(css4) + str(css5) + str(css6) + str(htmlcontent) + str(zeitzeile) + str(htmlclosing)
   f.write(outputtxt)
   f.close()

   programmcycles = programmcycles + 1
   time.sleep(1)

