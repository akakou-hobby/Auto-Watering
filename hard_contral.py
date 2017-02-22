#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as gpio
import time

### 水やり
def pump(PIN,time_len):
    gpio.setup(PIN, gpio.OUT)
    gpio.output(PIN, 1)
    time.sleep(time_len)
    gpio.output(PIN, 0)
    gpio.cleanup()
