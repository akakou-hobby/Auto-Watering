#!/usr/bin/python
import RPi.GPIO as gpio
import time

### 水やり
def pump(PUMP,time_len):
    gpio.setup(PUMP, GPIO.OUT)
    gpio.output(PUMP, 1)
    time.sleep(time_len)
    gpio.output(PUMP, 0)
