# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1027, 585)
        MainWindow.setMinimumSize(QtCore.QSize(991, 580))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(16777215, 120))
        self.label.setBaseSize(QtCore.QSize(1, 200))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(169, 207, 255);\n"
"font: 28pt \"Century Gothic\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame_3)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 70, 471, 271))
        self.calendarWidget.setStyleSheet("font: 12pt;")
        self.calendarWidget.setObjectName("calendarWidget")
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.listWidget = QtWidgets.QListWidget(self.frame_4)
        self.listWidget.setGeometry(QtCore.QRect(50, 70, 401, 271))
        self.listWidget.setStyleSheet("font: 14pt \"Century Gothic\";\n"
"")
        self.listWidget.setObjectName("listWidget")
        self.save_changes_button = QtWidgets.QPushButton(self.frame_4)
        self.save_changes_button.setGeometry(QtCore.QRect(50, 360, 401, 41))
        self.save_changes_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(169, 207, 255);\n"
"    font: 15pt \"Century Gothic\";\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    box-shadow: 0 20px #999;\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(119, 148, 184);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: rgb(100, 120, 150);\n"
"}\n"
"")
        self.save_changes_button.setObjectName("save_changes_button")
        self.add_new_button = QtWidgets.QPushButton(self.frame_4)
        self.add_new_button.setGeometry(QtCore.QRect(320, 30, 131, 31))
        self.add_new_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(169, 207, 255);\n"
"    font: 15pt \"Century Gothic\";\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    box-shadow: 0 20px #999;\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(119, 148, 184);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: rgb(100, 120, 150);\n"
"}")
        self.add_new_button.setObjectName("add_new_button")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit.setGeometry(QtCore.QRect(50, 30, 261, 31))
        self.lineEdit.setStyleSheet("font: 75 14pt \"Century Gothic\";\n"
"border-radius: 10px;")
        self.lineEdit.setObjectName("lineEdit")
        self.listWidget.raise_()
        self.add_new_button.raise_()
        self.save_changes_button.raise_()
        self.lineEdit.raise_()
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1027, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menuHelp.addAction(self.action)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Планировщик задач"))
        self.save_changes_button.setText(_translate("MainWindow", "Сохранить изменения"))
        self.add_new_button.setText(_translate("MainWindow", "Добавить"))
        self.menuHelp.setTitle(_translate("MainWindow", "About"))
        self.action.setText(_translate("MainWindow", "О программе"))
        self.action_2.setText(_translate("MainWindow", "Настройки"))
