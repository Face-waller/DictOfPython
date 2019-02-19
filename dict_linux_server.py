#!/usr/bin/env python3
from __future__ import unicode_literals
# coding=utf-8

'''
name:Levi
date:2018-10-20
email:1971546207@qq.com
modules: python3.6  pymysql
This is a dict
'''

from socket import *
import os
import signal
import pymysql
import hashlib
import time
import sys
from reptile import LookUpTheWord

import multiprocessing as mg


def do_child(c, db):
    # 循环接收请求
    while True:
        data = c.recv(1024).decode()
        print("Request", data)
        if (not data) or data[0] == "E":
            c.close()
            sys.exit(0)
        elif data[0] == "R":
            do_register(c, db, data)
        elif data[0] == "L":
            do_login(c, db, data)
        elif data[0] == "Q":
            do_query(c, db, data)
        elif data[0] == "H":
            do_history(c, db, data)

# 注册
def do_register(c,db,data):
    print("注册操作")
    l = data.split(" ")
    name = l[1]
    # 加盐操作
    passwd = "TiAmoLiuYan" + name + l[2] + "AoKyHyACdE$$1314&&520"
    # hash密码加密
    hashObj = hashlib.sha256()
    hashObj.update(passwd.encode("utf-8"))
    passwdHash = hashObj.hexdigest()
    # 查询是否有重复名字
    cursor = db.cursor()
    sql = "select * from user where name='%s'"%name
    cursor.execute(sql)
    r = cursor.fetchone()
    if r != None:
        c.send(b"EXISTS")
        print("注册失败！")
    else:
        sql = "insert into user(name,passwd) values('%s','%s')"%(name, passwdHash)
        try:
            cursor.execute(sql)
            db.commit()
            c.send(b"OK")
        except:
            c.send(b"FALL")
            db.rollback()
        else:
            print("%s注册成功"%name)
    cursor.close()

# 登陆
def do_login(c,db,data):
    print("登陆操作")
    l = data.split(" ")
    name = l[1]
    passwd = "TiAmoLiuYan" + name + l[2] + "AoKyHyACdE$$1314&&520"
    hashObj = hashlib.sha256()
    hashObj.update(passwd.encode("utf-8"))
    passwdHash = hashObj.hexdigest()
    # print(passwdHash)
    cursor = db.cursor()
    sql = "select * from user where name='%s' and passwd='%s'"%(name, passwdHash)
    cursor.execute(sql)
    r = cursor.fetchone()
    if r == None:
        c.send(b'FALL')
    else:
        c.send(b'OK')

    cursor.close()

# 查词
def do_query(c, db, data):
    print("查询操作！")
    l = data.split(" ")
    name = l[1]
    word = l[2]
    # 调用查词
    ss = LookUpTheWord()
    older = ss.do_word(word)
    if older != " ":
        c.send(b"OK")
        time.sleep(0.1)
        c.send(older.encode())

        # 查词记录存入数据库
        cursor = db.cursor()
        #获取原来的历史记录
        sql = "select history from user where name='%s'"%name
        cursor.execute(sql)
        history = cursor.fetchone()[0]
        #查询语句
        sql = "update user set history='%s' where name='%s';"%(history+','+word, name)
        try:
            cursor.execute(sql)
            db.commit()
            c.send(b"OK")
        except:
            c.send(b"FALL")
            db.rollback()
        else:
            print("%s历史记录已插入"%name)
        cursor.close()


    else:
        c.send(b"FALL")

# 查询历史记录，文件下载
def do_history(c, db, data):
    print('历史记录查询')
    l = data.split(" ")
    name = l[1]

    cursor = db.cursor()
    sql = "select history from user where name='%s'"%name
    cursor.execute(sql)
    date = cursor.fetchone()[0].encode()


    c.send(date)
    time.sleep(0.1)
    c.send(b"##")
    print("查询历史成功!")


# 主流程控制

def main():
    HOST = '0.0.0.0'
    PORT = 8000
    ADDR = (HOST, PORT)

    # 创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)

    # 忽略子进程退出
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    while True:
        # 数据库连接
        db = pymysql.connect("localhost", "root", "123456","dict")
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            s.close()
            c.close()
            db.close()
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            c.close()
            db.close()
            continue

        # 创建子进程
        pid = os.fork()
        if pid < 0:
            print("create process failed")
            c.close()
        elif pid == 0:
            s.close()
            do_child(c, db)
        else:
            c.close()


if __name__ == '__main__':
    main()




