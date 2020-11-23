import sqlite3
import os
from datetime import datetime

db_filename = 'todo.db'


class Schema:
    def __init__(self, db_filename=db_filename):
        self._db_filename = db_filename

        self._conn = sqlite3.connect(db_filename)

        self._todo = self._create_todo_table()
        self._user = self._create_user_table()

    def __del__(self):
        self._conn.commit()
        self._conn.close()

    def _create_todo_table(self):
        query = """
            create table if not exists "Todo" (
                _id          integer primary key autoincrement,
                title        text not null,
                description  text,
                due          date not null,
                created      date default current_date,
                user         text foreignkey references User(name)
            );
        """
        self._conn.execute(query)

    def _create_user_table(self):
        query = """
            create table if not exists "User" (
                name         text primary key,
                email        text,
                phone        text,
                created      date default current_date
            );
        """

        self._conn.execute(query)
