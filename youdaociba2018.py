# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '44.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
#问题 #???
#---version_v3 各窗口分类写

#导入资源文件路径生成模块
from resource import resource_path
#解决windows下使用多进程模块multiprocessing的程序用pyinstaller打包会出现问题的问题
from multiprocessing import freeze_support
from pygame.locals import *
#导入PyQt5模块
from PyQt5 import QtCore, QtGui, QtWidgets
#导入套接字
from socket import socket
import os,sys,threading,time
#导入多进程模块
import multiprocessing as mg
#导入游戏模块
from BrokenSword_version_V1 import BrokenSword
#导入爬虫模块
from reptile import LookUpTheWord
#导入本地检索词典模块
from LocalFindci import LLocalfindci



class Ui_MainWindow(object):
    def __init__(self):
        #判断登录和注册对话框存活和是否登录的初始变量
        self.loginn = False
        self.registerr = False
        self.successedlogi = False
    def setupUi(self, MainWindow):
        #主界面设置
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(803, 631)
        MainWindow.setWindowIcon(QtGui.QIcon(resource_path(os.path.join("images","tubiao.png"))))
        #设置窗口无法调整大小
        MainWindow.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        #设置窗口无边框 和 状态栏点击程序图标时稳定提供缩放
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowMinimizeButtonHint)


        #生成一个QWidget对象在MainWindow容器里
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        #在实例对象centralwidget里添加控件

#-------------      添加左侧 QListWidget选项        ------------- 

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 142, 141, 800))
        self.listWidget.setObjectName("listWidget")
        #设置背景颜色
        self.listWidget.setStyleSheet('QListWidget{background-color:#177BD0}')
        # 设置每个listwidgetitem的图标大小
        self.listWidget.setIconSize(QtCore.QSize(141, 140))
        #添加listwidget的item以及背景图
        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(resource_path(os.path.join("images","cidian.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.listWidget.addItem(item)

        item = QtWidgets.QListWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(resource_path(os.path.join("images","fanyi.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.listWidget.addItem(item)

        item = QtWidgets.QListWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(resource_path(os.path.join("images","shengciben.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.listWidget.addItem(item)

        item = QtWidgets.QListWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(resource_path(os.path.join("images","youxi.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon4)
        self.listWidget.addItem(item)

        #将listWidgetitem的点击事件连接到自定义槽
        self.listWidget.itemClicked.connect(self.ITEMClicked)


#---------------        添加由上方标题栏(page容器)      --------------- 


        self.page_6 = QtWidgets.QWidget(self.centralwidget)
        self.page_6.setGeometry(QtCore.QRect(141, 0, 664, 55 ))
        self.page_6.setObjectName('page_6')
        self.page_6.setStyleSheet("QWidget{background-image: url(%s)}"%resource_path(os.path.join("images","qqlan.png")))
        self.pushButton_8 = QtWidgets.QPushButton(self.page_6)
        self.pushButton_8.setGeometry(QtCore.QRect(630,21,14,16))
        self.pushButton_9 = QtWidgets.QPushButton(self.page_6)
        self.pushButton_9.setGeometry(QtCore.QRect(600,21,15,16))
        self.pushButton_24 = QtWidgets.QPushButton(self.page_6)
        self.pushButton_24.setGeometry(QtCore.QRect(570, 21, 15, 16))

        #关闭按钮
        self.pushButton_8.setStyleSheet("QPushButton{background-image:url(%s);border:none}\
        QPushButton:hover{background-image:url(%s);border:none}\
        QPushButton:pressed{background-image:url(%s);border:none}"\
        %(resource_path(os.path.join("images","iguan.png")),\
        resource_path(os.path.join("images","xuantingguan.png")),resource_path(os.path.join("images","anxiaguan.png"))))
        #实现按钮退出程序功能
        self.pushButton_8.clicked.connect(sys.exit)
        #缩小按钮
        self.pushButton_9.setStyleSheet("QPushButton{background-image:url(%s);border:none}\
        QPushButton:hover{background-image:url(%s);border:none}\
        QPushButton:pressed{background-image:url(%s);border:none}"\
        %(resource_path(os.path.join("images","isuo.png")),resource_path(os.path.join("images","anxiasuo.png")),\
        resource_path(os.path.join("images","anxiasuo.png"))))
        #实现按钮缩小程序功能
        self.pushButton_9.clicked.connect(MainWindow.showMinimized)
        #关于软件按钮
        self.pushButton_24.setStyleSheet("QPushButton{background-image:url(%s);border:none}\
        QPushButton:hover{background-image:url(%s);border:none}\
        QPushButton:pressed{background-image:url(%s);border:none}"\
        %(resource_path(os.path.join("images","iguanyu.png")),resource_path(os.path.join("images","xuantingguanyu.png")),\
        resource_path(os.path.join("images","anxiaguanyu.png"))))
        #实现按钮弹出关于软件弹框
        self.pushButton_24.clicked.connect(self.guanyuruanjian)


#----------------    添加左上侧登录界面(用户头像加登录字样)(page容器)  ----------------- 
        self.page_7 = QtWidgets.QWidget(self.centralwidget)
        self.page_7.setGeometry(QtCore.QRect(0, 0, 141, 143))
        self.page_7.setObjectName('page_7')
        self.page_7.setStyleSheet("QWidget{background-color:#177BD0}")
        #左上角程序名称logo
        self.label_6 = QtWidgets.QLabel(self.page_7)
        self.label_6.setGeometry(QtCore.QRect(6,2,64,21))
        #设置logo标签字体颜色
        self.label_6.setStyleSheet("QLabel{color:#FFFFFF}")
        #设置logo标签字体样式
        font_ = QtGui.QFont("Microsoft YaHei",10,63,False)
        self.label_6.setFont(font_)
        #list用户头像
        self.pushButton_10 = QtWidgets.QPushButton(self.page_7)
        self.pushButton_10.setGeometry(QtCore.QRect(37,30,65,66))
        self.pushButton_10.setStyleSheet("QPushButton{background-image:url(%s);border:none}\
        QPushButton:hover{background-image:url(%s);border:none}\
        QPushButton:pressed{background-image:url(%s);border:none}"\
        %(resource_path(os.path.join("images","ilistyonghu.png")),resource_path(os.path.join("images","anxialistyonghu.png")),\
        resource_path(os.path.join("images","anxialistyonghu.png"))))
        #list用户头像 按钮信号连接自定义槽函数
        self.pushButton_10.clicked.connect(self.checkstacked_0)
        #list登录字样
        self.pushButton_11 = QtWidgets.QPushButton(self.page_7)
        self.pushButton_11.setGeometry(QtCore.QRect(0,107,141,35))
        self.pushButton_11.setStyleSheet("QPushButton{background-image:url(%s);border:none}\
        QPushButton:hover{background-image:url(%s);border:none}\
        QPushButton:pressed{background-image:url(%s);border:none}"\
        %(resource_path(os.path.join("images","listdenglu.png")),resource_path(os.path.join("images","listdenglu.png")),\
        resource_path(os.path.join("images","listdenglu.png"))))
        #list登录字样 按钮信号连接自定义槽函数
        self.pushButton_11.clicked.connect(self.logindialog)


#---------------    添加右侧stackedWidget页面     ---------------
        
        #创建一个stackedWdiget对象
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(141, 56, 664, 630))
        self.stackedWidget.setObjectName("stackedWidget")

        #用户头像页(未登录页)
        self.page_15 = QtWidgets.QWidget()
        self.page_15.setObjectName("page_15")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.page_15)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.stackedWidget_2.setGeometry(QtCore.QRect(0, 37, 664, 630))

        #???
        #个人信息选项卡按钮
        self.pushButton_20 = QtWidgets.QPushButton(self.page_15)
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_20.setGeometry(QtCore.QRect(0, 0, 115, 37))
        self.pushButton_20.setStyleSheet("QPushButton{background-image: url(%s);border:none}\
        QPushButton:hover{background-image: url(%s);border:none}\
        QPushButton:pressed{background-image: url(%s);border:none}"\
        %(resource_path(os.path.join("images","igerenxinxi.png")),resource_path(os.path.join("images","xuangerenxinxi.png")),\
        resource_path(os.path.join("images","anxiagerenxinxi.png"))))
        self.pushButton_20.clicked.connect(self.checkstacked_1)
        #我的好友选项卡按钮
        self.pushButton_21 = QtWidgets.QPushButton(self.page_15)
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_21.setGeometry(QtCore.QRect(115, 0, 115, 37))
        self.pushButton_21.setStyleSheet("QPushButton{background-image: url(%s);border:none}\
        QPushButton:hover{background-image: url(%s);border:none}\
        QPushButton:pressed{background-image: url(%s);border:none}"\
        %(resource_path(os.path.join("images","iwodeshouc.png")),resource_path(os.path.join("images","xuanwodeshouc.png")),\
        resource_path(os.path.join("images","anxiawodeshouc.png"))))
        self.pushButton_21.clicked.connect(self.checkstacked_2)
        self.page_4 = QtWidgets.QWidget()
        self.page_14 = QtWidgets.QWidget()

        self.pushButton_18 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_18.setGeometry(QtCore.QRect(150, 285, 126, 36))
        self.pushButton_18.setStyleSheet("QPushButton{background-image: url(%s);border:none}\
        QPushButton:hover{background-image: url(%s);border:none}\
        QPushButton:pressed{background-image: url(%s);border:none}"\
        %(resource_path(os.path.join("images","itabzhuce.png")),resource_path(os.path.join("images","xuantingtabzhuce.png")),\
        resource_path(os.path.join("images","anxiatabzhuce.png"))))
        self.pushButton_19 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_19.setGeometry(QtCore.QRect(320, 285, 126, 36))
        self.pushButton_19.setStyleSheet("QPushButton{background-image: url(%s);border:none}\
        QPushButton:hover{background-image: url(%s);border:none}\
        QPushButton:pressed{background-image: url(%s);border:none}"\
        %(resource_path(os.path.join("images","itabdenglu.png")),resource_path(os.path.join("images","xuantingtabdenglu.png")),\
        resource_path(os.path.join("images","anxiatabdenglu.png"))))
        self.pushButton_18.clicked.connect(self.registerdialog)
        self.pushButton_19.clicked.connect(self.logindialog)
        self.label_12 = QtWidgets.QLabel(self.page_4)
        self.label_12.setObjectName("label_12")
        self.label_12.setGeometry(QtCore.QRect(257, 220, 150, 20))
        self.label_12.setText("登录账户同步生词本")
        self.label_12.setStyleSheet("QLabel{background-image:url('')}")

        self.label_11 = QtWidgets.QLabel(self.page_14)
        self.label_11.setObjectName("label_11")
        self.label_11.setGeometry(QtCore.QRect(275, 220, 115, 20))
        self.label_11.setText("暂时没有收藏哦")
        self.label_11.setStyleSheet("QLabel{background-image:url('')}")

        self.page_4.setStyleSheet("QWidget{background-image: url(%s)}"\
        %resource_path(os.path.join("images","jiemian.png")))
        self.stackedWidget_2.addWidget(self.page_4)
        self.stackedWidget_2.addWidget(self.page_14)
        self.stackedWidget.addWidget(self.page_15)

        #词典页
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        self.lineEdit.setGeometry(QtCore.QRect(120, 40, 340, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("请输入需要翻译的词")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(480, 40, 70, 41))
        self.pushButton.setObjectName("pushButton")
        self.TextEdit_4 = QtWidgets.QTextEdit(self.page)
        self.TextEdit_4.setGeometry(QtCore.QRect(120, 140, 200,300))
        self.TextEdit_4.setObjectName("TextEdit_4")
        self.TextEdit_3 = QtWidgets.QTextEdit(self.page)
        self.TextEdit_3.setGeometry(QtCore.QRect(330, 140, 200, 300))
        self.TextEdit_3.setObjectName("TextEdit_3")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(200, 110, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(400, 110, 54, 12))
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.page)
        self.pushButton.setStyleSheet("QPushButton{background-image: url(%s);border:none}\
        QPushButton:hover{background-image: url(%s);border:none}\
        QPushButton:pressed{background-image: url(%s);border:none}"\
        %(resource_path(os.path.join("images","ichaxun.png")),resource_path(os.path.join("images","xuantingchaxun.png")),\
        resource_path(os.path.join("images","anxiachaxun.png"))))
        
        #搜索按钮
        self.pushButton.clicked.connect(lambda: do_find(s, user))
        self.page.setStyleSheet("QWidget{background-image: url(%s)}"\
        %resource_path(os.path.join("images","jiemian.png")))
        self.label_3.setStyleSheet('QLabel{background:transparent}')
        self.label_4.setStyleSheet('QLabel{background:transparent}')
        self.lineEdit.setStyleSheet("QLineEdit{background-image:url()}")
        self.TextEdit_4.setStyleSheet("QTextEdit{background-image:url()}")
        self.TextEdit_3.setStyleSheet("QTextEdit{background-image:url()}")

        #翻译页
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.TEXTEdit = QtWidgets.QTextEdit(self.page_2)
        self.TEXTEdit.setGeometry(QtCore.QRect(80, 10, 441, 131))
        self.TEXTEdit.setObjectName("TEXTEdit")
        self.TEXTEdit.setPlaceholderText("输入原文")
        #翻译按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 150, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: do_tarnslate())
        self.TEXTEdit_2 = QtWidgets.QTextEdit(self.page_2)
        self.TEXTEdit_2.setGeometry(QtCore.QRect(80, 200, 441, 300))
        self.TEXTEdit_2.setObjectName("TEXTEdit_2")
        self.TEXTEdit_2.setPlaceholderText("译文")
        self.stackedWidget.addWidget(self.page_2)
        self.page_2.setStyleSheet("QWidget{background-image: url(%s)}"\
        %resource_path(os.path.join("images","jiemian.png")))
        self.TEXTEdit.setStyleSheet("QTextEdit{background-image: url()}")
        self.TEXTEdit_2.setStyleSheet("QTextEdit{background-image: url()}")

        #历史记录页
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.TEXTEdit_8 = QtWidgets.QTextEdit(self.page_3)
        self.TEXTEdit_8.setGeometry(QtCore.QRect(150, 260, 290, 161))
        self.TEXTEdit_8.setObjectName("TEXTEdit_8")
        self.TEXTEdit_8.setStyleSheet("QTextEdit{background-image: url()}")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 80, 131, 161))
        self.pushButton_4.setObjectName("pushButton_4")
        self.stackedWidget.addWidget(self.page_3)
        self.pushButton_4.setStyleSheet("QPushButton{background-image: url(%s)}"\
        %resource_path(os.path.join("images","sshengciben.png")))

        #历史查询按钮
        self.pushButton_4.clicked.connect(lambda: do_history(s, user))
        self.page_3.setStyleSheet("QWidget{background-image: url(%s)}"\
        %resource_path(os.path.join("images","jiemian.png")))

        #游戏页
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_7.setGeometry(QtCore.QRect(242, 350, 157, 155))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_5 = QtWidgets.QLabel(self.page_5)
        self.label_5.setGeometry(QtCore.QRect(82, 0,500, 303))
        self.label_5.setObjectName("label_5")
        self.checkbox = QtWidgets.QCheckBox(self.page_5)
        self.checkbox.setGeometry(QtCore.QRect(450,455,50,50))
        self.checkbox.setObjectName("checkbox")
        self.checkbox.setText('全屏')
        self.checkbox.setStyleSheet("QCheckBox{background-image: url()}")
        self.stackedWidget.addWidget(self.page_5)
        self.page_5.setStyleSheet("QWidget{background-image: url(%s)}"\
        %resource_path(os.path.join("images","jiemian.png")))
        self.movie = QtGui.QMovie('%s'\
        %resource_path(os.path.join("images","youxibeijin.gif")))
        self.label_5.setMovie(self.movie)
        self.movie.start()
        self.pushButton_7.setStyleSheet("QPushButton{background-image: url(%s); border:none}\
        QPushButton:hover{background-image: url(%s); border:none}\
        QPushButton:pressed{background-image: url(%s); border:none}"\
        %(resource_path(os.path.join("images","DirGameICO1.png")),resource_path(os.path.join("images","DirGameICO2.png")),\
        resource_path(os.path.join("images","DirGameICO2.png"))))
        #进入游戏按钮
        self.pushButton_7.clicked.connect(lambda: do_game())

        #用户头像页(登录成功页)(stackedWidget最后一页)(时间紧张，功能只是显示, 输入也不能改)
        self.page_13 = QtWidgets.QWidget()
        self.page_13.setObjectName("page_13")
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.page_13)
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.stackedWidget_3.setGeometry(QtCore.QRect(0, 37, 664, 630))

        #个人信息选项卡按钮
        self.pushButton_22 = QtWidgets.QPushButton(self.page_13)
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_22.setGeometry(QtCore.QRect(0, 0, 115, 37))
        self.pushButton_22.setStyleSheet("QPushButton{background-image: url(%s);border:none}\
        QPushButton:hover{background-image: url(%s);border:none}\
        QPushButton:pressed{background-image: url(%s);border:none}"\
        %(resource_path(os.path.join("images","igerenxinxi.png")),resource_path(os.path.join("images","xuangerenxinxi.png")),\
        resource_path(os.path.join("images","anxiagerenxinxi.png"))))
        self.pushButton_22.clicked.connect(self.checkstacked_3)
        #我的好友选项卡按钮
        self.pushButton_23 = QtWidgets.QPushButton(self.page_13)
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_23.setGeometry(QtCore.QRect(115, 0, 115, 37))
        self.pushButton_23.setStyleSheet("QPushButton{background-image: url(%s);border:none}\
        QPushButton:hover{background-image: url(%s);border:none}\
        QPushButton:pressed{background-image: url(%s);border:none}"\
        %(resource_path(os.path.join("images","iwodeshouc.png")),resource_path(os.path.join("images","xuanwodeshouc.png")),\
        resource_path(os.path.join("images","anxiawodeshouc.png"))))
        self.pushButton_23.clicked.connect(self.checkstacked_4)

        #stackedWdiget子页里的stackedWidget_3的第一页
        self.page_16 = QtWidgets.QWidget()
        #stackedWdiget子页里的stackedWidget_3的第二页
        self.page_17 = QtWidgets.QWidget()

        #第一页
        self.label_14 = QtWidgets.QLabel(self.page_16)
        self.label_14.setObjectName("label_14")
        self.label_14.setGeometry(QtCore.QRect(160, 160, 30, 30))
        self.label_14.setText("昵称")
        self.label_14.setStyleSheet("QLabel{background-image:url('')}")

        self.label_15 = QtWidgets.QLabel(self.page_16)
        self.label_15.setObjectName("label_15")
        self.label_15.setGeometry(QtCore.QRect(160, 220, 30, 30))
        self.label_15.setText("性别")
        self.label_15.setStyleSheet("QLabel{background-image:url('')}")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_16)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setPlaceholderText("请输入昵称")
        self.lineEdit_3.setMaxLength(6)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 160, 160, 30 ))
        self.lineEdit_3.setStyleSheet("QLineEdit{background-image:url('')}")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.page_16)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setPlaceholderText("请输入性别")
        self.lineEdit_4.setMaxLength(6)
        self.lineEdit_4.setGeometry(QtCore.QRect(220, 220, 160, 30))
        self.lineEdit_4.setStyleSheet("QLineEdit{background-image:url('')}")
 
        #第二页
        self.label_13 = QtWidgets.QLabel(self.page_17)
        self.label_13.setObjectName("label_13")
        self.label_13.setGeometry(QtCore.QRect(275, 220, 115, 20))
        self.label_13.setText("暂时没有收藏哦")
        self.label_13.setStyleSheet("QLabel{background-image:url('')}")

        self.page_16.setStyleSheet("QWidget{background-image: url(%s)}"\
        %resource_path(os.path.join("images","jiemian.png")))
        self.stackedWidget_3.addWidget(self.page_16)
        self.stackedWidget_3.addWidget(self.page_17)
        self.stackedWidget.addWidget(self.page_13)


#----------------------------------------------------------------

        #设置centralwidget为MainWindow的中心窗口
        MainWindow.setCentralWidget(self.centralwidget)

        #设置stackedWidget默认的页面为索引1的页面
        self.stackedWidget.setCurrentIndex(1)

#------------------     设置部分控件文本     ----------------------

        #进行翻译操作的函数,重新翻译一遍UI，是一个动态翻译的解决方案
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "有道词霸"))
        #设置自动排序为False
        self.listWidget.setSortingEnabled(False)

        #设置控件的文本
        self.label_3.setText(_translate("MainWindow", "本地释义"))
        self.label_4.setText(_translate("MainWindow", "网络释义"))
        self.label_6.setText(_translate("MainWindow", "有道词霸"))
        self.pushButton_2.setText(_translate("MainWindow", "翻译"))







#######################################     UI所有槽函数 START     #########################################


#-----------------         自定义槽函数->  一级界面stacked页号切换START        ------------------------


    #自定义槽实现列表切换stacked页面页号加1
    def ITEMClicked(self,i):
        i = self.listWidget.currentRow() + 1
        self.stackedWidget.setCurrentIndex(i)

    #自定义槽实现左侧list用户头像按钮切换stacked页面
    def checkstacked_0(self):
        #如果用户未登录切换到index(0)
        if not self.successedlogi:
            if self.registerr:
                self.regi.close()
            self.stackedWidget.setCurrentIndex(0)
        #如果用户登录成功切换到index(5)
        if self.successedlogi:
            if self.loginn:
                self.logi.close()
            self.stackedWidget.setCurrentIndex(5)

    #stackedWidget第一页(index=0)的子stackedWidget_2控件的页面切换
    def checkstacked_1(self):
        self.stackedWidget_2.setCurrentIndex(0)
    #stackedWidget第一页(index=0)的子stackedWidget_2控件的页面切换
    def checkstacked_2(self):
        self.stackedWidget_2.setCurrentIndex(1)

    #stackedWidget第5页(index=4)的子stackedWidget_3控件的页面切换
    def checkstacked_3(self):
        self.stackedWidget_3.setCurrentIndex(0)
    #stackedWidget第5页(index=4)的子stackedWidget_3控件的页面切换
    def checkstacked_4(self):
        self.stackedWidget_3.setCurrentIndex(1)


#----------------       自定义槽函数-> 实现弹出二级界面 START       ---------------------

    #登录对话框槽函数
    def logindialog(self):
        self.loginn = True
        #如果注册对话框存活就关闭它
        if self.registerr:
            self.regi.close()
            self.regisshezhiliang()
            # 创建登录对话框实例
            self.logi = emploginclass(self.regi)
            #将登录对话框切换到注册对话框的自定义信号连接到一级界面类的函数registerdialog上
            self.logi.new.xxxx.connect(self.registerdialog)
            #将登录对话框切换到敬请期待提示对话框的自定义信号连接到一级界面类的函数jingqingqidai上
            self.logi.new.zzzz.connect(self.jingqingqidai)
            #将登录对话框关闭的自定义信号连接到一级界面类的函数logishezhiliang上
            self.logi.new.uuuu.connect(self.logishezhiliang)

            #登录按钮调用后端函数
            self.logi.new.pushButton_5.clicked.connect(lambda: do_login(s))
            self.logi.show()
            self.logi.exec_()

        else:
            # 创建登录对话框实例
            self.logi = emploginclass(self.centralwidget.parentWidget())
            #将登录对话框切换到注册对话框的自定义信号连接到一级界面类的函数registerdialog上
            self.logi.new.xxxx.connect(self.registerdialog)
            #将登录对话框切换到敬请期待提示对话框的自定义信号连接到一级界面类的函数jingqingqidai上
            self.logi.new.zzzz.connect(self.jingqingqidai)
            #将登录对话框关闭的自定义信号连接到一级界面类的函数logishezhiliang上
            self.logi.new.uuuu.connect(self.logishezhiliang)
            #登录按钮调用后端函数
            self.logi.new.pushButton_5.clicked.connect(lambda: do_login(s))
            self.logi.show()
            self.logi.exec_()

    #注册对话框槽函数
    def registerdialog(self):
        self.registerr = True
        #如果登录对话框存活就关闭它
        if self.loginn:
            self.logi.close()
            self.logishezhiliang()
            #创建注册对话框实例
            self.regi = empregisterclass(self.logi)
            #将注册对话框切换到登录对话框的自定义信号连接到一级界面类的函数logindialog上
            self.regi.new.yyyy.connect(self.logindialog)
            #将注册对话框关闭的自定义信号连接到一级界面类的函数regisshenzhiliang上
            self.regi.new.iiii.connect(self.regisshezhiliang)
            
            #注册按钮调用后端函数
            self.regi.new.pushButton_14.clicked.connect(lambda: do_register(s))
            self.regi.show()
            self.regi.exec_()
        else:
            #创建注册对话框实例
            self.regi = empregisterclass(self.centralwidget.parentWidget())
            #将注册对话框切换到登录对话框的自定义信号连接到一级界面类的函数logindialog上
            self.regi.new.yyyy.connect(self.logindialog)
            #将注册对话框关闭的自定义信号连接到一级界面类的函数regisshenzhiliang上
            self.regi.new.iiii.connect(self.regisshezhiliang)

            #注册按钮调用后端函数
            self.regi.new.pushButton_14.clicked.connect(lambda: do_register(s))
            self.regi.show()
            self.regi.exec_()

    #关于软件槽函数
    def guanyuruanjian(self):
        #直接创建，不能移动，2s后关闭
        guanyusoft = notfirstui(self)
        guanyusoft.guanyusoftdialog(self.centralwidget.parentWidget())

    #敬请期待槽函数
    def jingqingqidai(self):
        #直接创建，不能移动，1s后自动关闭
        #创建敬请期待对话框实例
        jingq = notfirstui(self)
        jingq.jingqingqidaizhuti(self.logi)
    
    #登录失败槽函数
    def shibaidenglu(self):
        #直接创建，不能移动，1s后自动关闭
        shibai = notfirstui(self)
        shibai.faillogin(self.logi)
    
    #注册失败槽函数
    def shibaizhuce(self):
        #直接创建，不能移动，1s后自动关闭
        shibai2 = notfirstui(self)
        shibai2.zhuceshibai(self.regi)

    #使登录对话框存活变量为 False
    def logishezhiliang(self):
        self.loginn = False

    #使注册对话框存活变量为 False
    def regisshezhiliang(self):
        self.registerr = False


#######################################     UI所有槽函数END     #########################################







#*****************************        二级界面-类 START        ************************************


class notfirstui(QtWidgets.QDialog):
    #没有账号信号
    xxxx = QtCore.pyqtSignal()
    #已有账号信号
    yyyy = QtCore.pyqtSignal()
    #敬请期待信号
    zzzz = QtCore.pyqtSignal()
    #登录框关闭信号
    uuuu = QtCore.pyqtSignal()
    #注册框关闭信号
    iiii = QtCore.pyqtSignal()

    def __init__(self,centralwidget_parentWidget):
        super().__init__()
        #给鼠标重写函数初始化一个参数self._move_drag
        self._move_drag = False
        #传入主界面类的界面，以获得界面位置
        self.centralwidget_parentWidget = centralwidget_parentWidget

    #没有账号按钮
    def mmmm(self):
        self.xxxx.emit()
    
    #已有账号按钮
    def gggg(self):
        self.yyyy.emit()
    
    #敬请期待按钮
    def nnnn(self):
        self.zzzz.emit()

    #发送登录框关闭信号
    def bbbb(self):
        self.uuuu.emit()
    #发送注册框关闭信号
    def vvvv(self):
        self.iiii.emit()

    #登录对话框(二级界面)
    def logind(self,dialog):
        #获取centralwidget的父窗口的位置坐标(屏幕坐标)
        globalPos = self.centralwidget_parentWidget.geometry()
        #获取父窗口x坐标
        globalPosl = globalPos.left()
        #获取父窗口y坐标
        globalPost = globalPos.top()
        #获取父窗口宽
        globalWidth = globalPos.width()
        #获取父窗口高
        globalheight = globalPos.height()

        #子窗口应该移动位置
        globalx = globalPosl + globalWidth/2 - 201.5
        globaly = globalPost + globalheight/2 - 168.5
        #???
        # globalPosr = globalPos.right()
        #???
        # globalPosb = globalPos.bottom()

        #对话框大小
        dialog.resize(403,337)
        #对话框位置
        dialog.move(globalx,globaly)

        #设置窗口无法调整大小
        dialog.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        #设置窗口无边框 和 状态栏点击程序图标时稳定提供缩放
        dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowMinimizeButtonHint)
        dialog.setWindowTitle('登录')
        #设置对话框图标
        dialog.setWindowIcon(QtGui.QIcon('%s'\
        %resource_path(os.path.join("images","dengludialogtubiao.png"))))
        #设置应用程序模态
        dialog.setWindowModality(QtCore.Qt.ApplicationModal)

        #登录界面对话框的上方标题栏
        self.page_8 = QtWidgets.QWidget(dialog)
        self.page_8.setGeometry(QtCore.QRect(0, 0, 403, 49))
        self.page_8.setObjectName('page_8')
        self.page_8.setStyleSheet("QWidget{background-image:url(%s)}"\
        %resource_path(os.path.join("images","jinshanlan.png")))
        self.pushButton_12= QtWidgets.QPushButton(self.page_8)
        self.pushButton_12.setGeometry(QtCore.QRect(373,0,30,29))
        self.pushButton_12.setStyleSheet("QPushButton{background-image:url(%s);border:none}\
        QPushButton:hover{background-image:url(%s);border:none}\
        QPushButton:pressed{background-image:url(%s);border:none}"\
        %(resource_path(os.path.join("images","denglulaniguan.png")),resource_path(os.path.join("images","denglulanxuantingguan.png")),\
        resource_path(os.path.join("images","denglulananxiaguan.png"))))
        self.pushButton_12.clicked.connect(dialog.close)
        self.pushButton_12.clicked.connect(self.bbbb)

        #登录界面对话框的主体
        self.page_9 = QtWidgets.QWidget(dialog)
        self.page_9.setGeometry(QtCore.QRect(0,49,403,290))
        self.page_9.setObjectName('page_9')
        #登录按钮
        self.pushButton_5 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_5.setGeometry(QtCore.QRect(154, 160, 100, 36))
        self.pushButton_5.setObjectName("pushButton_5")
        #注册按钮
        self.pushButton_6 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_6.setGeometry(QtCore.QRect(304, 257, 99, 33))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet("QPushButton{border:none}")
        #创建一个QWidget的对象在page_9里面
        self.gridLayoutWidget = QtWidgets.QWidget(self.page_9)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 50, 251, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        #创建一个网格布局在QWidget的对象gridLayoutWidget里面
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        #密码文本输入框
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setPlaceholderText("请输入6位数字密码")
        self.lineEdit_3.setMaxLength(6)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        #密码标签
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        #用户名标签
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        #用户名文本输入框
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText("已注册长度为6的用户名")
        self.lineEdit_2.setMaxLength(6)
        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        #登录方式标签
        self.label_7 = QtWidgets.QLabel(self.page_9)
        self.label_7.setObjectName('label_7')
        self.label_7.setGeometry(80,10,62,30)

        #登录方式选项
        self.pushButton_16 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_16.setObjectName('pushButton_16')
        self.pushButton_16.setGeometry(150,10,62,30)

        self.pushButton_17 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_17.setObjectName('pushButton_17')
        self.pushButton_17.setGeometry(240,10,62,30)

        self.label_7.setText('登录方式')
        self.label_2.setText("密码")
        self.label.setText("用户名")
        self.pushButton_16.setStyleSheet("QPushButton{background-image: url(%s);border:none}\
        QPushButton:hover{background-image: url(%s);border:none}\
        QPushButton:pressed{background-image: url(%s);border:none}"\
        %(resource_path(os.path.join("images","idenglufangshiqq.png")),resource_path(os.path.join("images","anxiadenglufangshiqq.png")),\
        resource_path(os.path.join("images","anxiadenglufangshiqq.png"))))
        self.pushButton_17.setStyleSheet("QPushButton{background-image: url(%s);border:none}\
        QPushButton:hover{background-image: url(%s);border:none}\
        QPushButton:pressed{background-image: url(%s);border:none}"\
        %(resource_path(os.path.join("images","idenglufangshiweibo.png")),resource_path(os.path.join("images","anxiadenglufangshiweibo.png")),\
        resource_path(os.path.join("images","anxiadenglufangshiweibo.png"))))
        self.pushButton_5.setStyleSheet("QPushButton{background-image: url(%s);border:none}\
        QPushButton:hover{background-image: url(%s);border:none}\
        QPushButton:pressed{background-image: url(%s);border:none}"\
        %(resource_path(os.path.join("images","dialogidenglu.png")),resource_path(os.path.join("images","dialogxuantingdenglu.png")),\
        resource_path(os.path.join("images","dialoganxiadenglu.png"))))
        self.pushButton_6.setText('没有账号？')
        self.label.setStyleSheet('QLabel{background:transparent}')
        self.label_2.setStyleSheet('QLabel{background:transparent}')
        self.gridLayoutWidget.setStyleSheet("QWidget{background-image: url()}")
        
        #设置内部控件件的信号连接
        self.pushButton_16.clicked.connect(self.nnnn)
        self.pushButton_17.clicked.connect(self.nnnn)

        #访问外类的方法，改变外类的属性
        self.pushButton_6.clicked.connect(self.mmmm)


    #注册对话框(二级界面)
    def registerd(self,dialog_2):
        #获取centralwidget的父窗口的位置坐标(屏幕坐标)
        globalPos = self.centralwidget_parentWidget.geometry()
        #获取父窗口x坐标
        globalPosl = globalPos.left()
        #获取父窗口y坐标
        globalPost = globalPos.top()
        #获取父窗口宽
        globalWidth = globalPos.width()
        #获取父窗口高
        globalheight = globalPos.height()

        #子窗口应该移动位置
        globalx = globalPosl + globalWidth/2 - 212.5
        globaly = globalPost + globalheight/2 - 212.5

        #对话框大小
        dialog_2.resize(425,425)
        #对话框位置
        dialog_2.move(globalx,globaly)
        #设置窗口无法调整大小
        dialog_2.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        #设置窗口无边框 和 状态栏点击程序图标时稳定提供缩放
        dialog_2.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowMinimizeButtonHint)
        dialog_2.setWindowTitle('注册')
        #设置对话框图标
        dialog_2.setWindowIcon(QtGui.QIcon('%s'\
        %resource_path(os.path.join("images","dengludialogtubiao.png"))))
        #设置应用程序模态
        dialog_2.setWindowModality(QtCore.Qt.ApplicationModal)

        #注册界面对话框的上方标题栏
        self.page_10 = QtWidgets.QWidget(dialog_2)
        self.page_10.setGeometry(QtCore.QRect(0, 0, 425, 53))
        self.page_10.setObjectName('page_10')
        self.page_10.setStyleSheet("QWidget{background-image:url(%s)}"\
        %resource_path(os.path.join("images","zhucelan.png")))
        self.pushButton_13= QtWidgets.QPushButton(self.page_10)
        self.pushButton_13.setGeometry(QtCore.QRect(395,0,30,29))
        self.pushButton_13.setStyleSheet("QPushButton{background-image:url(%s);border:none}\
        QPushButton:hover{background-image:url(%s);border:none}\
        QPushButton:pressed{background-image:url(%s);border:none}"\
        %(resource_path(os.path.join("images","denglulaniguan.png")),resource_path(os.path.join("images","denglulanxuantingguan.png")),\
        resource_path(os.path.join("images","denglulananxiaguan.png"))))
        self.pushButton_13.clicked.connect(dialog_2.close)
        self.pushButton_13.clicked.connect(self.vvvv)

        #注册界面对话框的主体
        self.page_11 = QtWidgets.QWidget(dialog_2)
        self.page_11.setGeometry(QtCore.QRect(0,53,425,373))
        self.page_11.setObjectName('page_11')
        self.pushButton_14 = QtWidgets.QPushButton(self.page_11)
        self.pushButton_14.setGeometry(QtCore.QRect(163, 160, 126, 36))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.page_11)
        self.pushButton_15.setGeometry(QtCore.QRect(326, 340, 99, 33))
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.page_11)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(80, 50, 251, 81))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout")
        #密码输入
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_5.setObjectName("lineEdit_3")
        self.lineEdit_5.setPlaceholderText("请输入6位数字密码")
        self.lineEdit_5.setMaxLength(6)
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout_2.addWidget(self.lineEdit_5, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        #确认密码输入
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setMaxLength(6)
        self.lineEdit_4.setPlaceholderText("请再次输入密码")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout_2.addWidget(self.lineEdit_4, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 4, 0, 1, 1)
        #昵称输入
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setPlaceholderText("请输入长度为6的昵称")
        self.lineEdit_6.setMaxLength(6)
        self.gridLayout_2.addWidget(self.lineEdit_6, 0, 1, 1, 1)

        self.label_9.setText("密码")
        self.label_8.setText("确认密码")
        self.label_10.setText("昵称")
        self.pushButton_14.setStyleSheet("QPushButton{background-image: url(%s);border:none}\
        QPushButton:hover{background-image: url(%s);border:none}\
        QPushButton:pressed{background-image: url(%s);border:none}"\
        %(resource_path(os.path.join("images","dialogizhuce.png")),resource_path(os.path.join("images","dialogxuantingzhuce.png")),\
        resource_path(os.path.join("images","dialoganxiazhuce.png"))))
        self.pushButton_15.setStyleSheet("QPushButton{border:none}")
        self.pushButton_15.setText('已有账号？')
        self.label_10.setStyleSheet('QLabel{background:transparent}')
        self.label_9.setStyleSheet('QLabel{background:transparent}')
        self.label_8.setStyleSheet('QLabel{background:transparent}')
        self.gridLayoutWidget_2.setStyleSheet("QWidget{background-image:url()}")

        #设置内部控件件的信号连接
        
        self.pushButton_15.clicked.connect(self.gggg)


    #敬请期待对话框(二级界面)
    def jingqingqidaizhuti(self,fulogi):
        #创建对话框
        self.dialog_3 = QtWidgets.QDialog()
        #获取centralwidget的父窗口的位置坐标(屏幕坐标)
        globalPos = fulogi.geometry()
        #获取x坐标
        globalPosl = globalPos.left() +52.2
        #获取y坐标
        globalPost = globalPos.top() + 75
        #对话框大小
        self.dialog_3.resize(298,179)
        #对话框位置
        self.dialog_3.move(globalPosl,globalPost)
        #设置窗口无法调整大小
        self.dialog_3.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        #设置窗口无边框 和 状态栏点击程序图标时稳定提供缩放
        self.dialog_3.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowMinimizeButtonHint)
        self.dialog_3.setWindowTitle('提示')
        #设置对话框图标
        self.dialog_3.setWindowIcon(QtGui.QIcon('%s'\
        %resource_path(os.path.join("images","dengludialogtubiao.png"))))
        #设置应用程序模态
        self.dialog_3.setWindowModality(QtCore.Qt.ApplicationModal)

        #对话框主体
        self.page_12 = QtWidgets.QWidget(self.dialog_3)
        self.page_12.setObjectName("page_12")
        self.page_12.setGeometry(QtCore.QRect(0,0,298,179))
        self.page_12.setStyleSheet("QWidget{background-image: url(%s)}"\
        %resource_path(os.path.join("images","tishikuangbeijin.png")))
        #创建计时器关闭对话框
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.dialog_3.close)
        self.timer.start(1000)
        self.dialog_3.exec_()

#登录或者注册失败情况太多，统一弹出失败对话框

    #登录失败对话框(二级界面)
    def faillogin(self,fulogi):
        #创建对话框
        self.dialog_4 = QtWidgets.QDialog()
        #获取centralwidget的父窗口的位置坐标(屏幕坐标)
        globalPos = fulogi.geometry()
        #获取x坐标
        globalPosl = globalPos.left() +52.2
        #获取y坐标
        globalPost = globalPos.top() + 75
        #对话框大小
        self.dialog_4.resize(298,179)
        #对话框位置
        self.dialog_4.move(globalPosl,globalPost)
        #设置窗口无法调整大小
        self.dialog_4.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        #设置窗口无边框 和 状态栏点击程序图标时稳定提供缩放
        self.dialog_4.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowMinimizeButtonHint)
        self.dialog_4.setWindowTitle('提示')
        #设置对话框图标
        self.dialog_4.setWindowIcon(QtGui.QIcon('%s'\
        %resource_path(os.path.join("images","dengludialogtubiao.png"))))
        #设置应用程序模态
        self.dialog_4.setWindowModality(QtCore.Qt.ApplicationModal)
        
        #对话框主体
        self.page_18 = QtWidgets.QWidget(self.dialog_4)
        self.page_18.setObjectName("page_18")
        self.page_18.setGeometry(QtCore.QRect(0,0,298,179))
        self.page_18.setStyleSheet("QWidget{background-image: url(%s)}"\
        %resource_path(os.path.join("images","denglushibaidialog.png")))
        #创建计时器关闭对话框
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.dialog_4.close)
        self.timer.start(1000)
        self.dialog_4.exec_()
    
    #注册失败对话框(二级界面)
    def zhuceshibai(self,furegi):
        #创建对话框
        self.dialog_5 = QtWidgets.QDialog()
        #获取centralwidget的父窗口的位置坐标(屏幕坐标)
        globalPos = furegi.geometry()
        #获取x坐标
        globalPosl = globalPos.left() +52.2
        #获取y坐标
        globalPost = globalPos.top() + 75
        #对话框大小
        self.dialog_5.resize(298,179)
        #对话框位置
        self.dialog_5.move(globalPosl,globalPost)
        #设置窗口无法调整大小
        self.dialog_5.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        #设置窗口无边框 和 状态栏点击程序图标时稳定提供缩放
        self.dialog_5.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowMinimizeButtonHint)
        self.dialog_5.setWindowTitle('提示')
        #设置对话框图标
        self.dialog_5.setWindowIcon(QtGui.QIcon('%s'\
        %resource_path(os.path.join("images","dengludialogtubiao.png"))))
        #设置应用程序模态
        self.dialog_5.setWindowModality(QtCore.Qt.ApplicationModal)
        
        #对话框主体
        self.page_19 = QtWidgets.QWidget(self.dialog_5)
        self.page_19.setObjectName("page_19")
        self.page_19.setGeometry(QtCore.QRect(0,0,298,179))
        self.page_19.setStyleSheet("QWidget{background-image: url(%s)}"\
        %resource_path(os.path.join("images","zhuceshibaidialog.png")))
        #创建计时器关闭对话框
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.dialog_5.close)
        self.timer.start(1000)
        self.dialog_5.exec_()

    #关于软件对话框(二级界面)
    def guanyusoftdialog(self,fucenter):
        #创建对话框
        self.dialog_6 = QtWidgets.QDialog()
        #获取centralwidget的父窗口的位置坐标(屏幕坐标)
        globalPos = fucenter.geometry()
        #获取x坐标
        globalPosl = globalPos.left() + 565
        #获取y坐标
        globalPost = globalPos.top() + 56
        #对话框大小
        self.dialog_6.resize(236,359)
        #对话框位置
        self.dialog_6.move(globalPosl,globalPost)
        #设置窗口无法调整大小
        self.dialog_6.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        #设置窗口无边框 和 状态栏点击程序图标时稳定提供缩放
        self.dialog_6.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowMinimizeButtonHint)
        self.dialog_6.setWindowTitle('关于软件')
        #设置对话框图标
        self.dialog_6.setWindowIcon(QtGui.QIcon('%s'\
        %resource_path(os.path.join("images","dengludialogtubiao.png"))))
        #设置应用程序模态
        self.dialog_6.setWindowModality(QtCore.Qt.ApplicationModal)

        #对话框主体
        self.page_19 = QtWidgets.QWidget(self.dialog_6)
        self.page_19.setObjectName("page_19")
        self.page_19.setGeometry(QtCore.QRect(0,0,236,359))
        self.page_19.setStyleSheet("QWidget{background-image: url(%s)}"\
        %resource_path(os.path.join("images","linksoft.png")))
        #创建计时器关闭对话框
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.dialog_6.close)
        self.timer.start(3000)
        self.dialog_6.exec_()


#*****************************        二级界面-类 END        ************************************




#***********************************         间接创建界面-类  START       *************************************


#创建一个空白的重写鼠标事件的主窗口实例或者对话框实例，用于实现无边框的窗口移动


#创建二级界面实例(登录)
class emploginclass(QtWidgets.QDialog):
    def __init__(self,centralwidget_parentWidget):
        super(emploginclass,self).__init__()
        self.new = notfirstui(centralwidget_parentWidget)
        self.new.logind(self)
    
        #给鼠标重写函数初始化一个参数self._move_drag
        self._move_drag = False

    #重写鼠标事件
    def mousePressEvent(self, event):
        # 鼠标左键点击标题栏区域
        if (event.button() == QtCore.Qt.LeftButton) and \
        (event.y() < 337) and \
        (event.x() < 403):
            self._move_drag = True
            #窗口相对于屏幕的坐标 = 鼠标的点击相对于屏幕的点击位置-鼠标的点击相对于此实例窗口的点击位置
            self.move_DragPosition = event.globalPos() - self.pos()
            #告诉Qt这个类的事件处理函数想要处理这个事件
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        # 当鼠标左键点击不放及满足点击区域的要求后，分别实现不同的窗口调整
        if QtCore.Qt.LeftButton and self._move_drag:
            # 标题栏拖放窗口位置
            # 此实例窗口移动move()的位置 = 鼠标移动终点时窗口的屏幕位置-鼠标移动起点时窗口的屏幕位置
            self.move(QMouseEvent.globalPos() - self.move_DragPosition)
            #告诉Qt这个类的事件处理函数想要处理这个事件
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        # 鼠标释放后，扳机复位
        self._move_drag = False


#创建二级界面实例(注册)
class empregisterclass(QtWidgets.QDialog):
    def __init__(self,centralwidget_parentWidget):
        super(empregisterclass,self).__init__()
        self.new = notfirstui(centralwidget_parentWidget)
        self.new.registerd(self)

        #给鼠标重写函数初始化一个参数self._move_drag
        self._move_drag = False

    #重写鼠标事件
    def mousePressEvent(self, event):
        # 鼠标左键点击标题栏区域
        if (event.button() == QtCore.Qt.LeftButton) and \
        (event.y() < 425) and \
        (event.x() < 425):
            self._move_drag = True
            #窗口相对于屏幕的坐标 = 鼠标的点击相对于屏幕的点击位置-鼠标的点击相对于此实例窗口的点击位置
            self.move_DragPosition = event.globalPos() - self.pos()
            #告诉Qt这个类的事件处理函数想要处理这个事件
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        # 当鼠标左键点击不放及满足点击区域的要求后，分别实现不同的窗口调整
        if QtCore.Qt.LeftButton and self._move_drag:
            # 标题栏拖放窗口位置
             # 此实例窗口移动move()的位置 = 鼠标移动终点时窗口的屏幕位置-鼠标移动起点时窗口的屏幕位置
            self.move(QMouseEvent.globalPos() - self.move_DragPosition)
            #告诉Qt这个类的事件处理函数想要处理这个事件
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        # 鼠标释放后，扳机复位
        self._move_drag = False


#创建一级界面实例(主界面)
class mydesignershow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mydesignershow,self).__init__()
        self.new = Ui_MainWindow()
        self.new.setupUi(self)

        #给鼠标重写函数初始化一个参数self._move_drag
        self._move_drag = False

    #重写鼠标事件
    def mousePressEvent(self, event):
        # 鼠标左键点击标题栏区域
        if (event.button() == QtCore.Qt.LeftButton) and \
        (event.y() < 631) and \
        (event.x() < 804):
            self._move_drag = True
            #窗口相对于屏幕的坐标 = 鼠标的点击相对于屏幕的点击位置-鼠标的点击相对于此实例窗口的点击位置
            self.move_DragPosition = event.globalPos() - self.pos()
            #告诉Qt这个类的事件处理函数想要处理这个事件
            event.accept()


    def mouseMoveEvent(self, QMouseEvent):
        # 当鼠标左键点击不放及满足点击区域的要求后，分别实现不同的窗口调整
        if QtCore.Qt.LeftButton and self._move_drag:
            # 标题栏拖放窗口位置
             # 此实例窗口移动move()的位置 = 鼠标移动终点时窗口的屏幕位置-鼠标移动起点时窗口的屏幕位置
            self.move(QMouseEvent.globalPos() - self.move_DragPosition)
            #告诉Qt这个类的事件处理函数想要处理这个事件
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        # 鼠标释放后，扳机复位
        self._move_drag = False

#***********************************         间接创建界面-类  END       *************************************








# ***********************       客户端逻辑 START         ************************


#--------------------------       用户客户端槽函数 START      ------------------------------

#二级界面登录按钮槽函数
def do_login(s):
    if not s:
        # print('登录失败')
        myshow.new.shibaidenglu()
    else:
        global user
        user = login(s)

#二级界面注册按钮槽函数
def do_register(s):
    if not s:
        # print('注册失败')
        myshow.new.shibaizhuce()
    else:
        register(s)


#一级词典界面按钮槽函数
def do_find(s,user):
    localresulttt,olderrr = find(s, user)
    myshow.new.TextEdit_4.setText(localresulttt)
    myshow.new.TextEdit_3.setText(olderrr)


#一级历史记录界面按钮槽函数
def do_history(s,user):
    WorldResult = history(s, user)
    myshow.new.TEXTEdit_8.setText(WorldResult)


#一级翻译界面按钮槽函数
def do_tarnslate():
    WorldResult = translate()
    myshow.new.TEXTEdit_2.setText(WorldResult)

#子进程函数
def ProcessStart1(is_full):
    try:
        m = BrokenSword(is_full)
    except:
        #如果游戏模块实例运行异常退出则此进程退出
        sys.exit()

#子线程来回收子进程进程
def threadStart1():
    global p
    while 1:
        if p.is_alive():
            p.join()
            break

#一级游戏界面按钮clicked.connect(do_game)
def do_game():
    global p
    is_full = 0
    #如果复选框为True
    if myshow.new.checkbox.isChecked():
        #参数赋值为为pygame包里的的参数，设置为全屏
        is_full = FULLSCREEN
    else:
        is_full = 0

    #创建一个进程和一个线程并调用
    p = mg.Process(target=ProcessStart1,args=(is_full,))
    p2 = threading.Thread(target=threadStart1)
    p2.start()
    p.start()

#--------------------------       用户客户端槽函数 END       ------------------------------


# --------------------------      后台具体处理函数 START   --------------------------------

#登录(连接服务器)
def login(s):
    username = myshow.new.logi.new.lineEdit_2.text()
    passw = myshow.new.logi.new.lineEdit_3.text()
    if len(passw)!=6  or (not passw.isdigit()) or len(username) != 6:
        print('登录账号密码不符合规范')
        myshow.new.shibaidenglu()
    else:
        msg = "L {} {}".format(username,passw)
        s.send(msg.encode())
        data = s.recv(128).decode()
        if data == "OK":
            print('登录成功!')
            ####
            myshow.new.successedlogi = True
            myshow.new.checkstacked_0()

            # 登录成功则隐藏登录按钮控件
            myshow.new.pushButton_11.hide()
            return username
        else:
            print('服务器返回登录失败')
            myshow.new.shibaidenglu()
            return None

# 注册(连接服务器)
def register(s):
    rname = myshow.new.regi.new.lineEdit_6.text()
    rpassw1 = myshow.new.regi.new.lineEdit_5.text()
    rpassw2 = myshow.new.regi.new.lineEdit_4.text()
    if len(rname) != 6 or len(rpassw1) != 6 or len(rpassw2) != 6 or \
    rpassw1 != rpassw2 or (not rpassw1.isdigit()) or (not rpassw2.isdigit()):
        print('注册账号密码不符合规范')
        myshow.new.shibaizhuce()
    else:
        msg = "R {} {}".format(rname,rpassw1)
        #发送请求
        s.send(msg.encode())
        #收到回复
        data = s.recv(1024).decode()
        # print(data)
        if data == "OK":
            print('注册成功!')
            myshow.new.checkstacked_0()

        else:
            print(data)
            print('服务器返回注册失败')
            myshow.new.shibaizhuce()

#查词(服务器用来记录爬虫查词记录)
def find(s, user):
    ss = LookUpTheWord()
    ci = myshow.new.lineEdit.text()
    # myshow.new.lineEdit.clear()
    if not ci:
        return '',''
    else:
        #本地字典查询
        localresult = LLocalfindci(ci)
        try:
            #本地爬虫查询
            older = ss.do_word(ci)
        except:
            older = "< 无网络连接，请检查网络! >"
        # print(older)
        #如果用户登录并且爬虫查词有结果、则发给服务器查词记录
        if user and older and s:
            #对接没有对接完美，服务端又爬取一遍
            msg = 'Q {} {}'.format(user,ci)
            s.send(msg.encode())
            data = s.recv(128).decode()
        return localresult,older


# 查询历史(连接服务器)
def history(s, user):
    #如果已登录用户查询历史
    if user and s:
        msg = 'H {}'.format(user)
        s.send(msg.encode())
        
        # 将历史记录写入本地文件
        f = open(resource_path(os.path.join("localdirsource","我的历史记录.txt")),"wb")
        while True:
            time.sleep(0.1)
            data = s.recv(100000)
            print(data.decode())
            if data == b'##':
                break
            f.write(data)
        f.close()

        f = open(resource_path(os.path.join("localdirsource","我的历史记录.txt")),"rb")
        hisText = f.read().decode()
        if hisText == '':
            return '< 用户没有记录! >'
        return hisText

    else:
        return '< 您未登录! >'


#翻译(本地通过网络获取结果)
def translate():
    ss = LookUpTheWord()
    article = myshow.new.TEXTEdit.toPlainText()
    #获取完清理文本框
    # myshow.new.TEXTEdit.clear()
    if not article:
        return ''
    else:
        try:
            older = ss.do_word(article)
            return older
        except:
            return "< 无网络连接，请检查网络! >"


# --------------------------      后台具体处理函数 END   --------------------------------



# ******************             客户端逻辑 END          ***********************************


if __name__ == '__main__':
    # windows下multiprocessing模块设置有问题，在linux平台是没这个问题的
    #解决方法,freeze_support()函数
    #需要在主模块的行之后直接调用此函数
    #生成一个Windows可执行文件以添加对 使用multiprocessing的被冻结的程序 的支持 (Add 
    #support for when a program which uses multiprocessing has been frozen to produce a Windows executable.)
    freeze_support()

    #初始化客户端用户名和套接字,全局变量
    user = None
    #创建套接字连接服务器
    s = socket()
    #设置连接阻塞超时时间
    s.settimeout(0.4)
    try:
        s.connect(('172.88.4.225',8000))
        # s.connect(('127.0.0.1',8000))
    except:
        print('无法连接服务器，请检查网络!')
        s.close()
        s = None
    #生成创建一级界面类的实例
    app = QtWidgets.QApplication(sys.argv)
    myshow = mydesignershow()
    myshow.show()
    sys.exit(app.exec_())


