"""
SQLite Database Manager
Project PEGASUS
"""

import sqlite3


class Database:

    def __init__(self):

        self.connection = sqlite3.connect("data/memory.db")
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS memories(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            key TEXT UNIQUE,

            value TEXT

        )

        """)

        self.connection.commit()

    def save_memory(self, key, value):

        self.cursor.execute("""

        INSERT OR REPLACE INTO memories(key, value)

        VALUES(?,?)

        """, (key, value))

        self.connection.commit()

    def get_memory(self, key):

        self.cursor.execute("""

        SELECT value FROM memories

        WHERE key = ?

        """, (key,))

        result = self.cursor.fetchone()

        return result