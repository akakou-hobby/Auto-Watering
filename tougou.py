#!/usr/bin/env python
# -*- coding: utf-8 -*-
import commands
import time
import start_server
import hard_contral


###メイン -----------------------------------------------------------------------
def main_contral():
    #センサーデータの受け取り
    senser_data = commands.getoutput("sudo node senser.js")
    senser_data = senser_data[10:]
    senser_data = int(senser_data)
    print "data:",senser_data

    #セッティングデータとセンサデータを比較し、センサーデータの方が小さかったら水をやる
    if 100 < senser_data:
        hard_contral.pump(4,5)


if __name__ == '__main__':
    while True:
	for num in range(15):
            time.sleep(1)
	    print num
	main_contral()
