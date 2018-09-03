#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
   A basic subscriber, it will print every messagem of "quarto/luz" topic.
'''

import paho.mqtt.client as paho

def on_message(mosq, obj, msg):
    print('Topic: {0} - QoS: {1} - Msg:{2}.'.format(msg.topic, msg.qos, msg.payload))
    mosq.publish('pong', 'ack', 0)

def on_publish(mosq, obj, mid):
    pass

if __name__ == '__main__':
    client = paho.Client()
    client.on_message = on_message
    client.on_publish = on_publish

    client.connect("127.0.0.1", 1883, 60)

    client.subscribe("quarto/luz", 0)
    client.subscribe("quarto/#", 0)

    while client.loop() == 0:
        pass
