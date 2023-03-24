import datetime
import sqlite3 as sql


class MainDB:
    def __init__(self):
        self.con = sql.connect('data.db')
        self.cur = self.con.cursor()

    def create_table(self):
        with self.con:
            self.cur.execute('''CREATE TABLE IF NOT EXISTS users(
            user_id INT PRIMARY KEY,
            username VARCHAR(100),
            date VARCHAR(30)
            )''')

            self.cur.execute('''CREATE TABLE IF NOT EXISTS effects(
                        effect_name VARCHAR(50),
                        effect VARCHAR(50)
                        )''')

    def add_user(self, user_id: int, username: str):
        today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        with self.con:
            self.cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
            if user is None:
                self.cur.execute("INSERT INTO users (user_id, username, date) VALUES (?, ?, ?)",
                                 (user_id, username, today))
