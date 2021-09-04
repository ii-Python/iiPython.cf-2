# Copyright 2021 iiPython

# Modules
import os
import sqlite3
from typing import Union
from sqlite3.dbapi2 import Cursor, Row

# Database class
class Database(object):
    def __init__(self, path: str) -> None:
        self.path = path
        self.exists = os.path.isfile(self.path)

        # Load DB
        self._load_db()

    def __factory__(self, cursor: Cursor, row: Row) -> dict:
        return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}

    def _load_db(self) -> None:
        self.conn = sqlite3.connect(self.path, check_same_thread = False)
        self.conn.row_factory = self.__factory__
        self.cursor = self.conn.cursor()

    def _save_db(self) -> None:
        self.conn.commit()
        self.conn.close()
        self._load_db()

    def initialize(self, init_command: str) -> None:
        if not self.exists:
            self.cursor.execute(init_command)
            self._save_db()
            self.exists = True

    def get(self, table: str, identifier: tuple) -> Union[dict, None]:
        return self.cursor.execute(f"SELECT * FROM {table} WHERE {identifier[0]}=?", (identifier[1],)).fetchone()

    def add(self, table: str, values: tuple) -> None:
        self.cursor.execute(f"INSERT INTO {table} VALUES ({('?, ' * len(values))[:-2]})", values)
        self._save_db()

# Database loader
class DBLoader(object):
    def __init__(self, db_dir: str) -> None:
        self.db_dir = db_dir
        if not os.path.isdir(self.db_dir):
            os.makedirs(self.db_dir)

        self.db_ext = ".db"

    def load_db(self, db_name: str) -> Database:
        db_path = os.path.join(self.db_dir, db_name + self.db_ext)
        return Database(db_path)
