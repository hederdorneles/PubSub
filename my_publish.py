#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Publish messages to queue.
    This script will send a message every 3s.
'''

import paho.mqtt.publish as publish
import time

host = "localhost"


if __name__ == '__main__':
    '''
    Publish a single messagem to the "quarto/luz" topic.
    For publish multiples messages use:
        publish.multiple(msgs, hostname=host)
    '''
    publish.single(topic="quarto/luz", payload="ligado", hostname=host)

    i = 1
    while True:
        if i % 2 == 0:
            msg = "ligado"
        else:
            msg = "desligado"
        i = i + 1
        publish.single(topic="quarto/luz", payload=msg, hostname=host)
        time.sleep(3)
