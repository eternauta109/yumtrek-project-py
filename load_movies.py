import pandas as pd
from PyQt5 import QtWidgets, QtCore
from app_state import AppState
from datetime import timedelta

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

        # Layout principale con scroll
        scroll_area = QtWidgets.QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_content = QtWidgets.QWidget()
        scroll_layout = QtWidgets.QVBoxLayout(scroll_content)

        # Creare la lista di checkbox per ogni film
        self.checkboxes = []
        for index, row in self.movies_df.iterrows():
            # Calcolare FEATURE_TIME meno 10 minuti
            feature_time = pd.to_datetime(row['FEATURE_TIME']) - timedelta(minutes=10)
            checkbox_text = f"{row['AUDITORIUM']} - {row['PLAYLIST']} - Inizio intervallo: {feature_time.strftime('%Y-%m-%d %H:%M:%S')}"
            checkbox = QtWidgets.QCheckBox(checkbox_text, self)
            self.checkboxes.append(checkbox)
            scroll_layout.addWidget(checkbox)

        # Imposta il contenuto scrollabile
        scroll_area.setWidget(scroll_content)

        # Layout principale
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(scroll_area)

        # Pulsante per selezionare tutti i film
        self.select_all_button = QtWidgets.QPushButton('Seleziona Tutti', self)
        self.select_all_button.clicked.connect(self.select_all)

        # Pulsante per salvare la selezione
        self.save_selection_button = QtWidgets.QPushButton('Salva Selezione', self)
        self.save_selection_button.clicked.connect(self.save_selection)

        # Aggiungi i pulsanti al layout principale (fuori dallo scroll)
        main_layout.addWidget(self.select_all_button)
        main_layout.addWidget(self.save_selection_button)

        self.setLayout(main_layout)

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
