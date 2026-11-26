# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculatrice.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(317, 509)
        MainWindow.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.push_0 = QPushButton(self.centralwidget)
        self.push_0.setObjectName(u"push_0")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_0.sizePolicy().hasHeightForWidth())
        self.push_0.setSizePolicy(sizePolicy)
        self.push_0.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(172, 172, 172);\n"
"	border-radius: 30px;\n"
"}\n"
"QPushButtton:hover{\n"
"color:rgb(61,61,61);\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 30 px;\n"
"	gridline-color: rgb(239, 239, 239);\n"
"}")

        self.gridLayout.addWidget(self.push_0, 6, 0, 1, 2)

        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(13)
        sizePolicy1.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy1)
        self.label_1.setMinimumSize(QSize(21, 89))
        self.label_1.setStyleSheet(u"font: 700 28pt \"Segoe UI\";\n"
"color:rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 4, Qt.AlignmentFlag.AlignRight)

        self.push_plus = QPushButton(self.centralwidget)
        self.push_plus.setObjectName(u"push_plus")
        sizePolicy.setHeightForWidth(self.push_plus.sizePolicy().hasHeightForWidth())
        self.push_plus.setSizePolicy(sizePolicy)
        self.push_plus.setStyleSheet(u"QPushButton{\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(243, 213, 40);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:30px\n"
"}")
        icon = QIcon()
        icon.addFile(u"../assets/Screenshot_2026-11-18_172349-removebg-preview.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.push_plus.setIcon(icon)
        self.push_plus.setIconSize(QSize(0, 26))

        self.gridLayout.addWidget(self.push_plus, 2, 3, 1, 1)

        self.push_egal = QPushButton(self.centralwidget)
        self.push_egal.setObjectName(u"push_egal")
        sizePolicy.setHeightForWidth(self.push_egal.sizePolicy().hasHeightForWidth())
        self.push_egal.setSizePolicy(sizePolicy)
        self.push_egal.setStyleSheet(u"QPushButton{\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(243, 213, 40);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:30px\n"
"}")

        self.gridLayout.addWidget(self.push_egal, 6, 3, 1, 1)

        self.push_5 = QPushButton(self.centralwidget)
        self.push_5.setObjectName(u"push_5")
        sizePolicy.setHeightForWidth(self.push_5.sizePolicy().hasHeightForWidth())
        self.push_5.setSizePolicy(sizePolicy)
        self.push_5.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(172, 172, 172);\n"
"	border-radius: 30px;\n"
"}\n"
"QPushButtton:hover{\n"
"color:rgb(61,61,61);\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 30 px;\n"
"	gridline-color: rgb(239, 239, 239);\n"
"}")

        self.gridLayout.addWidget(self.push_5, 4, 1, 1, 1)

        self.push_1 = QPushButton(self.centralwidget)
        self.push_1.setObjectName(u"push_1")
        sizePolicy.setHeightForWidth(self.push_1.sizePolicy().hasHeightForWidth())
        self.push_1.setSizePolicy(sizePolicy)
        self.push_1.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(172, 172, 172);\n"
"	border-radius: 30px;\n"
"}\n"
"QPushButtton:hover{\n"
"color:rgb(61,61,61);\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 30 px;\n"
"	gridline-color: rgb(239, 239, 239);\n"
"}")

        self.gridLayout.addWidget(self.push_1, 3, 0, 1, 1)

        self.push_2 = QPushButton(self.centralwidget)
        self.push_2.setObjectName(u"push_2")
        sizePolicy.setHeightForWidth(self.push_2.sizePolicy().hasHeightForWidth())
        self.push_2.setSizePolicy(sizePolicy)
        self.push_2.setMinimumSize(QSize(0, 24))
        self.push_2.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(172, 172, 172);\n"
"	border-radius: 30px;\n"
"}\n"
"QPushButtton:hover{\n"
"color:rgb(61,61,61);\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 30 px;\n"
"	gridline-color: rgb(239, 239, 239);\n"
"}")

        self.gridLayout.addWidget(self.push_2, 3, 1, 1, 1)

        self.push_7 = QPushButton(self.centralwidget)
        self.push_7.setObjectName(u"push_7")
        sizePolicy.setHeightForWidth(self.push_7.sizePolicy().hasHeightForWidth())
        self.push_7.setSizePolicy(sizePolicy)
        self.push_7.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(172, 172, 172);\n"
"	border-radius: 30px;\n"
"}\n"
"QPushButtton:hover{\n"
"color:rgb(61,61,61);\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 30 px;\n"
"	gridline-color: rgb(239, 239, 239);\n"
"}")

        self.gridLayout.addWidget(self.push_7, 5, 0, 1, 1)

        self.push_3 = QPushButton(self.centralwidget)
        self.push_3.setObjectName(u"push_3")
        sizePolicy.setHeightForWidth(self.push_3.sizePolicy().hasHeightForWidth())
        self.push_3.setSizePolicy(sizePolicy)
        self.push_3.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(172, 172, 172);\n"
"	border-radius: 30px;\n"
"}\n"
"QPushButtton:hover{\n"
"color:rgb(61,61,61);\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 30 px;\n"
"	gridline-color: rgb(239, 239, 239);\n"
"}")

        self.gridLayout.addWidget(self.push_3, 3, 2, 1, 1)

        self.push_point = QPushButton(self.centralwidget)
        self.push_point.setObjectName(u"push_point")
        sizePolicy.setHeightForWidth(self.push_point.sizePolicy().hasHeightForWidth())
        self.push_point.setSizePolicy(sizePolicy)
        self.push_point.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(172, 172, 172);\n"
"	border-radius: 30px;\n"
"}\n"
"QPushButtton:hover{\n"
"color:rgb(61,61,61);\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 30 px;\n"
"	gridline-color: rgb(239, 239, 239);\n"
"}")

        self.gridLayout.addWidget(self.push_point, 6, 2, 1, 1)

        self.push_division = QPushButton(self.centralwidget)
        self.push_division.setObjectName(u"push_division")
        sizePolicy.setHeightForWidth(self.push_division.sizePolicy().hasHeightForWidth())
        self.push_division.setSizePolicy(sizePolicy)
        self.push_division.setStyleSheet(u"QPushButton{\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(243, 213, 40);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:30px\n"
"}")

        self.gridLayout.addWidget(self.push_division, 5, 3, 1, 1)

        self.push_del = QPushButton(self.centralwidget)
        self.push_del.setObjectName(u"push_del")
        sizePolicy.setHeightForWidth(self.push_del.sizePolicy().hasHeightForWidth())
        self.push_del.setSizePolicy(sizePolicy)
        self.push_del.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	\n"
"	background-color: rgb(255, 0, 0);\n"
"	border-radius: 30px;\n"
"}\n"
"QPushButtton:hover{\n"
"color:rgb(61,61,61);\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 30 px;\n"
"	gridline-color: rgb(239, 239, 239);\n"
"}")

        self.gridLayout.addWidget(self.push_del, 2, 2, 1, 1)

        self.push_fois = QPushButton(self.centralwidget)
        self.push_fois.setObjectName(u"push_fois")
        sizePolicy.setHeightForWidth(self.push_fois.sizePolicy().hasHeightForWidth())
        self.push_fois.setSizePolicy(sizePolicy)
        self.push_fois.setStyleSheet(u"QPushButton{\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(243, 213, 40);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:30px\n"
"}")

        self.gridLayout.addWidget(self.push_fois, 4, 3, 1, 1)

        self.push_moin = QPushButton(self.centralwidget)
        self.push_moin.setObjectName(u"push_moin")
        sizePolicy.setHeightForWidth(self.push_moin.sizePolicy().hasHeightForWidth())
        self.push_moin.setSizePolicy(sizePolicy)
        self.push_moin.setStyleSheet(u"QPushButton{\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(243, 213, 40);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:30px\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../assets/Screenshot_2026-11-18_182242-removebg-preview.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.push_moin.setIcon(icon1)
        self.push_moin.setIconSize(QSize(0, 16))

        self.gridLayout.addWidget(self.push_moin, 3, 3, 1, 1)

        self.push_clear = QPushButton(self.centralwidget)
        self.push_clear.setObjectName(u"push_clear")
        sizePolicy.setHeightForWidth(self.push_clear.sizePolicy().hasHeightForWidth())
        self.push_clear.setSizePolicy(sizePolicy)
        self.push_clear.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(172, 172, 172);\n"
"	border-radius: 30px;\n"
"}\n"
"QPushButtton:hover{\n"
"color:rgb(61,61,61);\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 30 px;\n"
"	gridline-color: rgb(239, 239, 239);\n"
"}")
        self.push_clear.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.push_clear, 2, 0, 1, 2)

        self.push_8 = QPushButton(self.centralwidget)
        self.push_8.setObjectName(u"push_8")
        sizePolicy.setHeightForWidth(self.push_8.sizePolicy().hasHeightForWidth())
        self.push_8.setSizePolicy(sizePolicy)
        self.push_8.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(172, 172, 172);\n"
"	border-radius: 30px;\n"
"}\n"
"QPushButtton:hover{\n"
"color:rgb(61,61,61);\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 30 px;\n"
"	gridline-color: rgb(239, 239, 239);\n"
"}")

        self.gridLayout.addWidget(self.push_8, 5, 1, 1, 1)

        self.push_6 = QPushButton(self.centralwidget)
        self.push_6.setObjectName(u"push_6")
        sizePolicy.setHeightForWidth(self.push_6.sizePolicy().hasHeightForWidth())
        self.push_6.setSizePolicy(sizePolicy)
        self.push_6.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(172, 172, 172);\n"
"	border-radius: 30px;\n"
"}\n"
"QPushButtton:hover{\n"
"color:rgb(61,61,61);\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 30 px;\n"
"	gridline-color: rgb(239, 239, 239);\n"
"}")

        self.gridLayout.addWidget(self.push_6, 4, 2, 1, 1)

        self.push_9 = QPushButton(self.centralwidget)
        self.push_9.setObjectName(u"push_9")
        sizePolicy.setHeightForWidth(self.push_9.sizePolicy().hasHeightForWidth())
        self.push_9.setSizePolicy(sizePolicy)
        self.push_9.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(172, 172, 172);\n"
"	border-radius: 30px;\n"
"}\n"
"QPushButtton:hover{\n"
"color:rgb(61,61,61);\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 30 px;\n"
"	gridline-color: rgb(239, 239, 239);\n"
"}")

        self.gridLayout.addWidget(self.push_9, 5, 2, 1, 1)

        self.push_4 = QPushButton(self.centralwidget)
        self.push_4.setObjectName(u"push_4")
        sizePolicy.setHeightForWidth(self.push_4.sizePolicy().hasHeightForWidth())
        self.push_4.setSizePolicy(sizePolicy)
        self.push_4.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(172, 172, 172);\n"
"	border-radius: 30px;\n"
"}\n"
"QPushButtton:hover{\n"
"color:rgb(61,61,61);\n"
"	font: 700 20pt \"Segoe UI\";\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 30 px;\n"
"	gridline-color: rgb(239, 239, 239);\n"
"}")

        self.gridLayout.addWidget(self.push_4, 4, 0, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(154, 154, 154);")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 4)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.push_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.push_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.push_egal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.push_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.push_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.push_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.push_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.push_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.push_point.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.push_division.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.push_del.setText(QCoreApplication.translate("MainWindow", u"del", None))
        self.push_fois.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.push_moin.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.push_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.push_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.push_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.push_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.push_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
    # retranslateUi

