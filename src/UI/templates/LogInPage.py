# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginPage.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(872, 489)
        Form.setStyleSheet(u"#frame{\n"
"background-image:url(\"C:/Programy/python/projekt/projekt/src/UI/apartment.jpg\");\n"
"background-position: top center;\n"
"width: 100%;\n"
"height: 100%;\n"
"background-repeat: no-repeat;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_6 = QHBoxLayout(self.page)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_13 = QFrame(self.page)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 0))
        self.frame_13.setMaximumSize(QSize(16777215, 500))
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 400))
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_14)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.frame_14)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_14)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_4.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_14)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_14)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_4.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_14)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_4.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_14)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_4.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_14)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_4.addWidget(self.label_11)


        self.horizontalLayout_7.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(500, 400))
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.le_username = QLineEdit(self.frame_15)
        self.le_username.setObjectName(u"le_username")

        self.verticalLayout_5.addWidget(self.le_username)

        self.le_firstname = QLineEdit(self.frame_15)
        self.le_firstname.setObjectName(u"le_firstname")

        self.verticalLayout_5.addWidget(self.le_firstname)

        self.le_surname = QLineEdit(self.frame_15)
        self.le_surname.setObjectName(u"le_surname")

        self.verticalLayout_5.addWidget(self.le_surname)

        self.le_email = QLineEdit(self.frame_15)
        self.le_email.setObjectName(u"le_email")

        self.verticalLayout_5.addWidget(self.le_email)

        self.le_phone = QLineEdit(self.frame_15)
        self.le_phone.setObjectName(u"le_phone")

        self.verticalLayout_5.addWidget(self.le_phone)

        self.le_password = QLineEdit(self.frame_15)
        self.le_password.setObjectName(u"le_password")

        self.verticalLayout_5.addWidget(self.le_password)

        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 100))
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.bt_regpath = QPushButton(self.frame_17)
        self.bt_regpath.setObjectName(u"bt_regpath")

        self.horizontalLayout_8.addWidget(self.bt_regpath)

        self.l_regphoto = QLabel(self.frame_17)
        self.l_regphoto.setObjectName(u"l_regphoto")

        self.horizontalLayout_8.addWidget(self.l_regphoto)


        self.verticalLayout_5.addWidget(self.frame_17)


        self.horizontalLayout_7.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(50, 0))
        self.frame_16.setMaximumSize(QSize(100, 16777215))
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_16)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.bt_ok = QPushButton(self.frame_16)
        self.bt_ok.setObjectName(u"bt_ok")

        self.verticalLayout_6.addWidget(self.bt_ok)


        self.horizontalLayout_7.addWidget(self.frame_16)


        self.horizontalLayout_6.addWidget(self.frame_13)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 850, 467))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_3.addWidget(self.frame_6)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(300, 800))
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 80))
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 40))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.frame_9)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 100))
        self.frame_7.setMaximumSize(QSize(16777215, 100))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.frame_10)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 15))

        self.horizontalLayout_4.addWidget(self.label)

        self.le_login = QLineEdit(self.frame_10)
        self.le_login.setObjectName(u"le_login")
        self.le_login.setMinimumSize(QSize(0, 20))
        self.le_login.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.le_login.setDragEnabled(False)

        self.horizontalLayout_4.addWidget(self.le_login)


        self.verticalLayout_3.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.frame_11)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_5.addWidget(self.label_3)

        self.le_haslo = QLineEdit(self.frame_11)
        self.le_haslo.setObjectName(u"le_haslo")
        self.le_haslo.setMinimumSize(QSize(0, 20))
        self.le_haslo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.le_haslo)


        self.verticalLayout_3.addWidget(self.frame_11)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 50))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.bt_login = QPushButton(self.frame_8)
        self.bt_login.setObjectName(u"bt_login")
        self.bt_login.setGeometry(QRect(10, 10, 93, 29))
        self.bt_rejestr = QPushButton(self.frame_8)
        self.bt_rejestr.setObjectName(u"bt_rejestr")
        self.bt_rejestr.setGeometry(QRect(120, 10, 93, 29))

        self.verticalLayout_2.addWidget(self.frame_8)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 60))
        self.frame_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_5)


        self.horizontalLayout_3.addWidget(self.frame_2)

        self.frame_12 = QFrame(self.frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setEnabled(True)
        self.frame_12.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Shadow.Sunken)
        self.frame_12.setLineWidth(0)

        self.horizontalLayout_3.addWidget(self.frame_12)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"username/login", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"firstname", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"surname", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"email", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"phone", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"password", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"profile_b64", None))
        self.bt_regpath.setText(QCoreApplication.translate("Form", u"Wybierz zdj\u0119cie", None))
        self.l_regphoto.setText(QCoreApplication.translate("Form", u"zdjecie", None))
        self.bt_ok.setText(QCoreApplication.translate("Form", u"OK", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Zaloguj si\u0119", None))
        self.label.setText(QCoreApplication.translate("Form", u"login", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"has\u0142o", None))
        self.bt_login.setText(QCoreApplication.translate("Form", u"Zaloguj si\u0119", None))
        self.bt_rejestr.setText(QCoreApplication.translate("Form", u"Rejestracja", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"ajk co\u015b p\u00f3jdzie nie tak", None))
    # retranslateUi

