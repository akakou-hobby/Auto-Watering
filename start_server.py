#!/usr/bin/python

import CGIHTTPServer

###サーバの起動
def server():
    CGIHTTPServer.test()

###スレッドの立ち上げ
def open_server():
    # スレッドの設定
    th = threading.Thread(target=open_server, name="server", args=(,))
    th.start()
    th.setDaemon(True)
