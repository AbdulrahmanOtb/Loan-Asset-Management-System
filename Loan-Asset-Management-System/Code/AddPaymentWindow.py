# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddPaymentWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 350)
        MainWindow.setMinimumSize(QtCore.QSize(300, 350))
        MainWindow.setMaximumSize(QtCore.QSize(300, 350))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PushButtons_AddPayment_Frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.PushButtons_AddPayment_Frame_3.setGeometry(QtCore.QRect(0, 290, 290, 50))
        self.PushButtons_AddPayment_Frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PushButtons_AddPayment_Frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PushButtons_AddPayment_Frame_3.setObjectName("PushButtons_AddPayment_Frame_3")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.PushButtons_AddPayment_Frame_3)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.Save_AddPayment_Button_3 = QtWidgets.QPushButton(self.PushButtons_AddPayment_Frame_3)
        self.Save_AddPayment_Button_3.setObjectName("Save_AddPayment_Button_3")
        self.horizontalLayout_16.addWidget(self.Save_AddPayment_Button_3)
        self.Cancel_AddPayment_Button_3 = QtWidgets.QPushButton(self.PushButtons_AddPayment_Frame_3)
        self.Cancel_AddPayment_Button_3.setObjectName("Cancel_AddPayment_Button_3")
        self.horizontalLayout_16.addWidget(self.Cancel_AddPayment_Button_3)
        self.AddPayment_Title_2 = QtWidgets.QLabel(self.centralwidget)
        self.AddPayment_Title_2.setGeometry(QtCore.QRect(30, 0, 211, 60))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.AddPayment_Title_2.setFont(font)
        self.AddPayment_Title_2.setObjectName("AddPayment_Title_2")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 60, 284, 231))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TitleOfLoanID_AddPayment_2 = QtWidgets.QLabel(self.frame)
        self.TitleOfLoanID_AddPayment_2.setObjectName("TitleOfLoanID_AddPayment_2")
        self.verticalLayout_2.addWidget(self.TitleOfLoanID_AddPayment_2)
        self.TitleOfAmount_AddPayment_2 = QtWidgets.QLabel(self.frame)
        self.TitleOfAmount_AddPayment_2.setObjectName("TitleOfAmount_AddPayment_2")
        self.verticalLayout_2.addWidget(self.TitleOfAmount_AddPayment_2)
        self.TitleOfAuditorID_AddPayment_2 = QtWidgets.QLabel(self.frame)
        self.TitleOfAuditorID_AddPayment_2.setObjectName("TitleOfAuditorID_AddPayment_2")
        self.verticalLayout_2.addWidget(self.TitleOfAuditorID_AddPayment_2)
        self.PaymentMethod_title_2 = QtWidgets.QLabel(self.frame)
        self.PaymentMethod_title_2.setObjectName("PaymentMethod_title_2")
        self.verticalLayout_2.addWidget(self.PaymentMethod_title_2)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LoanID_Input_AddPayment_2 = QtWidgets.QLineEdit(self.frame_2)
        self.LoanID_Input_AddPayment_2.setObjectName("LoanID_Input_AddPayment_2")
        self.verticalLayout.addWidget(self.LoanID_Input_AddPayment_2)
        self.PaymentAmount_Input_2 = QtWidgets.QLineEdit(self.frame_2)
        self.PaymentAmount_Input_2.setObjectName("PaymentAmount_Input_2")
        self.verticalLayout.addWidget(self.PaymentAmount_Input_2)
        self.AuditorID_Input_AddPayment_2 = QtWidgets.QLineEdit(self.frame_2)
        self.AuditorID_Input_AddPayment_2.setObjectName("AuditorID_Input_AddPayment_2")
        self.verticalLayout.addWidget(self.AuditorID_Input_AddPayment_2)
        self.PaymentMethod_Enum_2 = QtWidgets.QComboBox(self.frame_2)
        self.PaymentMethod_Enum_2.setMinimumSize(QtCore.QSize(70, 0))
        self.PaymentMethod_Enum_2.setObjectName("PaymentMethod_Enum_2")
        self.verticalLayout.addWidget(self.PaymentMethod_Enum_2)
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Save_AddPayment_Button_3.setText(_translate("MainWindow", "Add"))
        self.Cancel_AddPayment_Button_3.setText(_translate("MainWindow", "Cancel"))
        self.AddPayment_Title_2.setText(_translate("MainWindow", "Add Payment"))
        self.TitleOfLoanID_AddPayment_2.setText(_translate("MainWindow", "Loan ID:"))
        self.TitleOfAmount_AddPayment_2.setText(_translate("MainWindow", "Amount:"))
        self.TitleOfAuditorID_AddPayment_2.setText(_translate("MainWindow", "Auditor ID:"))
        self.PaymentMethod_title_2.setText(_translate("MainWindow", "Payment method:"))


class AddPaymentWindow (QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self = self.setupUi(self)

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
