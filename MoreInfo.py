from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class MoreInfo(object):
    def setup(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(200, 150)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 180, 130))
        self.textBrowser.setObjectName("textBrowser")
        text = """
            third project
        
        corona virus (covid-19) updates
        """
        self.textBrowser.setText(text)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)    
    Dialog = QtWidgets.QDialog()
    ui = MoreInfo()
    ui.setup(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
