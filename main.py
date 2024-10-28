from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from src.UI.templates.LogInPage import Ui_Form
from src.UI.templates.MainWindow import Ui_MainWindow
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import QTimer
import os
from src.db.db_init.initialize_db import UserData, Session, Users



#trzeba sprawdzić login i hasło
#dodawanie mieszkania
#widget konta, update konta
#dodawanie zdjęć
#dodanie zdjec mieszkań na strone startową
#hashowanie hasła
#dodawanie residents
#usuwanie mieszkania
#update zdjec mieszkań 
#usuwanie mieszkania,konta






class LoginPage(QWidget, Ui_Form):

    def __init__(self, mainwindow):
        super().__init__()
        self.setupUi(self)
        self.mainwindow = mainwindow
        self.stackedWidget.setCurrentWidget(self.page_2)
        self.bt_login.clicked.connect(self.login)
        self.bt_rejestr.clicked.connect(self.rejestr)
        self.bt_rejestr.setToolTip("juuuuuuhuuu")
        self.bt_ok.clicked.connect(self.test)

    def login(self):
        username = self.le_login.text()
        password = self.le_haslo.text()

        db_session = Session()
        try:
            user = db_session.query(Users).filter_by(username=username).first()
            if user:
                if user.password_hashed == password:
                    print("zalogowano pomyślnie")
                    self.hide()
                    self.mainwindow.show()
                else:
                    print("błędne hasło")
            else:
                print("Użytkownik nie istnieje")
        except Exception as e:
            print(f"wystapil blad podczas logowania: {e}")
        finally:
            db_session.close()
        
        

    def rejestr(self):
        self.stackedWidget.setCurrentWidget(self.page)
        
        
    def test(self):
        if not all([self.le_username, self.le_firstname, self.le_surname, self.le_email, self.le_phone, self.le_password]):
            print("Wszystkie pola muszą być wypełnione!")
            return

        new_user = Users()
        new_user.username = self.le_username.text()
        new_user.firstname = self.le_firstname.text()
        new_user.surname = self.le_surname.text()
        new_user.email = self.le_email.text()
        new_user.phone = self.le_phone.text()
        new_user.password_hashed = self.le_password.text()
        new_user.profile_b64 = self.le_profile_b64.text() if self.le_profile_b64.text() else None
        
        
        db_session = Session()
        try:
            db_session.add(new_user)
            db_session.commit()
            print("Użytkownik został pomyślnie dodany do bazy danych.")
        except Exception as e:
            db_session.rollback()
            print(f"Wystąpił błąd podczas dodawania użytkowania: {e}")
        finally:
            db_session.close()
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
        self.stackedWidget.setCurrentWidget(self.page_3)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.next_image)
        self.timer.start(5000)

        self.bt_right.clicked.connect(self.next_image)
        self.bt_left.clicked.connect(self.previous_image)
        
        self.bt_mieszkania.clicked.connect(self.show_page2)


    def reset_timer(self):
        self.timer.stop()
        self.timer.start(5000)

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
        self.reset_timer()

    def previous_image(self):
        self.current_image_index = (self.current_image_index-1) % len(self.images)
        previous_image = self.images[self.current_image_index]
        self.show_image(previous_image)
        self.reset_timer()
    
    def show_page2(self):
        self.stackedWidget.setCurrentWidget(self.page_2)

if __name__ == "__main__":
    app = QApplication()
    widget = MainWindow()
    
    
    app.exec()


