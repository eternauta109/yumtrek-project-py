import sys
from PyQt5 import QtWidgets
from database.initialize import initialize_db
from database.default_users import add_default_user
from login import LoginWindow
from home import HomeWindow
from user_management import UserManagementWindow


if __name__ == '__main__':
    initialize_db()
    add_default_user()
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet("* { font-size: 18px; }")  # Imposta il font più grande per l'intera applicazione
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())

# Crea un file .gitignore per escludere i file non necessari dalla repository
gitignore_content = '''
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
dist/
*.egg-info/
*.egg

# Installer logs
env/
venv/

# IDE files
.vscode/
.idea/
*.sublime-project
*.sublime-workspace

# SQLite database
yumtrek.db

# Jupyter Notebook checkpoints
.ipynb_checkpoints/
'''

with open('.gitignore', 'w') as f:
    f.write(gitignore_content)