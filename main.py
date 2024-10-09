import sys
from PyQt5 import QtWidgets
from database.initialize import initialize_db
from database.default_users import add_default_user
from login import LoginWindow
from home import HomeWindow
from user_management import UserManagementWindow
from load_movies import LoadMoviesWindow, SelectMoviesWindow

if __name__ == '__main__':
    initialize_db()
    add_default_user()
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet("* { font-size: 18px; }")  # Imposta il font più grande per l'intera applicazione
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())