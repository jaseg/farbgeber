#!/usr/bin/env python3

import sys
import struct
import time

import paho.mqtt.client as mqtt

def on_connect(mqttc, obj, flags, rc):
	# do this in the connect handler to automatically re-subscribe after connection loss
	mqttc.subscribe("farbgeber", 0)

def on_message(mqttc, obj, msg):
	# for multiple subscriptions, add topic check here
	elems = struct.unpack('18B', msg.payload)
	kolors = [ elems[i:i+3] for i in range(0,18,3) ]
	bc,cc,v1,v2,v3,v4 = kolors
	print(time.time(), 'got color: base', bc, 'cont', cc, 'others', v1, v2, v3, v4)

# If you want to use a specific client id, use
# mqttc = mqtt.Client("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.connect("iot.eclipse.org", 1883)

mqttc.loop_forever()

