#!/usr/bin/python
# -*- coding: utf-8 -*-
#
import object_storage
import os
import sys

#####
# ユーザーID、パスワード、データセンター（ラベル）
uid = 'SL123456-1:SL123456'
upw = '71a8c0f9cd9*****************************************************'
odc = 'tok02'

# コンテナとアップロード時のオブジェクト名
cnt = ''
obj = ''
#####


#
# メイン
#
if __name__ == '__main__':
    argvs = sys.argv  # コマンドライン引数のリスト
    argc = len(argvs) # 個数

    if (argc != 2):   
        print 'Usage: os_list.py Container' 
        quit() 

    cnt = argvs[1]
    #
    oos = object_storage.get_client(uid, upw, datacenter=odc)

    obj = oos[cnt].objects()
    for obn in obj:
        print obn['path']

    





