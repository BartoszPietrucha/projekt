from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog
from src.UI.templates.LogInPage import Ui_Form
from src.UI.templates.MainWindow import Ui_MainWindow
from PySide6.QtGui import QPixmap, QImage, QCursor, QMouseEvent
from PySide6.QtCore import QTimer, QByteArray, Qt
import os
from src.db.db_init.initialize_db import UserData, Session, Users, Apartments, Info, Photos
import base64




#dodanie residenta

#obejrzenie zdjecia jednego mieszkania
#obejrzenie danych mieszkania

#dodawanie zdjęć
#dodanie zdjec mieszkań na strone startową
#hashowanie hasła
#dodawanie residents
#usuwanie mieszkania
#update zdjec mieszkań 
#usuwanie mieszkania,konta



class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db_session = Session() ################################# 2 raz
        self.userr_id = None
        self.current_user: Users
        self.loginpage = LoginPage(self)
        self.loginpage.show()
        self.l_photos.setScaledContents(True)
        self.image_paths = []
        self.images = ["C:/Programy/python/projekt/projekt/src/UI/apartment2.jpg",
                       "C:/Programy/python/projekt/projekt/src/UI/apartment.jpg"]
        self.current_image_index = 0
        self.current_image_index2 = 0
        self.show_image(self.images[self.current_image_index])
        self.stackedWidget.setCurrentWidget(self.page_3)


        

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.next_image)
        self.timer.start(5000)

        self.bt_right.clicked.connect(self.next_image)
        self.bt_left.clicked.connect(self.previous_image)
        
        self.bt_mieszkania.clicked.connect(self.show_page2)

        self.bt_konto.clicked.connect(self.show_page)
        self.bt_edytuj.clicked.connect(self.save_changes)
        self.bt_wyloguj.clicked.connect(self.log_out)
        self.bt_kontouploadphoto.clicked.connect(self.upload_photo)

        self.bt_zapisz_dane.clicked.connect(self.dodaj_mieszkanie)
        self.bt_cofnij.clicked.connect(self.show_page2)
        #self.bt_resident_add_photos.clicked.connect(self.show_page5)
        #self.bt_dodaj_najemcow.clicked.connect(self.show_page6)
        self.bt_resident_wroc.clicked.connect(self.show_page4)
        self.bt_listamieszkan_wroc.clicked.connect(self.show_page4)
        self.bt_nastepna_strona.clicked.connect(self.show_page7)
        self.bt_right_add.clicked.connect(self.next_image2)
        self.bt_left_add.clicked.connect(self.previous_image2)



        #kursor na reke
        self.l_plus.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.l_plus.mousePressEvent = self.on_l_plus_clicked

        self.l_plik.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.l_plik.mousePressEvent = self.on_l_plik_clicked

        self.l_photos_add.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.l_photos_add.mousePressEvent = self.on_l_plus_add



    ########################################################################################################
    ## dodanie nowego mieszkania
    ########################################################################################################



    def upload_photos(self):
       file_paths, _ = QFileDialog.getOpenFileNames(self, "Wybierz zdjęcia", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        
       if file_paths:
            
            normalized_paths = [os.path.normpath(path) for path in file_paths]
        
            # Dodanie nowych zdjęć do listy
            self.image_paths.extend(normalized_paths)
            self.show_image2(self.image_paths)

            print(self.image_paths)

    def show_image2(self, image_paths):
        if image_paths:

            image_path = image_paths[self.current_image_index2]
            
            print(image_path)
            if os.path.exists(image_path):
                image = QImage(image_path)
                pixmap = QPixmap(image)
                self.l_photos_add.setPixmap(pixmap)
                self.l_photos_add.setScaledContents(True)
            else:
                print(f"Plik {image_path} nie istnieje")

    def next_image2(self):
        if len(self.image_paths) == 0:
            print("Brak zdjęć do wyświetlenia!")
            return
        self.current_image_index2 = (self.current_image_index2 + 1) % len(self.image_paths)
        self.show_image2(self.image_paths)

    def previous_image2(self):
        if len(self.image_paths) == 0:
            print("Brak zdjęć do wyświetlenia!")
            return
        self.current_image_index2 = (self.current_image_index2 - 1) % len(self.image_paths)
        self.show_image2(self.image_paths)

    def dodaj_mieszkanie(self):
        if not all([self.le_miasto, self.le_ulica, self.le_adres_pocz, self.le_numer_budy, self.le_numer_lok, self.le_metraz, self.le_ilosc_pokoi
                    , self.le_wlasciciel, self.le_stan, self.cb_osoba_wc, self.le_cena]):
            print("Wszystkie pola muszą być wypełnione dotyczące mieszkania!")
            return

        try:
            new_apartment = Apartments(user_id = self.userr_id)

        
            new_info = Info(
                apartment=new_apartment,  # Przypisanie mieszkania
                miasto=self.le_miasto.text(),
                ulica=self.le_ulica.text(),
                adres_pocztowy=self.le_adres_pocz.text(),
                numer_budynku=int(self.le_numer_budy.text()),
                numer_lokalu=int(self.le_numer_lok.text()) if self.le_numer_lok.text() else None,
                metraz=int(self.le_metraz.text()),
                pokoje=int(self.le_ilosc_pokoi.text()),
                wlasciciel=self.le_wlasciciel.text(),
                stan=self.le_stan.text() if self.le_stan.text() else None,
                wc_osobno= True if self.cb_osoba_wc.currentText() == "tak" else False,
                cena_wynajmu=int(self.le_cena.text())
        )
            self.db_session.add(new_apartment)
            self.db_session.add(new_info)

            # Zapisanie zmian w bazie danych
            self.db_session.commit()
            print("Mieszkanie zostało pomyślnie dodane do bazy danych.")

        except Exception as e:
            # Obsługa błędów i wycofanie transakcji
            self.db_session.rollback()
            print(f"Wystąpił błąd podczas dodawania mieszkania: {e}")
        
        if len(self.image_paths) == 0:
            print("zostanie dodany defaultowy obrazek")
            self.photo_b64 = None

            try:
                new_photo = Photos(
                    apartment = new_apartment,
                    photo_b64 = self.photo_b64
                )
                self.db_session.add(new_photo)

                self.db_session.commit()
                print("zdjecie zostalo dodane pomyslnie")

            except Exception as e:
                self.db_session.rollback()
                print(f"nie zostalo dodane zdjecie: {e}")

        else:
            for i in self.image_paths:
                with open(i, "rb") as file:
                    image_data = file.read()
                    self.photo_b64 = base64.b64encode(image_data).decode('utf-8')  # Przechowaj w base64

                try:
                    new_photo = Photos(
                        apartment = new_apartment,
                        photo_b64 = self.photo_b64
                    )

                    self.db_session.add(new_photo)

                    self.db_session.commit()
                    print("zdjecie zostalo dodane pomyslnie")

                except Exception as e:
                    self.db_session.rollback()
                    print(f"cos poszlo nei tak przy dodawaniu zdjecia: {e}")


        

    def on_l_plus_clicked(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.show_page4()

    def on_l_plik_clicked(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.show_page5()

    def on_l_plus_add(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.upload_photos()
            
            

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
        path_plus = "C:/Programy/python/projekt/projekt/src/UI/plus.jpg"
        if os.path.exists(path_plus):
            image = QImage(path_plus)
            pixmap = QPixmap(image)
            self.l_plus.setPixmap(pixmap)
            self.l_plus.setScaledContents(True)

        path_plik = "C:/Programy/python/projekt/projekt/src/UI/folder.jpg"
        if os.path.exists(path_plik):
            image = QImage(path_plik)
            pixmap = QPixmap(image)
            self.l_plik.setPixmap(pixmap)
            self.l_plik.setScaledContents(True)

    def show_page4(self):
        self.stackedWidget.setCurrentWidget(self.page_4)

    def show_page5(self):
        self.stackedWidget.setCurrentWidget(self.page_5)    

    def show_page6(self):
        self.stackedWidget.setCurrentWidget(self.page_6) 

    def show_page7(self):
        self.stackedWidget.setCurrentWidget(self.page_7)

    def show_page(self):
        self.stackedWidget.setCurrentWidget(self.page)
        self.le_kontouser.setText(self.current_user.username)
        self.le_kontofirstname.setText(self.current_user.firstname)
        self.le_kontosurname.setText(self.current_user.surname)
        self.le_kontoemail.setText(self.current_user.email)
        self.le_kontophone.setText(self.current_user.phone)
        self.le_kontopassword.setText(self.current_user.password_hashed)
        encoded_image_data = self.current_user.profile_b64 if self.current_user.profile_b64 else None

        if encoded_image_data:
            image_data = base64.b64decode(encoded_image_data)
            image = QPixmap()
            image.loadFromData(QByteArray(image_data), format="JPG")

            self.l_kontophoto.setPixmap(image)
            self.l_kontophoto.setScaledContents(True)
        else:
            image = QImage("C:/Programy/python/projekt//projekt/src/UI/user.jpg")
            pixmap = QPixmap(image)
            self.l_kontophoto.setPixmap(pixmap)
            self.l_kontophoto.setScaledContents(True)

    def upload_photo(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Wybierz zdjecie profilowe", "", "Images (*.png *.jpg *.jpeg *.bmp)")

        if file_path:
            pixmap = QPixmap(file_path)
            self.l_kontophoto.setPixmap(pixmap)
            self.l_kontophoto.setScaledContents(True)
            
            with open(file_path, "rb") as file:
                image_data = file.read()
                self.profile_b64 = base64.b64encode(image_data).decode('utf-8')
        
    def save_changes(self):
        
        image_changed = self.profile_b64 != self.current_user.profile_b64

        updated_data = {
            "username": self.le_kontouser.text(),
            "firstname": self.le_kontofirstname.text(),
            "surname": self.le_kontosurname.text(),
            "email": self.le_kontoemail.text(),
            "phone": self.le_kontophone.text() 
        }

        self.original_data = {
                "username": self.current_user.username,
                "firstname": self.current_user.firstname,
                "surname": self.current_user.surname,
                "email": self.current_user.email,
                "phone": self.current_user.phone,
            }
        
        changed_fields = {
            key: value for key, value in updated_data.items() if value != self.original_data.get(key)
        }

        if image_changed:
            changed_fields["profile_b64"] = self.profile_b64

        if changed_fields:
            try:
                for field, new_value in changed_fields.items():
                    setattr(self.current_user, field, new_value)
                self.db_session.commit()
                print("zmiany zostały zapisane")
            except Exception as e:
                self.db_session.rollback()
                print(f"Błąd podczas zapisywania zmian: {e}")
        else:
            print("Brak zmian do zapsiania")

    def log_out(self):

        
        self.hide()

        
        #wszystkie le
        self.le_kontouser.setText("")
        self.le_kontofirstname.setText("")
        self.le_kontosurname.setText("")
        self.le_kontoemail.setText("")
        self.le_kontophone.setText("")
        self.le_kontopassword.setText("")
        # or self.profile_b64 tuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu
        if (self.current_user.profile_b64):
            image = QImage("C:/Programy/python/projekt//projekt/src/UI/user.jpg")
            pixmap = QPixmap(image)
            self.l_kontophoto.setPixmap(pixmap)
            self.l_kontophoto.setScaledContents(True)

        #czyszczenie wszystkiego
        self.current_user: Users = None
        

        self.db_session.close()
        self.loginpage.show()


#username = Column(String(50), nullable=False, unique=True)
#    firstname = Column(String(50), nullable=False)
#    surname = Column(String(50), nullable=False)
#    email = Column(String(100), nullable=False, unique=True)
 #   phone = Column(String(100), nullable=False)
 #   password_hashed = Column(String(200), nullable=False)
 #   profile_b64 = Column(String(), nullable=True)





class LoginPage(QWidget, Ui_Form):

    def __init__(self, mainwindow: MainWindow):
        super().__init__()
        self.setupUi(self)
        self.mainwindow = mainwindow
        self.db_session = self.mainwindow.db_session
        
        self.stackedWidget.setCurrentWidget(self.page_2)
        self.bt_login.clicked.connect(self.login)
        self.bt_rejestr.clicked.connect(self.rejestr)
        self.bt_rejestr.setToolTip("juuuuuuhuuu")
        self.bt_ok.clicked.connect(self.test)
        self.bt_regpath.clicked.connect(self.upload_photo)


    def login(self):
        username = self.le_login.text()
        password = self.le_haslo.text()

        #db_session = Session()
        try:
            
            current_user = self.db_session.query(Users).filter_by(username=username).first()
            
            if current_user:
                if current_user.password_hashed == password:
                    print("zalogowano pomyślnie")
                    self.mainwindow.userr_id = current_user.user_id
                    self.le_login.setText("")
                    self.le_haslo.setText("")
                    self.hide()
                    self.mainwindow.current_user = current_user
                    print(self.mainwindow.current_user)
                    print(type(self.mainwindow.current_user))
                    print(self.mainwindow.userr_id)
                    self.mainwindow.stackedWidget.setCurrentWidget(self.mainwindow.page_3)
                    self.mainwindow.show()
                else:
                    print("błędne hasło")
                    
            else:
                print("Użytkownik nie istnieje")
        except Exception as e:
            print(f"wystapil blad podczas logowania: {e}")
            self.db_session.close()
        
            
        
        

    def rejestr(self):
        self.stackedWidget.setCurrentWidget(self.page)
        
    def upload_photo(self):

        file_path, _ = QFileDialog.getOpenFileName(self, "Wybierz zdjecie profilowe", "", "Images (*.png *.jpg *.jpeg *.bmp)")

        if file_path:
            pixmap = QPixmap(file_path)
            self.l_regphoto.setPixmap(pixmap)
            self.l_regphoto.setScaledContents(True)
            
            with open(file_path, "rb") as file:
                image_data = file.read()
                self.profile_b64 = base64.b64encode(image_data).decode('utf-8')  # Przechowaj w base64


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
        new_user.profile_b64 = self.profile_b64 if self.profile_b64 else None
        
        
        
        try:
            self.db_session.add(new_user)
            self.db_session.commit()
            print("Użytkownik został pomyślnie dodany do bazy danych.")
        except Exception as e:
            self.db_session.rollback()
            print(f"Wystąpił błąd podczas dodawania użytkowania: {e}")
            self.db_session.close()    
        
        self.hide()
        self.stackedWidget.setCurrentWidget(self.mainwindow.page_3)
        self.mainwindow.show()
        

        



if __name__ == "__main__":
    app = QApplication()
    widget = MainWindow()
    
    
    app.exec()


