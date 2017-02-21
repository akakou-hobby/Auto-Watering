#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi

#手に入れたデータの必要な部分を切り取る
def cut_string(data):
    HTTP_GET_String = str(data)
    HTTP_GET_List = HTTP_GET_String.split("\'")
    HTTP_GET_Data = HTTP_GET_List[3]
    HTTP_GET_Data = HTTP_GET_Data[1:]
    return "data = " + HTTP_GET_Data

#テキストファイルへのデータの書き込み
def write_data(data):
    WriteText = open('CoH.txt', 'w')
    WriteText.write(data)
    WriteText.close()

#初期ページにジャンプさせる
def write_HTML():
    #HTMLのソース-----------------------------------------------------
    html_body="""
    <html><body>
    <Script>alert(\"Saved !\")</Script>
    <meta http-equiv="refresh" content="0;URL=../../">
    </body></html>"""
    #ここまで---------------------------------------------------------

    #実際の表示
    print "Content-type: text/html\n"
    print html_body



#HTTP GET
form = cgi.FieldStorage()

#各関数等
target_string = cut_string(form)
write_data(target_string)
write_HTML()
