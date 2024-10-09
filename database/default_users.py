import sqlite3

def add_default_user():
    connection = sqlite3.connect('yumtrek.db')
    cursor = connection.cursor()

    # Add default users
    default_users = [
        ('fabioc', '109', 'manager', 'guidonia'),       
    ]

    for username, password, role, cinema in default_users:
        try:
            cursor.execute('INSERT INTO users (username, password, role, cinema) VALUES (?, ?, ?, ?)', (username, password, role, cinema))
        except sqlite3.IntegrityError:
            # User already exists
            pass

    connection.commit()
    connection.close()
