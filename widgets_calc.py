# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(125, 125, 125);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.button_subtract = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_subtract.sizePolicy().hasHeightForWidth())
        self.button_subtract.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_subtract.setFont(font)
        self.button_subtract.setStyleSheet("QPushButton {\n"
"    background-color: rgb(88, 88, 88);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(145, 145, 145);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(160,160,160);\n"
"}")
        self.button_subtract.setObjectName("button_subtract")
        self.gridLayout.addWidget(self.button_subtract, 4, 3, 1, 1)
        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_6.sizePolicy().hasHeightForWidth())
        self.button_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_6.setFont(font)
        self.button_6.setStyleSheet("QPushButton {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton::hover {\n"
"    background-color: rgb(145, 145, 145);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(160,160,160);\n"
"}")
        self.button_6.setObjectName("button_6")
        self.gridLayout.addWidget(self.button_6, 4, 2, 1, 1)
        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_5.sizePolicy().hasHeightForWidth())
        self.button_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_5.setFont(font)
        self.button_5.setStyleSheet("QPushButton {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton::hover {\n"
"    background-color: rgb(145, 145, 145);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(160,160,160);\n"
"}")
        self.button_5.setObjectName("button_5")
        self.gridLayout.addWidget(self.button_5, 4, 1, 1, 1)
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_2.sizePolicy().hasHeightForWidth())
        self.button_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_2.setFont(font)
        self.button_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton::hover {\n"
"    background-color: rgb(145, 145, 145);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(160,160,160);\n"
"}")
        self.button_2.setObjectName("button_2")
        self.gridLayout.addWidget(self.button_2, 5, 1, 1, 1)
        self.button_add = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_add.sizePolicy().hasHeightForWidth())
        self.button_add.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_add.setFont(font)
        self.button_add.setStyleSheet("QPushButton {\n"
"    background-color: rgb(88, 88, 88);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(145, 145, 145);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(160,160,160);\n"
"}")
        self.button_add.setObjectName("button_add")
        self.gridLayout.addWidget(self.button_add, 5, 3, 1, 1)
        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_3.sizePolicy().hasHeightForWidth())
        self.button_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_3.setFont(font)
        self.button_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton::hover {\n"
"    background-color: rgb(145, 145, 145);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(160,160,160);\n"
"}")
        self.button_3.setObjectName("button_3")
        self.gridLayout.addWidget(self.button_3, 5, 2, 1, 1)
        self.button_comma = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_comma.sizePolicy().hasHeightForWidth())
        self.button_comma.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_comma.setFont(font)
        self.button_comma.setStyleSheet("QPushButton {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton::hover {\n"
"    background-color: rgb(145, 145, 145);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(160,160,160);\n"
"}")
        self.button_comma.setObjectName("button_comma")
        self.gridLayout.addWidget(self.button_comma, 6, 2, 1, 1)
        self.button_0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_0.sizePolicy().hasHeightForWidth())
        self.button_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_0.setFont(font)
        self.button_0.setStyleSheet("QPushButton {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton::hover {\n"
"    background-color: rgb(145, 145, 145);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(160,160,160);\n"
"}")
        self.button_0.setObjectName("button_0")
        self.gridLayout.addWidget(self.button_0, 6, 1, 1, 1)
        self.button_equals = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_equals.sizePolicy().hasHeightForWidth())
        self.button_equals.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_equals.setFont(font)
        self.button_equals.setStyleSheet("QPushButton {\n"
"    background-color: rgb(140, 140, 140);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton::hover {\n"
"    background-color: rgb(155,155,155);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(160,160,160);\n"
"}")
        self.button_equals.setObjectName("button_equals")
        self.gridLayout.addWidget(self.button_equals, 6, 3, 1, 1)
        self.button_divide = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_divide.sizePolicy().hasHeightForWidth())
        self.button_divide.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_divide.setFont(font)
        self.button_divide.setStyleSheet("QPushButton {\n"
"    background-color: rgb(88, 88, 88);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(145, 145, 145);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(160,160,160);\n"
"}")
        self.button_divide.setObjectName("button_divide")
        self.gridLayout.addWidget(self.button_divide, 2, 3, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("QPushButton {\n"
"    background-color: rgb(88, 88, 88);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(145, 145, 145);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(160,160,160);\n"
"}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 2, 2, 1, 1)
        self.button_square = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_square.sizePolicy().hasHeightForWidth())
        self.button_square.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_square.setFont(font)
        self.button_square.setStyleSheet("QPushButton {\n"
"    background-color: rgb(88, 88, 88);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(145, 145, 145);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(160,160,160);\n"
"}")
        self.button_square.setObjectName("button_square")
        self.gridLayout.addWidget(self.button_square, 2, 1, 1, 1)
        self.button_multiply = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_multiply.sizePolicy().hasHeightForWidth())
        self.button_multiply.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_multiply.setFont(font)
        self.button_multiply.setStyleSheet("QPushButton {\n"
"    background-color: rgb(88, 88, 88);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(145, 145, 145);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(160,160,160);\n"
"}")
        self.button_multiply.setObjectName("button_multiply")
        self.gridLayout.addWidget(self.button_multiply, 3, 3, 1, 1)
        self.button_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_8.sizePolicy().hasHeightForWidth())
        self.button_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_8.setFont(font)
        self.button_8.setStyleSheet("QPushButton {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton::hover {\n"
"    background-color: rgb(145, 145, 145);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(160,160,160);\n"
"}")
        self.button_8.setObjectName("button_8")
        self.gridLayout.addWidget(self.button_8, 3, 1, 1, 1)
        self.button_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_9.sizePolicy().hasHeightForWidth())
        self.button_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_9.setFont(font)
        self.button_9.setStyleSheet("QPushButton {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton::hover {\n"
"    background-color: rgb(145, 145, 145);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(160,160,160);\n"
"}")
        self.button_9.setObjectName("button_9")
        self.gridLayout.addWidget(self.button_9, 3, 2, 1, 1)
        self.button_delete = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_delete.sizePolicy().hasHeightForWidth())
        self.button_delete.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_delete.setFont(font)
        self.button_delete.setStyleSheet("QPushButton {\n"
"    background-color: rgb(88, 88, 88);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(145, 145, 145);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(160,160,160);\n"
"}")
        self.button_delete.setObjectName("button_delete")
        self.gridLayout.addWidget(self.button_delete, 1, 3, 1, 1)
        self.button_clearAll = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_clearAll.sizePolicy().hasHeightForWidth())
        self.button_clearAll.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_clearAll.setFont(font)
        self.button_clearAll.setStyleSheet("QPushButton {\n"
"    background-color: rgb(88, 88, 88);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(145, 145, 145);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(160,160,160);\n"
"}")
        self.button_clearAll.setObjectName("button_clearAll")
        self.gridLayout.addWidget(self.button_clearAll, 1, 2, 1, 1)
        self.button_clearEntry = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_clearEntry.sizePolicy().hasHeightForWidth())
        self.button_clearEntry.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_clearEntry.setFont(font)
        self.button_clearEntry.setStyleSheet("QPushButton {\n"
"    background-color: rgb(88, 88, 88);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(145, 145, 145);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(160,160,160);\n"
"}")
        self.button_clearEntry.setObjectName("button_clearEntry")
        self.gridLayout.addWidget(self.button_clearEntry, 1, 1, 1, 1)
        self.button_percent = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_percent.sizePolicy().hasHeightForWidth())
        self.button_percent.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_percent.setFont(font)
        self.button_percent.setStyleSheet("QPushButton {\n"
"    background-color: rgb(88, 88, 88);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(145, 145, 145);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(160,160,160);\n"
"}")
        self.button_percent.setObjectName("button_percent")
        self.gridLayout.addWidget(self.button_percent, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(88, 88, 88);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(145, 145, 145);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(160,160,160);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_7.sizePolicy().hasHeightForWidth())
        self.button_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_7.setFont(font)
        self.button_7.setStyleSheet("QPushButton {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton::hover {\n"
"    background-color: rgb(145, 145, 145);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(160,160,160);\n"
"}")
        self.button_7.setObjectName("button_7")
        self.gridLayout.addWidget(self.button_7, 3, 0, 1, 1)
        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_4.sizePolicy().hasHeightForWidth())
        self.button_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_4.setFont(font)
        self.button_4.setStyleSheet("QPushButton {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton::hover {\n"
"    background-color: rgb(145, 145, 145);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(160,160,160);\n"
"}")
        self.button_4.setObjectName("button_4")
        self.gridLayout.addWidget(self.button_4, 4, 0, 1, 1)
        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_1.sizePolicy().hasHeightForWidth())
        self.button_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_1.setFont(font)
        self.button_1.setStyleSheet("QPushButton {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton::hover {\n"
"    background-color: rgb(145, 145, 145);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(160,160,160);\n"
"}")
        self.button_1.setObjectName("button_1")
        self.gridLayout.addWidget(self.button_1, 5, 0, 1, 1)
        self.button_sign = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_sign.sizePolicy().hasHeightForWidth())
        self.button_sign.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_sign.setFont(font)
        self.button_sign.setStyleSheet("QPushButton {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton::hover {\n"
"    background-color: rgb(145, 145, 145);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(160,160,160);\n"
"}")
        self.button_sign.setObjectName("button_sign")
        self.gridLayout.addWidget(self.button_sign, 6, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QtCalc"))
        self.label_2.setText(_translate("MainWindow", "0"))
        self.button_subtract.setText(_translate("MainWindow", "-"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_add.setText(_translate("MainWindow", "+"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_comma.setText(_translate("MainWindow", ","))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_equals.setText(_translate("MainWindow", "="))
        self.button_divide.setText(_translate("MainWindow", "÷"))
        self.pushButton_13.setText(_translate("MainWindow", "√x"))
        self.button_square.setText(_translate("MainWindow", "x²"))
        self.button_multiply.setText(_translate("MainWindow", "×"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_delete.setText(_translate("MainWindow", "<-"))
        self.button_clearAll.setText(_translate("MainWindow", "C"))
        self.button_clearEntry.setText(_translate("MainWindow", "CE"))
        self.button_percent.setText(_translate("MainWindow", "%"))
        self.pushButton_2.setText(_translate("MainWindow", "1/x"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_sign.setText(_translate("MainWindow", "+/-"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
