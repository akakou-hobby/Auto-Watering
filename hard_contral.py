#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as gpio
import time

### 水やり
def pump(PUMP,time_len):
    gpio.setup(PUMP, gpio.OUT)
    gpio.output(PUMP, 1)
    time.sleep(time_len)
    gpio.output(PUMP, 0)
    gpio.cleanup()
