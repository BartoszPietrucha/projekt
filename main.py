from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from src.UI.templates.LogInPage import Ui_Form
from src.UI.templates.MainWindow import Ui_MainWindow
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import QTimer
import os

class LoginPage(QWidget, Ui_Form):

    def __init__(self, mainwindow):
        super().__init__()
        self.setupUi(self)
        self.mainwindow = mainwindow
        self.bt_login.clicked.connect(self.login)
        self.bt_rejestr.setToolTip("jeśli chcesz zarejestrowa c to kliknij zaloguj")
        

    def login(self):
        self.hide()
        self.mainwindow.show()
        
        

class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loginpage = LoginPage(self)
        self.loginpage.show()
        self.l_photos.setScaledContents(True)
        self.images = ["C:/Programy/python/projekt/projekt/src/UI/apartment2.jpg",
                       "C:/Programy/python/projekt/projekt/src/UI/apartment.jpg"]
        self.current_image_index = 0
        self.show_image(self.images[self.current_image_index])

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.next_image)
        self.timer.start(5000)

        self.bt_right.clicked.connect(self.next_image)
        self.bt_left.clicked.connect(self.previous_image)
        


    def show_image(self,image_path):
        if os.path.exists(image_path):
            image = QImage(image_path)
            pixmap = QPixmap(image)
            self.l_photos.setPixmap(pixmap)
        else:
            print(f"Plik {image_path} nie istnieje")

    def next_image(self):
        self.current_image_index = (self.current_image_index+1) % len(self.images)
        next_image = self.images[self.current_image_index]
        self.show_image(next_image)

    def previous_image(self):
        self.current_image_index = (self.current_image_index-1) % len(self.images)
        previous_image = self.images[self.current_image_index]
        self.show_image(previous_image)

if __name__ == "__main__":
    app = QApplication()
    widget = MainWindow()
    
    
    app.exec()


