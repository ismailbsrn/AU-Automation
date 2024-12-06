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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QWidget)
from ApplicationUI.Resources import Resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(633, 183)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label_FilePath = QLabel(self.groupBox)
        self.label_FilePath.setObjectName(u"label_FilePath")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_FilePath)

        self.lineEdit_FilePath = QLineEdit(self.groupBox)
        self.lineEdit_FilePath.setObjectName(u"lineEdit_FilePath")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_FilePath)

        self.pushButton_ChooseFile = QPushButton(self.groupBox)
        self.pushButton_ChooseFile.setObjectName(u"pushButton_ChooseFile")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.pushButton_ChooseFile)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(2, QFormLayout.FieldRole, self.verticalSpacer)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 633, 33))
        self.menubar_Dosya = QMenu(self.menubar)
        self.menubar_Dosya.setObjectName(u"menubar_Dosya")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menubar_Dosya.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TimeTable Creator", None))
        self.groupBox.setTitle("")
        self.label_FilePath.setText(QCoreApplication.translate("MainWindow", u"Dosya Yolu:", None))
        self.pushButton_ChooseFile.setText(QCoreApplication.translate("MainWindow", u"Dosya Se\u00e7", None))
        self.menubar_Dosya.setTitle(QCoreApplication.translate("MainWindow", u"Dosya", None))
    # retranslateUi

