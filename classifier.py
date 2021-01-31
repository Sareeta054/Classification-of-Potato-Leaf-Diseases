
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QMainWindow,QApplication,QWidget,QVBoxLayout, QPushButton, QFileDialog , QLabel, QTextEdit,QLineEdit
from PyQt5.QtGui import QPixmap
import sys
import cv2
from box import Ui_Dialogboxs
import inp

"""def image():
    #print("data")
    r=inp.main()
    print(r)



    class AppDWindow(QDialog):
        def __init__(self):
            super().__init__()
            self.ui = Ui_Dialogboxs()
            self.ui.setupUiboxs(self)
            print('hi')
            self.ui.label.setText(r)
            self.show()
    #_translate = QtCore.QCoreApplication.translate
    app = QApplication(sys.argv)
    w = AppDWindow()
    w.show()
    w.exec_()"""

class Ui_MainWindowclassifier(object):
    def setupUiclassifier(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(664, 633)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(200, 10, 209, 41))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(50, 94, 541, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_2.clicked.connect(self.getImage)
        
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(90, 170, 461, 361))
        self.label_2.setStyleSheet("\n"
"image: url(:/newPrefix/next/potato/Potato___healthy/h (105).JPG);\n"
"background-color: rgb(232, 232, 232);")
        self.label_2.setPixmap(QtGui.QPixmap("../healthy/healthy/h (6).JPG"))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(470, 540, 101, 31))
        self.pushButton.setObjectName("pushButton")

        


        
        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def getImage(self):
        #print("hello")
        _translate = QtCore.QCoreApplication.translate
        fname = QFileDialog.getOpenFileName(QFileDialog(), 'Open file','D:\finalproject', "Image files (*.jpg *.gif)")
        if fname[0]:

            #print(fname)
           
           #self.pytextbox.setText(fname)
           imagePath = fname[0]
           self.lineEdit.setText(imagePath)
           ms=self.lineEdit.text()
           print(imagePath)

           #self.label_2.setPixmap(QtGui.QPixmap(imagePath))
           #self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=imagePath></p></body></html>"))
           #self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"></p></body></html>"))
           img=cv2.imread(imagePath,1)
           #self.label_2.setText(_translate("MainWindow","<html><head><img src= e (6).jpg/></head></html>"))
         
           dim = (461, 361)
           resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
           cv2.imwrite("resized.jpg",resized)
           #cv2.imshow("image", resized)
           
           cv2.waitKey(0)
           self.label_2.setPixmap(QtGui.QPixmap("resized.jpg"))
           



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "CLASSIFIER"))
        self.label.setText(_translate("MainWindow", "File Name:"))
        self.pushButton_2.setText(_translate("MainWindow", "Browse"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "check"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowclassifier()
    ui.setupUiclassifier(MainWindow)
    #ui.pushButton.clicked.connect(image)
    #print(r)
    MainWindow.show()
    sys.exit(app.exec_())

    

#import test_rc
