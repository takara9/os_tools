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

# ローカルファイル
lfn = ''
#####


#
# メイン
#
if __name__ == '__main__':
    #
    argvs = sys.argv  # 引数リストの取得
    argc = len(argvs) # 個数

    if (argc != 4):   
        print 'Usage: os_download.py Container Object_name Local_file' 
        quit() 

    oos = object_storage.get_client(uid, upw, datacenter=odc)

    cnt = argvs[1]
    obj = argvs[2]
    lfn = argvs[3]

    oos[cnt][obj].save_to_filename(lfn)




