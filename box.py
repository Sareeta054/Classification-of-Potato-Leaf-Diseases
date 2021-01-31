# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'box.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialogboxs(object):
    def setupUiboxs(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 100)
        Dialog.setStyleSheet("<html><body><a href=#>Detail</a></body><html>")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(210, 290, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 250, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        #self.label_2 = QtWidgets.QLabel(Dialog)
        #self.label_2.setGeometry(QtCore.QRect(40, 180, 91, 41))
        #self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        #Dialog.setWhatsThis(_translate("Dialog", "<html><head/><body><p><a href=\"#\"><span style=\" text-decoration: underline; color:#0000ff;\">hello</span></a></p></body></html>"))
        #self.label.setText(_translate("Dialog", "<html><head/><body><p>hello</p></body></html>"))
        #self.label_2.setText(_translate("Dialog", "<html><head/><body><p><a href=\"www.facebook.com\"><span style=\" font-size:11pt; text-decoration: underline; color:#0000ff;\">Detail...</span></a></p></body></html>"))
if __name__ == "__main__":
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    self.label.setText(_translate("Dialog", "<html><head/><body><p>hello</p></body></html>"))
    MainWindow.pushButton.clicked.connect(input.main)
    MainWindow.show()
    sys.exit(app.exec_())

