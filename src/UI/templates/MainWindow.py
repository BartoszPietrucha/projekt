# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(150, 0))
        self.frame_3.setMaximumSize(QSize(150, 16777215))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.bt_mieszkania = QPushButton(self.frame_3)
        self.bt_mieszkania.setObjectName(u"bt_mieszkania")
        self.bt_mieszkania.setGeometry(QRect(20, 10, 93, 29))
        self.bt_konto = QPushButton(self.frame_3)
        self.bt_konto.setObjectName(u"bt_konto")
        self.bt_konto.setGeometry(QRect(20, 50, 93, 29))
        self.bt_wyloguj = QPushButton(self.frame_3)
        self.bt_wyloguj.setObjectName(u"bt_wyloguj")
        self.bt_wyloguj.setGeometry(QRect(20, 90, 93, 29))

        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: #92a8d1;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_4 = QHBoxLayout(self.page)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.bt_mieszkania_3 = QPushButton(self.page)
        self.bt_mieszkania_3.setObjectName(u"bt_mieszkania_3")

        self.horizontalLayout_4.addWidget(self.bt_mieszkania_3)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_5 = QHBoxLayout(self.page_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.bt_mieszkania_2 = QPushButton(self.page_2)
        self.bt_mieszkania_2.setObjectName(u"bt_mieszkania_2")

        self.horizontalLayout_5.addWidget(self.bt_mieszkania_2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_3 = QHBoxLayout(self.page_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.l_photos = QLabel(self.page_3)
        self.l_photos.setObjectName(u"l_photos")
        self.l_photos.setMaximumSize(QSize(500, 500))

        self.horizontalLayout_3.addWidget(self.l_photos)

        self.stackedWidget.addWidget(self.page_3)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_mieszkania.setText(QCoreApplication.translate("MainWindow", u"mieszkania", None))
        self.bt_konto.setText(QCoreApplication.translate("MainWindow", u"konto", None))
        self.bt_wyloguj.setText(QCoreApplication.translate("MainWindow", u"wyloguj si\u0119", None))
        self.bt_mieszkania_3.setText(QCoreApplication.translate("MainWindow", u"mieszkania", None))
        self.bt_mieszkania_2.setText(QCoreApplication.translate("MainWindow", u"mieszkania", None))
        self.l_photos.setText(QCoreApplication.translate("MainWindow", u"zdjecia", None))
    # retranslateUi

