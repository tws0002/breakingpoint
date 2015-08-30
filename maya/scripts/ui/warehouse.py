# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../_sandbox/maya/scripts/ui/qt/warehouse.ui'
#
# Created: Fri Aug 28 18:18:38 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_warehouse(object):
    def setupUi(self, warehouse):
        warehouse.setObjectName("warehouse")
        warehouse.resize(613, 591)
        warehouse.setMinimumSize(QtCore.QSize(613, 325))
        warehouse.setMaximumSize(QtCore.QSize(613, 700))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        warehouse.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/shelf/img/shelf/shelf_save35.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        warehouse.setWindowIcon(icon)
        warehouse.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(31, 31, 31);")
        self.lblImage = QtGui.QLabel(warehouse)
        self.lblImage.setGeometry(QtCore.QRect(10, 6, 416, 171))
        self.lblImage.setText("")
        self.lblImage.setPixmap(QtGui.QPixmap(":/shot/img/shot/000.png"))
        self.lblImage.setScaledContents(True)
        self.lblImage.setObjectName("lblImage")
        self.edtComment = QtGui.QPlainTextEdit(warehouse)
        self.edtComment.setGeometry(QtCore.QRect(225, 440, 381, 61))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.edtComment.setFont(font)
        self.edtComment.setFrameShape(QtGui.QFrame.Box)
        self.edtComment.setFrameShadow(QtGui.QFrame.Plain)
        self.edtComment.setLineWidth(1)
        self.edtComment.setMidLineWidth(0)
        self.edtComment.setReadOnly(True)
        self.edtComment.setPlainText("")
        self.edtComment.setBackgroundVisible(False)
        self.edtComment.setCenterOnScroll(False)
        self.edtComment.setObjectName("edtComment")
        self.edtMetaData = QtGui.QPlainTextEdit(warehouse)
        self.edtMetaData.setGeometry(QtCore.QRect(440, 41, 161, 131))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.edtMetaData.setFont(font)
        self.edtMetaData.setFrameShape(QtGui.QFrame.Box)
        self.edtMetaData.setFrameShadow(QtGui.QFrame.Plain)
        self.edtMetaData.setLineWidth(1)
        self.edtMetaData.setReadOnly(True)
        self.edtMetaData.setObjectName("edtMetaData")
        self.btnHelp = QtGui.QPushButton(warehouse)
        self.btnHelp.setGeometry(QtCore.QRect(590, 566, 16, 16))
        self.btnHelp.setStyleSheet("background-color: rgb(56, 56, 56);")
        self.btnHelp.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/btn/img/btn/helpBtn24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnHelp.setIcon(icon1)
        self.btnHelp.setIconSize(QtCore.QSize(16, 16))
        self.btnHelp.setObjectName("btnHelp")
        self.btnReport = QtGui.QPushButton(warehouse)
        self.btnReport.setGeometry(QtCore.QRect(565, 566, 16, 16))
        self.btnReport.setStyleSheet("background-color: rgb(56, 56, 56);")
        self.btnReport.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/btn/img/btn/mailBtn24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReport.setIcon(icon2)
        self.btnReport.setIconSize(QtCore.QSize(16, 16))
        self.btnReport.setObjectName("btnReport")
        self.btnEmail = QtGui.QPushButton(warehouse)
        self.btnEmail.setGeometry(QtCore.QRect(525, 566, 16, 16))
        self.btnEmail.setStyleSheet("background-color: rgb(56, 56, 56);")
        self.btnEmail.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/btn/img/btn/inboxBtn24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEmail.setIcon(icon3)
        self.btnEmail.setIconSize(QtCore.QSize(16, 16))
        self.btnEmail.setObjectName("btnEmail")
        self.line = QtGui.QFrame(warehouse)
        self.line.setGeometry(QtCore.QRect(10, 176, 596, 20))
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lblShotNr = QtGui.QLabel(warehouse)
        self.lblShotNr.setGeometry(QtCore.QRect(280, 151, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.lblShotNr.setFont(font)
        self.lblShotNr.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblShotNr.setStyleSheet("background-color: \'transparent\';")
        self.lblShotNr.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblShotNr.setObjectName("lblShotNr")
        self.lblBanner = QtGui.QLabel(warehouse)
        self.lblBanner.setGeometry(QtCore.QRect(400, 11, 24, 24))
        self.lblBanner.setStyleSheet("background-color: \'transparent\';")
        self.lblBanner.setText("")
        self.lblBanner.setPixmap(QtGui.QPixmap(":/banner/img/banner/LIGHT.png"))
        self.lblBanner.setScaledContents(True)
        self.lblBanner.setObjectName("lblBanner")
        self.lblVersion = QtGui.QLabel(warehouse)
        self.lblVersion.setGeometry(QtCore.QRect(15, 161, 46, 13))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setWeight(75)
        font.setBold(True)
        self.lblVersion.setFont(font)
        self.lblVersion.setStyleSheet("background-color: \'transparent\';")
        self.lblVersion.setObjectName("lblVersion")
        self.cbxUser = QtGui.QComboBox(warehouse)
        self.cbxUser.setGeometry(QtCore.QRect(470, 10, 131, 22))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.cbxUser.setFont(font)
        self.cbxUser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cbxUser.setStyleSheet("background-color: rgb(56, 56, 56);")
        self.cbxUser.setEditable(False)
        self.cbxUser.setInsertPolicy(QtGui.QComboBox.InsertAtBottom)
        self.cbxUser.setFrame(False)
        self.cbxUser.setObjectName("cbxUser")
        self.lblUser = QtGui.QLabel(warehouse)
        self.lblUser.setGeometry(QtCore.QRect(440, 6, 30, 30))
        self.lblUser.setStyleSheet("background-color: \'transparent\';")
        self.lblUser.setText("")
        self.lblUser.setPixmap(QtGui.QPixmap(":/user/img/user/_default.png"))
        self.lblUser.setScaledContents(True)
        self.lblUser.setObjectName("lblUser")
        self.edtPath = QtGui.QLineEdit(warehouse)
        self.edtPath.setEnabled(True)
        self.edtPath.setGeometry(QtCore.QRect(15, 565, 501, 18))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.edtPath.setFont(font)
        self.edtPath.setFrame(False)
        self.edtPath.setReadOnly(True)
        self.edtPath.setObjectName("edtPath")
        self.tabWidget = QtGui.QTabWidget(warehouse)
        self.tabWidget.setGeometry(QtCore.QRect(10, 205, 206, 351))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("color: rgb(0, 0, 0);")
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.Assets = QtGui.QWidget()
        self.Assets.setObjectName("Assets")
        self.tabWidget.addTab(self.Assets, "")
        self.Shots = QtGui.QWidget()
        self.Shots.setObjectName("Shots")
        self.tabWidget.addTab(self.Shots, "")
        self.tabWidget_2 = QtGui.QTabWidget(warehouse)
        self.tabWidget_2.setGeometry(QtCore.QRect(225, 205, 381, 226))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.tabWidget_2.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget_2.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.widget = QtGui.QWidget()
        self.widget.setObjectName("widget")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/shelf/_img/shelf/shelf_default35.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.widget, icon4, "")
        self.LIGHT = QtGui.QWidget()
        self.LIGHT.setObjectName("LIGHT")
        self.tabWidget_2.addTab(self.LIGHT, "")
        self.tableView = QtGui.QTableView(warehouse)
        self.tableView.setGeometry(QtCore.QRect(225, 510, 381, 46))
        self.tableView.setObjectName("tableView")

        self.retranslateUi(warehouse)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(warehouse)

    def retranslateUi(self, warehouse):
        warehouse.setWindowTitle(QtGui.QApplication.translate("warehouse", "Warehouse", None, QtGui.QApplication.UnicodeUTF8))
        self.edtMetaData.setPlainText(QtGui.QApplication.translate("warehouse", "Resolution:    2048 x 1152\n"
"\n"
"FPS:    25 FPS\n"
"\n"
"Frames:    1001 - ", None, QtGui.QApplication.UnicodeUTF8))
        self.lblShotNr.setText(QtGui.QApplication.translate("warehouse", "140", None, QtGui.QApplication.UnicodeUTF8))
        self.lblVersion.setText(QtGui.QApplication.translate("warehouse", "v.0.01", None, QtGui.QApplication.UnicodeUTF8))
        self.edtPath.setText(QtGui.QApplication.translate("warehouse", "P:/2_production/2_shots/140_magneto/4_LIGHT/WORK/140_LIGHT_v003_ar.ma", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Assets), QtGui.QApplication.translate("warehouse", "Assets", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Shots), QtGui.QApplication.translate("warehouse", "Shots", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.LIGHT), QtGui.QApplication.translate("warehouse", "LIGHT", None, QtGui.QApplication.UnicodeUTF8))

import maya_rc
