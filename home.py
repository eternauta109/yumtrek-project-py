from PyQt5 import QtWidgets
from user_management import UserManagementWindow
from load_movies import LoadMoviesWindow

class HomeWindow(QtWidgets.QWidget):
    def __init__(self, role):
        super().__init__()
        self.role = role
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Yumtrek Home')
        self.setGeometry(0, 0, 800, 600)

        layout = QtWidgets.QVBoxLayout()

        # Pulsanti per le varie funzioni
        self.load_movies_button = QtWidgets.QPushButton('Carica Film', self)
        self.load_movies_button.setFixedHeight(70)
        self.load_movies_button.setStyleSheet("font-size: 18px")
        self.load_movies_button.clicked.connect(self.open_load_movies)

        self.load_yumtrek_button = QtWidgets.QPushButton('Carica Yumtrek', self)
        self.load_yumtrek_button.setFixedHeight(70)
        self.load_yumtrek_button.setStyleSheet("font-size: 18px")

        self.cash_register_button = QtWidgets.QPushButton('Cassa', self)
        self.cash_register_button.setFixedHeight(70)
        self.cash_register_button.setStyleSheet("font-size: 18px")

        layout.addWidget(self.load_movies_button)
        layout.addWidget(self.load_yumtrek_button)
        layout.addWidget(self.cash_register_button)

        # Pulsanti specifici per i manager
        if self.role == 'manager':
            self.add_user_button = QtWidgets.QPushButton('Aggiungi User', self)
            self.add_user_button.setFixedHeight(70)
            self.add_user_button.setStyleSheet("font-size: 18px")
            self.add_user_button.clicked.connect(self.open_user_management)

            self.add_product_button = QtWidgets.QPushButton('Aggiungi Prodotto', self)
            self.add_product_button.setFixedHeight(70)
            self.add_product_button.setStyleSheet("font-size: 18px")

            self.close_register_button = QtWidgets.QPushButton('Chiudi Cassa', self)
            self.close_register_button.setFixedHeight(70)
            self.close_register_button.setStyleSheet("font-size: 18px")

            layout.addWidget(self.add_user_button)
            layout.addWidget(self.add_product_button)
            layout.addWidget(self.close_register_button)

        self.setLayout(layout)

    def open_load_movies(self):
        self.load_movies_window = LoadMoviesWindow()
        self.load_movies_window.show()

    def open_user_management(self):
        self.user_management_window = UserManagementWindow()
        self.user_management_window.show()