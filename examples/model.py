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


class Todo:
    tablename = "Todo"
    
    def __init__(self, db_filename=db_filename):
        self._db_filename = db_filename
        assert os.path.isfile(self._db_filename)

        try:
            self._conn = sqlite3.connect(db_filename)

        except Exception as e:
            print(e)

    def __del__(self):
        self._conn.commit()
        self._conn.close()

    def create(self, user, title, description, due="2020-12-31 11:59:59"):
        created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query   = (
            f'insert into {Todo.tablename} '
            f'(user, title, description, due, created) values '
            f'("{user}", "{title}", "{description}", "{due}", "{created}");'
        )
        self._conn.execute(query)
        self._conn.commit()

    def select(self, *args):
        assert all(map(lambda arg: isinstance(arg, str), args))
        fields = ', '.join(args)

        query  = f'select {fields} from {Todo.tablename} order by _id;'
        self._conn.execute(query).fetchall()

    def purge(self):
        query  = f'delete from {Todo.tablename};'
        self._conn.execute(query)

    def delete(self, id):
        query  = f'delete from {Todo.tablename} where _id={id};'
        self._conn.execute(query)
        self._conn.commit()

    def update_title(self, _id, title):
        sql = (
            f'update {Todo.tablename} '
            f'set title="{title}" '
            f'where _id="{_id}";'
        )

        self._conn.execute(sql)
        self._conn.commit()

    def update_description(self, _id, description):
        sql = (
            f'update {Todo.tablename} '
            f'set description="{description}" '
            f'where _id="{_id}";'
        )

        self._conn.execute(sql)
        self._conn.commit()

    def show(self):
        query  = f'select * from {Todo.tablename} order by _id;'
        result  = self._conn.execute(query)
        fetched = result.fetchall()
        colnames = [rec[0] for rec in result.description]

        return [
            {col: record[i] for i, col in enumerate(colnames)}
            for record in fetched
        ]

