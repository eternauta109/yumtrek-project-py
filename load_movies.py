import pandas as pd
from PyQt5 import QtWidgets, QtCore
from app_state import AppState

class LoadMoviesWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Carica Film')
        self.setGeometry(0, 0, 600, 400)

        layout = QtWidgets.QVBoxLayout()

        # Pulsante per caricare il file
        self.load_file_button = QtWidgets.QPushButton('Carica File Excel', self)
        self.load_file_button.setFixedHeight(60)
        self.load_file_button.setStyleSheet("font-size: 18px")
        self.load_file_button.clicked.connect(self.load_excel_file)

        # Aggiungi pulsante al layout
        layout.addWidget(self.load_file_button)

        self.setLayout(layout)

    def load_excel_file(self):
        options = QtWidgets.QFileDialog.Options()
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Seleziona il file Excel", "", "Excel Files (*.xlsx; *.xls);;All Files (*)", options=options)
        
        if file_name:
            try:
                # Carica il file Excel in un DataFrame Pandas
                df = pd.read_excel(file_name)

                # Salva i dati nel AppState per renderli disponibili nell'app
                AppState.set_movies_data(df)
                
                # Apri la finestra per selezionare i film
                self.select_movies_window = SelectMoviesWindow(df)
                self.select_movies_window.show()
                
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, 'Errore', f'Errore durante il caricamento del file: {e}')

class SelectMoviesWindow(QtWidgets.QWidget):
    def __init__(self, movies_df):
        super().__init__()
        self.movies_df = movies_df
        self.selected_movies = []
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Seleziona i Film per la Vendita')
        self.setGeometry(0, 0, 800, 600)

        layout = QtWidgets.QVBoxLayout()

        # Creare la lista di checkbox per ogni film
        self.checkboxes = []
        for index, row in self.movies_df.iterrows():
            checkbox = QtWidgets.QCheckBox(f"{row['AUDITORIUM']} - {row['PLAYLIST']}", self)
            self.checkboxes.append(checkbox)
            layout.addWidget(checkbox)

        # Pulsante per selezionare tutti i film
        self.select_all_button = QtWidgets.QPushButton('Seleziona Tutti', self)
        self.select_all_button.clicked.connect(self.select_all)

        # Pulsante per salvare la selezione
        self.save_selection_button = QtWidgets.QPushButton('Salva Selezione', self)
        self.save_selection_button.clicked.connect(self.save_selection)

        # Aggiungi i pulsanti al layout
        layout.addWidget(self.select_all_button)
        layout.addWidget(self.save_selection_button)

        self.setLayout(layout)

    def select_all(self):
        # Seleziona tutti i checkbox
        for checkbox in self.checkboxes:
            checkbox.setChecked(True)

    def save_selection(self):
        # Salva i film selezionati
        self.selected_movies = [row for i, row in self.movies_df.iterrows() if self.checkboxes[i].isChecked()]
        AppState.set_selected_movies(self.selected_movies)

        QtWidgets.QMessageBox.information(self, 'Successo', 'Selezione salvata con successo!')
        self.close()
