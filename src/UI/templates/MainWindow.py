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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStackedWidget,
    QStatusBar, QVBoxLayout, QWidget)

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
        self.l_kontophoto.setMaximumSize(QSize(200, 200))

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
        self.frame_7 = QFrame(self.page_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.l_plus = QLabel(self.frame_8)
        self.l_plus.setObjectName(u"l_plus")
        self.l_plus.setMinimumSize(QSize(250, 0))
        self.l_plus.setMaximumSize(QSize(16777215, 250))

        self.gridLayout.addWidget(self.l_plus, 0, 0, 1, 1)

        self.label_10 = QLabel(self.frame_8)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)


        self.horizontalLayout_7.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.l_plik = QLabel(self.frame_9)
        self.l_plik.setObjectName(u"l_plik")
        self.l_plik.setMinimumSize(QSize(250, 0))
        self.l_plik.setMaximumSize(QSize(16777215, 250))

        self.verticalLayout_3.addWidget(self.l_plik)

        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_3.addWidget(self.label_11)


        self.horizontalLayout_7.addWidget(self.frame_9)


        self.horizontalLayout_5.addWidget(self.frame_7)

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
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_8 = QHBoxLayout(self.page_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_10 = QFrame(self.page_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_17 = QFrame(self.frame_11)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_17)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_8 = QLabel(self.frame_17)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_5.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_17)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_5.addWidget(self.label_9)

        self.label_12 = QLabel(self.frame_17)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_5.addWidget(self.label_12)


        self.horizontalLayout_9.addWidget(self.frame_17)

        self.frame_15 = QFrame(self.frame_11)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(150, 16777215))
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.l_miasto = QLineEdit(self.frame_15)
        self.l_miasto.setObjectName(u"l_miasto")

        self.verticalLayout_6.addWidget(self.l_miasto)

        self.l_ulica = QLineEdit(self.frame_15)
        self.l_ulica.setObjectName(u"l_ulica")

        self.verticalLayout_6.addWidget(self.l_ulica)

        self.l_adres_pocz = QLineEdit(self.frame_15)
        self.l_adres_pocz.setObjectName(u"l_adres_pocz")

        self.verticalLayout_6.addWidget(self.l_adres_pocz)


        self.horizontalLayout_9.addWidget(self.frame_15)

        self.frame_14 = QFrame(self.frame_11)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_14)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_13 = QLabel(self.frame_14)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_7.addWidget(self.label_13)

        self.label_15 = QLabel(self.frame_14)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_7.addWidget(self.label_15)

        self.label_14 = QLabel(self.frame_14)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_7.addWidget(self.label_14)


        self.horizontalLayout_9.addWidget(self.frame_14)

        self.frame_16 = QFrame(self.frame_11)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_16)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.l_numer_budy = QLineEdit(self.frame_16)
        self.l_numer_budy.setObjectName(u"l_numer_budy")

        self.verticalLayout_8.addWidget(self.l_numer_budy)

        self.l_numer_lok = QLineEdit(self.frame_16)
        self.l_numer_lok.setObjectName(u"l_numer_lok")

        self.verticalLayout_8.addWidget(self.l_numer_lok)

        self.l_metraz = QLineEdit(self.frame_16)
        self.l_metraz.setObjectName(u"l_metraz")

        self.verticalLayout_8.addWidget(self.l_metraz)


        self.horizontalLayout_9.addWidget(self.frame_16)


        self.verticalLayout_4.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_18 = QFrame(self.frame_12)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_18)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_16 = QLabel(self.frame_18)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_9.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_18)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_9.addWidget(self.label_17)

        self.label_18 = QLabel(self.frame_18)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_9.addWidget(self.label_18)


        self.horizontalLayout_10.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_12)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(150, 16777215))
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_19)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.l_ilosc_pokoi = QLineEdit(self.frame_19)
        self.l_ilosc_pokoi.setObjectName(u"l_ilosc_pokoi")

        self.verticalLayout_10.addWidget(self.l_ilosc_pokoi)

        self.l_wlasciciel = QLineEdit(self.frame_19)
        self.l_wlasciciel.setObjectName(u"l_wlasciciel")

        self.verticalLayout_10.addWidget(self.l_wlasciciel)

        self.l_stan = QLineEdit(self.frame_19)
        self.l_stan.setObjectName(u"l_stan")

        self.verticalLayout_10.addWidget(self.l_stan)


        self.horizontalLayout_10.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_12)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_20)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_19 = QLabel(self.frame_20)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_11.addWidget(self.label_19)

        self.label_20 = QLabel(self.frame_20)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_11.addWidget(self.label_20)

        self.label_21 = QLabel(self.frame_20)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_11.addWidget(self.label_21)


        self.horizontalLayout_10.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_12)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_21)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.cb_osoba_wc = QComboBox(self.frame_21)
        self.cb_osoba_wc.setObjectName(u"cb_osoba_wc")

        self.verticalLayout_12.addWidget(self.cb_osoba_wc)

        self.l_cena = QLineEdit(self.frame_21)
        self.l_cena.setObjectName(u"l_cena")

        self.verticalLayout_12.addWidget(self.l_cena)

        self.l_opis = QLineEdit(self.frame_21)
        self.l_opis.setObjectName(u"l_opis")

        self.verticalLayout_12.addWidget(self.l_opis)


        self.horizontalLayout_10.addWidget(self.frame_21)


        self.verticalLayout_4.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_13)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.bt_zapisz_dane = QPushButton(self.frame_13)
        self.bt_zapisz_dane.setObjectName(u"bt_zapisz_dane")

        self.verticalLayout_13.addWidget(self.bt_zapisz_dane)

        self.bt_resident_add_photos = QPushButton(self.frame_13)
        self.bt_resident_add_photos.setObjectName(u"bt_resident_add_photos")

        self.verticalLayout_13.addWidget(self.bt_resident_add_photos)

        self.bt_dodaj_najemcow = QPushButton(self.frame_13)
        self.bt_dodaj_najemcow.setObjectName(u"bt_dodaj_najemcow")

        self.verticalLayout_13.addWidget(self.bt_dodaj_najemcow)


        self.verticalLayout_4.addWidget(self.frame_13)


        self.horizontalLayout_8.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.horizontalLayout_11 = QHBoxLayout(self.page_5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_22 = QFrame(self.page_5)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_22)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(400, 200))
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_26 = QFrame(self.frame_23)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.l_resident_photo = QLabel(self.frame_26)
        self.l_resident_photo.setObjectName(u"l_resident_photo")

        self.horizontalLayout_13.addWidget(self.l_resident_photo)


        self.horizontalLayout_12.addWidget(self.frame_26)

        self.frame_28 = QFrame(self.frame_23)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_12.addWidget(self.frame_28)

        self.frame_27 = QFrame(self.frame_23)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_12.addWidget(self.frame_27)


        self.verticalLayout_14.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_22)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_29 = QFrame(self.frame_24)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_29)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_22 = QLabel(self.frame_29)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_15.addWidget(self.label_22)

        self.label_23 = QLabel(self.frame_29)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_15.addWidget(self.label_23)

        self.label_24 = QLabel(self.frame_29)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_15.addWidget(self.label_24)


        self.horizontalLayout_14.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_24)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(150, 16777215))
        self.frame_30.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_30)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.l_resident_name = QLineEdit(self.frame_30)
        self.l_resident_name.setObjectName(u"l_resident_name")

        self.verticalLayout_16.addWidget(self.l_resident_name)

        self.l_resident_surname = QLineEdit(self.frame_30)
        self.l_resident_surname.setObjectName(u"l_resident_surname")

        self.verticalLayout_16.addWidget(self.l_resident_surname)

        self.l_resident_city = QLineEdit(self.frame_30)
        self.l_resident_city.setObjectName(u"l_resident_city")

        self.verticalLayout_16.addWidget(self.l_resident_city)


        self.horizontalLayout_14.addWidget(self.frame_30)

        self.frame_32 = QFrame(self.frame_24)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_32)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_25 = QLabel(self.frame_32)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_17.addWidget(self.label_25)

        self.label_26 = QLabel(self.frame_32)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_17.addWidget(self.label_26)

        self.label_27 = QLabel(self.frame_32)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_17.addWidget(self.label_27)


        self.horizontalLayout_14.addWidget(self.frame_32)

        self.frame_31 = QFrame(self.frame_24)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_31)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.l_resident_street = QLineEdit(self.frame_31)
        self.l_resident_street.setObjectName(u"l_resident_street")

        self.verticalLayout_18.addWidget(self.l_resident_street)

        self.l_resident_number_app = QLineEdit(self.frame_31)
        self.l_resident_number_app.setObjectName(u"l_resident_number_app")

        self.verticalLayout_18.addWidget(self.l_resident_number_app)

        self.l_resident_number2 = QLineEdit(self.frame_31)
        self.l_resident_number2.setObjectName(u"l_resident_number2")

        self.verticalLayout_18.addWidget(self.l_resident_number2)


        self.horizontalLayout_14.addWidget(self.frame_31)


        self.verticalLayout_14.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.frame_22)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_33 = QFrame(self.frame_25)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_33)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_28 = QLabel(self.frame_33)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_19.addWidget(self.label_28)

        self.label_30 = QLabel(self.frame_33)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_19.addWidget(self.label_30)

        self.label_29 = QLabel(self.frame_33)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_19.addWidget(self.label_29)


        self.horizontalLayout_15.addWidget(self.frame_33)

        self.frame_35 = QFrame(self.frame_25)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMaximumSize(QSize(250, 16777215))
        self.frame_35.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_35)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.l_resident_phone = QLineEdit(self.frame_35)
        self.l_resident_phone.setObjectName(u"l_resident_phone")

        self.verticalLayout_20.addWidget(self.l_resident_phone)

        self.l_resident_email = QLineEdit(self.frame_35)
        self.l_resident_email.setObjectName(u"l_resident_email")

        self.verticalLayout_20.addWidget(self.l_resident_email)

        self.l_resident_addres = QLineEdit(self.frame_35)
        self.l_resident_addres.setObjectName(u"l_resident_addres")

        self.verticalLayout_20.addWidget(self.l_resident_addres)


        self.horizontalLayout_15.addWidget(self.frame_35)

        self.frame_37 = QFrame(self.frame_25)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_15.addWidget(self.frame_37)

        self.frame_36 = QFrame(self.frame_25)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_15.addWidget(self.frame_36)


        self.verticalLayout_14.addWidget(self.frame_25)


        self.horizontalLayout_11.addWidget(self.frame_22)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.stackedWidget.addWidget(self.page_7)

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

        self.stackedWidget.setCurrentIndex(5)


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
        self.l_plus.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Dodaj mieszkanie", None))
        self.l_plik.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Lista mieszka\u0144", None))
        self.bt_left.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.l_photos.setText(QCoreApplication.translate("MainWindow", u"                                                        zdjecia", None))
        self.bt_right.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Miasto", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Ulica", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Adres pocztowy", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"numer budynku", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"numer lokalu", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"metra\u017c", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"ilo\u015b\u0107 pokoi", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"w\u0142a\u015bciciel", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"stan", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"osobna ubikacja", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"cena wynajmu", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"opis(dodatkowo)", None))
        self.bt_zapisz_dane.setText(QCoreApplication.translate("MainWindow", u"zapisz dane", None))
        self.bt_resident_add_photos.setText(QCoreApplication.translate("MainWindow", u"dodaj zdj\u0119cia mieszkania", None))
        self.bt_dodaj_najemcow.setText(QCoreApplication.translate("MainWindow", u"dodaj najemc\u00f3w", None))
        self.l_resident_photo.setText(QCoreApplication.translate("MainWindow", u"zdjecie", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Imi\u0119", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Nazwisko", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"miasto", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"ulica", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"numer budynku", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"numer lokalu", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"telefon", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"email", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"adres pocztowy", None))
    # retranslateUi

