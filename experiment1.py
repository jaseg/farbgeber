#!/usr/bin/env python3
import time
import signal
from colorsys import hls_to_rgb
import struct

import paho.mqtt.client as mqtt

#MQTT_BROKER = 'c-beam.cbrp3.c-base.org'
MQTT_BROKER = 'iot.eclipse.org' # test broker
CLIENTID    = 'farbgeber'
TOPIC       = 'farbgeber'
IVL         = 1 # tx interval in whole seconds

mc = mqtt.Client(CLIENTID)
mc.connect(MQTT_BROKER, 1883)

# For a simple introduction on color schemes, have a look at
# > http://printingcode.runemadsen.com/lecture-color/
bs, bl      = 1.0, 0.4          # base sat, lum
δh, δs, δl  = 0.03, 0.2, 0.07   # h,s,l modifieres
δlc         = 0.2               # lum modifier for contrast color
T           = 3600              # period of color cycle in seconds

def handle(_signum, _frame):
    tick = time.time()%T

    # Note that some of the values here might overflow. We allow this since colorsys handles this just fine.
    bh = tick/T         # base hue
    ch = bh+0.5         # contrast hue, diametrically opposite to base hue

    bc = (bh,    bl,     bs   )
    cc = (ch,    bl+δlc, bs-δs)
    v1 = (bh+δh, bl,     bs-δs)
    v2 = (bh-δh, bl,     bs-δs)
    v3 = (bh,    bl+δl,  bs   )
    v4 = (bh,    bl-δl,  bs   )
    kolors = [bc,cc,v1,v2,v3,v4]

    msg = [ min(int(k*256), 255) for rgb in ( hls_to_rgb(*hls) for hls in kolors ) for k in rgb ]
    mc.publish(TOPIC, bytearray(struct.pack('18B', *msg))) # bytearray hack for poor python3-compatibility of paho
    # TODO Initial accuracy is within one millisecond on my system. If this turns out to drift away over time, perhaps
    # add some offset correction by re-scheduling the itimer here.
    # Also, periodicity on loaded machines might be increased using the technique described in
    # > http://linux.subogero.com/1261/linux-real-time-periodic/
    # $ chrt -f -p 1 $PYTHON_PID
    #print(time.time(), tick, kolors)

signal.signal(signal.SIGALRM, handle)
signal.setitimer(signal.ITIMER_REAL, IVL-time.time()%IVL, IVL) # offset first call to synchronize with wall second
mc.loop_forever()

