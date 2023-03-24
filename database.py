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