# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)
from ApplicationUI.Resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(451, 411)
        icon = QIcon()
        icon.addFile(u":/Icons/Ankara_University_Logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label_FilePath = QLabel(self.groupBox)
        self.label_FilePath.setObjectName(u"label_FilePath")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_FilePath)

        self.lineEdit_FilePath = QLineEdit(self.groupBox)
        self.lineEdit_FilePath.setObjectName(u"lineEdit_FilePath")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_FilePath)

        self.pushButton_ChooseFile = QPushButton(self.groupBox)
        self.pushButton_ChooseFile.setObjectName(u"pushButton_ChooseFile")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.pushButton_ChooseFile)

        self.label_ExcelInputDesc = QLabel(self.groupBox)
        self.label_ExcelInputDesc.setObjectName(u"label_ExcelInputDesc")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_ExcelInputDesc)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_Compile = QPushButton(self.groupBox_2)
        self.pushButton_Compile.setObjectName(u"pushButton_Compile")

        self.gridLayout_2.addWidget(self.pushButton_Compile, 0, 0, 1, 1)

        self.pushButton_CreateTimeTable = QPushButton(self.groupBox_2)
        self.pushButton_CreateTimeTable.setObjectName(u"pushButton_CreateTimeTable")

        self.gridLayout_2.addWidget(self.pushButton_CreateTimeTable, 1, 0, 1, 1)

        self.pushButton_Print = QPushButton(self.groupBox_2)
        self.pushButton_Print.setObjectName(u"pushButton_Print")

        self.gridLayout_2.addWidget(self.pushButton_Print, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_DaysInput = QLineEdit(self.groupBox_3)
        self.lineEdit_DaysInput.setObjectName(u"lineEdit_DaysInput")

        self.gridLayout_3.addWidget(self.lineEdit_DaysInput, 1, 0, 1, 1)

        self.label_DaysInputLabel = QLabel(self.groupBox_3)
        self.label_DaysInputLabel.setObjectName(u"label_DaysInputLabel")

        self.gridLayout_3.addWidget(self.label_DaysInputLabel, 0, 0, 1, 1)

        self.label_HoursInputLabel = QLabel(self.groupBox_3)
        self.label_HoursInputLabel.setObjectName(u"label_HoursInputLabel")

        self.gridLayout_3.addWidget(self.label_HoursInputLabel, 2, 0, 1, 1)

        self.lineEdit_HoursInput = QLineEdit(self.groupBox_3)
        self.lineEdit_HoursInput.setObjectName(u"lineEdit_HoursInput")

        self.gridLayout_3.addWidget(self.lineEdit_HoursInput, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 451, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AU - TimeTable Creator", None))
        self.groupBox.setTitle("")
        self.label_FilePath.setText(QCoreApplication.translate("MainWindow", u"Dosya Yolu:", None))
        self.pushButton_ChooseFile.setText(QCoreApplication.translate("MainWindow", u"Dosya Se\u00e7", None))
        self.label_ExcelInputDesc.setText(QCoreApplication.translate("MainWindow", u"\u0130\u00e7e aktar\u0131lacak Excel dosyas\u0131n\u0131 se\u00e7iniz:", None))
        self.groupBox_2.setTitle("")
        self.pushButton_Compile.setText(QCoreApplication.translate("MainWindow", u"Derle", None))
        self.pushButton_CreateTimeTable.setText(QCoreApplication.translate("MainWindow", u"Olu\u015ftur", None))
        self.pushButton_Print.setText(QCoreApplication.translate("MainWindow", u"Yazd\u0131r", None))
        self.groupBox_3.setTitle("")
        self.label_DaysInputLabel.setText(QCoreApplication.translate("MainWindow", u"G\u00fcnleri virg\u00fcl ile ay\u0131rarak giriniz:", None))
        self.label_HoursInputLabel.setText(QCoreApplication.translate("MainWindow", u"Saatleri virg\u00fcl ile ay\u0131rarak giriniz:", None))
    # retranslateUi

