from PyQt5 import QtWidgets

class ManagerWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Yumtrek Manager Panel')
        self.setGeometry(100, 100, 500, 400)
        # TODO: Add functionality for adding products and users
