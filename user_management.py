from PyQt5 import QtWidgets, QtCore
import sqlite3
from app_state import AppState

class UserManagementWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Gestione Utenti')
        self.setGeometry(0, 0, 800, 600)

        layout = QtWidgets.QVBoxLayout()

        # Tabella per visualizzare gli utenti
        self.user_table = QtWidgets.QTableWidget(self)
        self.user_table.setColumnCount(5)
        self.user_table.setHorizontalHeaderLabels(['ID', 'Username', 'Password', 'Role', 'Cinema'])
        self.user_table.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.user_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.load_users()

        # Campi di input
        form_layout = QtWidgets.QFormLayout()

        self.username_input = QtWidgets.QLineEdit(self)
        self.password_input = QtWidgets.QLineEdit(self)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.role_input = QtWidgets.QComboBox(self)
        self.role_input.addItems(['manager', 'staff'])

        current_user = AppState.get_current_user()
        self.cinema_input = QtWidgets.QLineEdit(self)
        self.cinema_input.setText(current_user[4])
        self.cinema_input.setReadOnly(True)

        # Pulsanti per aggiungere, modificare e cancellare utenti
        self.add_user_button = QtWidgets.QPushButton('Aggiungi Utente', self)
        self.update_user_button = QtWidgets.QPushButton('Modifica Utente', self)
        self.delete_user_button = QtWidgets.QPushButton('Elimina Utente', self)

        self.add_user_button.clicked.connect(self.add_user)
        self.update_user_button.clicked.connect(self.update_user)
        self.delete_user_button.clicked.connect(self.delete_user)

        # Layout
        layout.addWidget(self.user_table)
        form_layout.addRow('Username:', self.username_input)
        form_layout.addRow('Password:', self.password_input)
        form_layout.addRow('Ruolo:', self.role_input)
        form_layout.addRow('Cinema:', self.cinema_input)
        layout.addLayout(form_layout)

        layout.addWidget(self.add_user_button)
        layout.addWidget(self.update_user_button)
        layout.addWidget(self.delete_user_button)

        self.setLayout(layout)

    def load_users(self):
        # Carica gli utenti dal database nella tabella
        connection = sqlite3.connect('yumtrek.db')
        cursor = connection.cursor()
        cursor.execute("SELECT id, username, password, role, cinema FROM users")
        users = cursor.fetchall()
        connection.close()

        self.user_table.setRowCount(0)
        for row_number, user in enumerate(users):
            self.user_table.insertRow(row_number)
            for column_number, data in enumerate(user):
                self.user_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def add_user(self):
        username = self.username_input.text()
        password = self.password_input.text()
        role = self.role_input.currentText()
        cinema = self.cinema_input.text()

        connection = sqlite3.connect('yumtrek.db')
        cursor = connection.cursor()
        try:
            cursor.execute('INSERT INTO users (username, password, role, cinema) VALUES (?, ?, ?, ?)',
                           (username, password, role, cinema))
            connection.commit()
            QtWidgets.QMessageBox.information(self, 'Successo', 'Utente aggiunto con successo!')
            self.load_users()  # Ricarica la tabella utenti
        except sqlite3.IntegrityError:
            QtWidgets.QMessageBox.warning(self, 'Errore', 'L\'utente esiste già!')
        finally:
            connection.close()

    def update_user(self):
        selected_row = self.user_table.currentRow()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self, 'Errore', 'Seleziona un utente da modificare.')
            return

        user_id = int(self.user_table.item(selected_row, 0).text())
        username = self.username_input.text()
        password = self.password_input.text()
        role = self.role_input.currentText()
        cinema = self.cinema_input.text()

        connection = sqlite3.connect('yumtrek.db')
        cursor = connection.cursor()
        try:
            cursor.execute('UPDATE users SET username=?, password=?, role=?, cinema=? WHERE id=?',
                           (username, password, role, cinema, user_id))
            connection.commit()
            QtWidgets.QMessageBox.information(self, 'Successo', 'Utente modificato con successo!')
            self.load_users()  # Ricarica la tabella utenti
        finally:
            connection.close()

    def delete_user(self):
        selected_row = self.user_table.currentRow()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self, 'Errore', 'Seleziona un utente da eliminare.')
            return

        user_id = int(self.user_table.item(selected_row, 0).text())

        connection = sqlite3.connect('yumtrek.db')
        cursor = connection.cursor()
        try:
            cursor.execute('DELETE FROM users WHERE id=?', (user_id,))
            connection.commit()
            QtWidgets.QMessageBox.information(self, 'Successo', 'Utente eliminato con successo!')
            self.load_users()  # Ricarica la tabella utenti
        finally:
            connection.close()
