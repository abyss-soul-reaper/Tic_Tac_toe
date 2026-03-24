import sqlite3

class BaseDataManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.conn = None
        self.connect()

    def connect(self):
        self.conn = sqlite3.connect(self.file_path)

    def execute(self, query, params=None):
        cur = self.conn.cursor()
        if params is not None:
            cur.execute(query, params)
        else:
            cur.execute(query)
        return cur

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()
