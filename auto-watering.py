#!/usr/bin/env python
# -*- coding: utf-8 -*-
import commands
import time
import start_server
import hard_contral
import os
import sys
import signal

###強制終了 ---------------------------------------------------------------------
def exit_handler(signal, frame):
	print("\nExit")
	sys.exit(0)


###セッティングデータの読み込み -----------------------------------------------------
def get_setting_data():
    ###ファイルの読み込み
    def load_file():
        #ファイルの読み込み
        file_ = open('CoH.txt')
        file_data = file_.read()  # ファイル終端まで全て読んだデータを返す
        file_.close()

        return file_data

    ###データの数値部分を取り出す
    def set_int(string_num):
        #テキストのデータを切り取って、整数型へ変換
        result = string_num[7:]
        result = int(result)
        return result

    set_data = load_file()
    set_data = set_int(set_data)
    return set_data


###メイン -----------------------------------------------------------------------
def main_contral():
    #セッティングの受け取り
    set_data = get_setting_data()
    #センサーデータの受け取り
    senser_data = commands.getoutput("sudo node index.js")
    senser_data = int(senser_data)

    #セッティングデータとセンサデータを比較し、センサーデータの方が小さかったら水をやる
    if set_data > senser_data:
        hard_contral.pump(4,5)

    ###print
    print "setting data :" , set_data
    print "senser_data :" , senser_data
    print set_data > senser_data


if __name__ == '__main__':
    start_server.open_server()
    signal.signal(signal.SIGINT, exit_handler)

    while True:
        main_contral()
	for num in range(15):
            time.sleep(1)
	    print "time :" , num

