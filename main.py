from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from src.UI.templates.LogInPage import Ui_Form
from src.UI.templates.MainWindow import Ui_MainWindow


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



if __name__ == "__main__":
    app = QApplication()
    widget = MainWindow()
    
    
    app.exec()


