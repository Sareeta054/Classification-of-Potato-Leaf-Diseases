import cv2
import inp
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QDialog, QApplication,QMainWindow,QMessageBox
#from wid1 import Ui_MainWindow

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from box import Ui_Dialogboxs
from classifier import Ui_MainWindowclassifier


def image():
    #print("data")
    r=inp.main()
    #msg=r
    #query1.querysent(msg)
    #print(r)



    class AppDWindow(QDialog):
        def __init__(self):
            super().__init__()
            self.ui = Ui_Dialogboxs()
            self.ui.setupUiboxs(self)
            #print('hi')
            self.ui.label.setText(r)
            self.show()
    _translate = QtCore.QCoreApplication.translate
    app = QApplication(sys.argv)
    w = AppDWindow()
    #ui = Ui_Dialog()
    #ui.label.setText(_translate("Dialog", "<html><head/><body><p>hello this is dialog</p></body></html>"))
    #ui.label.setText("this is dialogue")
    w.show()
    w.exec_()
    #sys.exit(app.exec_())

    
    #MainWindow.pushButton.clicked.connect(jpt.main)
    
    


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindowclassifier()
        self.ui.setupUiclassifier(self)
        #ms=self.ui.lineEdit.text()
        #print(ms)
        #query1.querysent(ms+"hello are you there")
        self.show()  



app = QtWidgets.QApplication(sys.argv)
MainWindow=AppWindow()
#MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindowclassifier()
ui.setupUiclassifier(MainWindow)

ui.pushButton.clicked.connect(image)
MainWindow.show()
sys.exit(app.exec_())
