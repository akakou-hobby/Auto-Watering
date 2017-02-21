import commands
import time
import threading
import start_server
import hard_contral


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
        result = int(string_num)
        return result

    set_data = load_file()
    set_data = set_int(set_data)
    return set_data


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
    start_server.open_server()

    while True:
        main_contral()
        time.sleep(300)
