# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wid1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from classifier import Ui_MainWindowclassifier
from query import Ui_MainWindowquery
from PyQt5.QtWidgets import QDialog, QApplication,QMainWindow,QMessageBox
from box import Ui_Dialogboxs
import inp
import smtplib

class Ui_MainWindowpage(object):
    def querysent(self):
        self.window=QtWidgets.QMainWindow()
        print("hyyy")
        self.ui=Ui_MainWindowquery()
        self.ui.setupUiquery(self.window)
        #self.ui.pushButton.clicked.connect(self.classify)
        #print(r)
              
        self.window.show()
        
    def classify(self):
        print("hllll")
        r=inp.main()
        print(r)
        
        self.window=QtWidgets.QDialog()
        
        self.ui=Ui_Dialogboxs()
        
        self.ui.setupUiboxs(self.window)
        
        self.ui.label.setText(r)
        
        #self.ui.pushButton.clicked.connect(self.classify)
            #print(r)
                  
        self.window.show()
        print("hyyy")


        
        """class AppDWindow(QDialog):
            def __init__(self):
                super().__init__()
                self.ui = Ui_Dialogboxs()
                self.ui.setupUiboxs(self)
                #print('hi')
                self.ui.label.setText(r)
                self.show()
        #_translate = QtCore.QCoreApplication.translate
        #app = QApplication(sys.argv)
        w = AppDWindow()
        w.show()
        #w.exec_()"""

        
    
    def frame1(self,item):
        
        if(item.text()=="Home"):
            self.labelhome.setPixmap(QtGui.QPixmap("home.jpg"))
            
        
        elif(item.text()=="Diseases"):
            self.labelhome.setPixmap(QtGui.QPixmap("dis.png"))
            

        elif(item.text()=="How it works"):
            self.labelhome.setPixmap(QtGui.QPixmap("hiw.png"))
            

        elif(item.text()=="Contact"):
            self.labelhome.setPixmap(QtGui.QPixmap("cnt.jpg"))


        elif(item.text()=="About"):
            self.labelhome.setPixmap(QtGui.QPixmap("about.jpg"))
            #print("help")

        elif(item.text()=="Classifier"):
            
            self.window=QtWidgets.QMainWindow()
            print("hyyy")
            self.ui=Ui_MainWindowclassifier()
            self.ui.setupUiclassifier(self.window)
            self.ui.pushButton.clicked.connect(self.classify)
            #print(r)
                  
            self.window.show()
            
    
        

        
    def setupUipage(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1367, 758)
        MainWindow.setMaximumSize(QtCore.QSize(1367, 758))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 1367, 758))
        self.frame.setMaximumSize(QtCore.QSize(1367, 758))
        self.frame.setObjectName("frame")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(160, 10, 1181, 41))
        self.frame_3.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(10, 72, 41, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(960, 10, 157, 25))
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0,0);\n"
"font: 11pt \"Lucida Bright\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/57108.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.labelhome = QtWidgets.QLabel(self.frame)
        self.labelhome.setGeometry(QtCore.QRect(166, 50, 1191, 701))
        self.labelhome.setText("")
        
        self.labelhome.setObjectName("labelhome")
        self.labelhome.setPixmap(QtGui.QPixmap("home.jpg"))
        
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 10, 171, 711))
        self.frame_2.setMinimumSize(QtCore.QSize(171, 691))
        self.frame_2.setMaximumSize(QtCore.QSize(171, 711))
        self.frame_2.setStyleSheet("background-color: rgb(10, 72, 41);\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setGeometry(QtCore.QRect(10, 43, 151, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setGeometry(QtCore.QRect(20, 210, 141, 201))
        self.listWidget.setStyleSheet("")
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 161, 161))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(16)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(161, 161, 161))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(16)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(161, 161, 161))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(161, 161, 161))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(161, 161, 161))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignBottom)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(161, 161, 161))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 94, 27))
        self.label_2.setStyleSheet("border: 1px solid #cfcfcf;\n"
"")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(0, 80, 161, 91))
        self.label.setStyleSheet("image: url(:/icon/lk.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 510, 151, 131))
        self.textEdit_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 440, 99, 29))
        self.pushButton_2.setStyleSheet("QPushButton{font: 13pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(69, 135, 122);\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.querysent)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.listWidget.itemClicked.connect(self.frame1)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Help and Support"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Home"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Diseases"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "How it works"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "Classifier"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "About"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "Contact"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">LeafSnap</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#6a6a6a;\">Copyright © 2019 LeafSnap. All Rights Reserved.</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Send Query!"))

import icons_rc
if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowpage()
    ui.setupUipage(MainWindow)
    #ui.pushButton.clicked.connect(input1.main)
    MainWindow.show()
    sys.exit(app.exec_())

