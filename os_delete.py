#!/usr/bin/python
# -*- coding: utf-8 -*-
#
import object_storage
import os
import sys

###
# ユーザーID、パスワード、データセンター（ラベル）
uid = 'SL123456-1:SL123456'
upw = '71a8c0f9cd9*****************************************************'
odc = 'tok02'

# コンテナとオブジェクト名
cnt = ''
obj = ''

###
#
# メイン
#
if __name__ == '__main__':
    argvs = sys.argv  # コマンドライン引数のリスト
    argc = len(argvs) # 個数

    if (argc != 3):   
        print 'Usage: os_delete.py container object_name' 
        quit() 

    cnt = argvs[1]
    obj = argvs[2]


    oos = object_storage.get_client(uid, upw, datacenter=odc)

    res = {}
    res = oos[cnt][obj].search(obj)
    for rec in res['results']:
        print "Delete %s" % rec
        rec.delete()
    oos[cnt][obj].delete()
