import sqlite3
from PyQt5 import QtWidgets
from home import HomeWindow
from app_state import AppState

class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Yumtrek Login')
        self.setGeometry(0, 0, 600, 400)

        layout = QtWidgets.QVBoxLayout()

        self.username_input = QtWidgets.QLineEdit(self)
        self.username_input.setPlaceholderText('Username')
        self.username_input.setFixedHeight(50)

        self.password_input = QtWidgets.QLineEdit(self)
        self.password_input.setPlaceholderText('Password')
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setFixedHeight(50)

        self.login_button = QtWidgets.QPushButton('Login', self)
        self.login_button.setFixedHeight(60)
        self.login_button.setStyleSheet("font-size: 18px")
        self.login_button.clicked.connect(self.check_login)

        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        connection = sqlite3.connect('yumtrek.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        connection.close()

        if user:
            AppState.set_current_user(user)  # Salva l'utente connesso nello stato globale
            role = user[3]
            self.open_home_window(role)
        else:
            QtWidgets.QMessageBox.warning(self, 'Errore', 'Username o password errati')

    def open_home_window(self, role):
        self.home_window = HomeWindow(role)
        self.home_window.show()
        self.close()
