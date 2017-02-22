#!/usr/bin/env python
# -*- coding: utf-8 -*-
import commands
import time
import start_server
import hard_contral


###メイン -----------------------------------------------------------------------
def main_contral():
    #セッティングの受け取り
    set_data = get_setting_data()
    #センサーデータの受け取り
    senser_data = commands.getoutput("sudo node senser.js")

    #セッティングデータとセンサデータを比較し、センサーデータの方が小さかったら水をやる
    if set_data > senser_data:
        hard_contral.pump()


if __name__ == '__main__':
    while True:
        main_contral()
        time.sleep(300)
