# Обработчик sql запросов (sql handler's requests)
import sqlite3

class SqlH():
    def __init__(self):
        self.conn = sqlite3.connect('settings.db')
        self.cur = self.conn.cursor()

    def add_token(self, token, name):
        pass