

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(348, 191)
        self.lblPortNo = QtWidgets.QLabel(Form)
        self.lblPortNo.setGeometry(QtCore.QRect(20, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblPortNo.setFont(font)
        self.lblPortNo.setObjectName("lblPortNo")
        self.portNoField = QtWidgets.QLineEdit(Form)
        self.portNoField.setGeometry(QtCore.QRect(140, 70, 191, 31))
        self.portNoField.setStyleSheet("background-color: orange;") 
        font = QtGui.QFont()
        font.setPointSize(12)
        self.portNoField.setFont(font)
        self.portNoField.setObjectName("hostField_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 20, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lblPortNo.setText(_translate("Form", "Port Number"))
        self.lblPortNo.setStyleSheet("background-color: orange;") 
        self.label.setText(_translate("Form", "Default port is 8080"))