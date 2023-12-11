from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import covid19_data
from CoNam import *
from MoreInfo import *


class Ui_Dialog(object):
        
    def GetInfoButton(self):
        country = self.lineEdit.text()
        if country == '':
            pass
        elif country == "world" or country == "World":
            data = covid19_data.dataByName("Total")
            country_cases = data.cases
            country_deaths = data.deaths
            country_recovered = data.recovered
            self.textBrowser.setText("""
=======[Covid-19 Updates]=======
\nCountry Name : All the world
\nTotal Active Cases : {}
\nTotal Deaths : {}
\nTotal Recovered: {}
\n===========================
            """.format(country_cases,country_deaths,country_recovered))

        else:
            data = covid19_data.dataByName(country)
            country_cases = data.cases
            country_deaths = data.deaths
            country_recovered = data.recovered
            self.textBrowser.setText("""
=======[Covid-19 Updates]=======
\nCountry Name : {}
\nTotal Active Cases : {}
\nTotal Deaths : {}
\nTotal Recovered: {}
\n==========================
            """.format(country,country_cases,country_deaths,country_recovered))

        
    def CancelButton(self):
        msg = QMessageBox()
        msg.setWindowTitle("message")
        msg.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        msg.setDefaultButton(QMessageBox.No)
        msg.setText("Are you sure to quit")
        msg.setIcon(QMessageBox.Question)
        msg.buttonClicked.connect(self.ActionMessageBox)
        x = msg.exec_()
    
    def ActionMessageBox(self, i):
        a = i.text()
        if a == "&Yes":
            exit()
        else:
            pass

    def NameButton(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = CoNam()
        self.ui.setupU(self.window)
        self.window.show()
        
    def MoreButton(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = MoreInfo()
        self.ui.setup(self.window)
        self.window.show()        

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 380)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 100, 27))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(129, 20, 170, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(20, 100, 310, 260))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 60, 90, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.GetInfoButton)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 60, 90, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.CancelButton)
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(300, 20, 27, 27))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.NameButton)
        self.toolButton_2 = QtWidgets.QToolButton(Dialog)
        self.toolButton_2.setGeometry(QtCore.QRect(20, 60, 27, 27))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_2.clicked.connect(self.MoreButton)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Country name:"))
        self.pushButton.setText(_translate("Dialog", "Get info"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.toolButton.setText(_translate("Dialog", "..."))
        self.toolButton_2.setText(_translate("Dialog", "?"))
       
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    style = """
        QDialog{
            background: #414545;
            border: 1px solid #414545;
            border-radius: 8px;
            padding: 2px;
        }
        QTextBrowser{
            background: #5B6161;
            border: 1px solid #5B6161;
            border-radius: 8px;
            padding: 2px;
        }
        QTableWidget{
            background: #5B6161;
            border: 1px solid #5B6161;
            border-radius: 8px;
            padding: 2px;
        }
        QPushButton{
            background: #545757;
            border: 1px solid #545757;
            border-radius: 8px;
            padding: 2px;
        }
        QToolButton{
            background: #545757;
            border: 1px solid #545757;
            border-radius: 8px;
            padding: 2px;
        }
        QTextEdit{
            background: #5B6161;
            border: 1px solid #5B6161;
            border-radius: 8px;
            padding: 2px;
        }
        QLineEdit{
            background: #5B6161;
            border: 1px solid #5B6161;
            border-radius: 8px;
            padding: 2px;
        }        
    """
    app.setStyleSheet(style)    
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
