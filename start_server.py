#!/usr/bin/env python
# -*- coding: utf-8 -*-

import CGIHTTPServer
import threading

###サーバの起動
def server():
    CGIHTTPServer.test()

###スレッドの立ち上げ
def open_server():
    # スレッドの設定
    th = threading.Thread(target=server, name="server", args=())
    th.start()
