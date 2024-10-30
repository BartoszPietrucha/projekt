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
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

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
        self.frame_4 = QFrame(self.page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)


        self.horizontalLayout_4.addWidget(self.frame_4)

        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.le_kontouser = QLineEdit(self.frame)
        self.le_kontouser.setObjectName(u"le_kontouser")

        self.verticalLayout_2.addWidget(self.le_kontouser)

        self.le_kontofirstname = QLineEdit(self.frame)
        self.le_kontofirstname.setObjectName(u"le_kontofirstname")

        self.verticalLayout_2.addWidget(self.le_kontofirstname)

        self.le_kontosurname = QLineEdit(self.frame)
        self.le_kontosurname.setObjectName(u"le_kontosurname")

        self.verticalLayout_2.addWidget(self.le_kontosurname)

        self.le_kontoemail = QLineEdit(self.frame)
        self.le_kontoemail.setObjectName(u"le_kontoemail")

        self.verticalLayout_2.addWidget(self.le_kontoemail)

        self.le_kontophone = QLineEdit(self.frame)
        self.le_kontophone.setObjectName(u"le_kontophone")

        self.verticalLayout_2.addWidget(self.le_kontophone)

        self.le_kontopassword = QLineEdit(self.frame)
        self.le_kontopassword.setObjectName(u"le_kontopassword")

        self.verticalLayout_2.addWidget(self.le_kontopassword)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 100))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.bt_kontouploadphoto = QPushButton(self.frame_6)
        self.bt_kontouploadphoto.setObjectName(u"bt_kontouploadphoto")

        self.horizontalLayout_6.addWidget(self.bt_kontouploadphoto)

        self.l_kontophoto = QLabel(self.frame_6)
        self.l_kontophoto.setObjectName(u"l_kontophoto")

        self.horizontalLayout_6.addWidget(self.l_kontophoto)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.horizontalLayout_4.addWidget(self.frame)

        self.frame_5 = QFrame(self.page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(100, 0))
        self.frame_5.setMaximumSize(QSize(100, 16777215))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.bt_edytuj = QPushButton(self.frame_5)
        self.bt_edytuj.setObjectName(u"bt_edytuj")
        self.bt_edytuj.setGeometry(QRect(10, 250, 93, 29))

        self.horizontalLayout_4.addWidget(self.frame_5)

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
        self.bt_left = QPushButton(self.page_3)
        self.bt_left.setObjectName(u"bt_left")
        self.bt_left.setMinimumSize(QSize(0, 450))
        self.bt_left.setMaximumSize(QSize(25, 16777215))

        self.horizontalLayout_3.addWidget(self.bt_left)

        self.l_photos = QLabel(self.page_3)
        self.l_photos.setObjectName(u"l_photos")
        self.l_photos.setMaximumSize(QSize(500, 500))

        self.horizontalLayout_3.addWidget(self.l_photos)

        self.bt_right = QPushButton(self.page_3)
        self.bt_right.setObjectName(u"bt_right")
        self.bt_right.setMaximumSize(QSize(25, 450))

        self.horizontalLayout_3.addWidget(self.bt_right)

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

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_mieszkania.setText(QCoreApplication.translate("MainWindow", u"mieszkania", None))
        self.bt_konto.setText(QCoreApplication.translate("MainWindow", u"konto", None))
        self.bt_wyloguj.setText(QCoreApplication.translate("MainWindow", u"wyloguj si\u0119", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"username", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"firstname", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"surname", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"email", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"phone", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"password", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"profile_b64", None))
        self.bt_kontouploadphoto.setText(QCoreApplication.translate("MainWindow", u"Wybierz zdj\u0119cie", None))
        self.l_kontophoto.setText(QCoreApplication.translate("MainWindow", u"Zdj\u0119cie", None))
        self.bt_edytuj.setText(QCoreApplication.translate("MainWindow", u"Edytuj", None))
        self.bt_mieszkania_2.setText(QCoreApplication.translate("MainWindow", u"mieszkania", None))
        self.bt_left.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.l_photos.setText(QCoreApplication.translate("MainWindow", u"                                                        zdjecia", None))
        self.bt_right.setText(QCoreApplication.translate("MainWindow", u">", None))
    # retranslateUi

