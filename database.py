import sqlite3
import datetime


class MainDB():
    def __init__(self):
        self.con = sqlite3.connect('files.db')
        self.cur = self.con.cursor()

    def create_table(self):
        with self.con:
            self.con.cursor()
            self.cur.execute('''CREATE TABLE IF NOT EXISTS files
                       (id INTEGER PRIMARY KEY,
                        user_id INTEGER NOT NULL,
                        file_id TEXT NOT NULL,
                        file_type TEXT NOT NULL,
                        date TIMESTAMP)''')

    def insert_photo(self, user, photo):
        with self.con:
            self.con.cursor()
            self.cur.execute("INSERT INTO files (user_id, file_id, file_type, date) VALUES (?, ?, ?, DATETIME('now'))",
                             (user, photo, 'photo'))

    def insert_audio(self, user, audio):
        with self.con:
            self.con.cursor()
            self.cur.execute("INSERT INTO files (user_id, file_id, file_type, date) VALUES (?, ?, ?, DATETIME('now'))",
                             (user, audio, 'audio'))

    def select_data(self, user):
        with self.con:
            self.con.cursor()
            self.cur.execute("SELECT file_id, file_type FROM files WHERE user_id = ?", (user))
