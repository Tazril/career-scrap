import sqlite3

from base.db import PostingDatabase


class SQLPostingDatabase(PostingDatabase):
    name = 'data/careers.db'

    def __init__(self):
        self.conn = sqlite3.connect(self.name, check_same_thread=False)
        self.create_table()

    def create_table(self):
        try:
            table = ''' CREATE TABLE IF NOT EXISTS posting (
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         title TEXT    NOT NULL,
                         location TEXT     NOT NULL,
                         url TEXT NOT NULL,
                         company TEXT NOT NULL,
                         created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                     );'''
            self.conn.execute(table)
            self.conn.commit()
        except Exception as e:
            print('Create Table Exception: ' + str(e))

    def insert(self, name, location, url, company):
        try:
            query = '''INSERT INTO posting (title, location, url, company) 
                   VALUES (?, ?, ?, ?)'''
            self.conn.execute(query, (name, location, url, company))
            self.conn.commit()
        except Exception as e:
            print('Insert Exception: ' + str(e))

    def get_all(self):
        try:
            cursor = self.conn.cursor()
            query = '''SELECT * FROM POSTING'''
            cursor.execute(query)
            data = []
            for row in cursor.fetchall():
                data.append({})
                data[-1]['title'] = row[1]
                data[-1]['location'] = row[2]
                data[-1]['url'] = row[3]
                data[-1]['company'] = row[4]
                data[-1]['created_at'] = row[5]
            return data
        except Exception as e:
            print('Get All Exception: ' + str(e))

    def get_company_list(self):
        try:
            cursor = self.conn.cursor()
            query = '''SELECT DISTINCT company FROM POSTING'''
            cursor.execute(query)
            return [row[0] for row in cursor.fetchall()]
        except Exception as e:
            print('Get All Exception: ' + str(e))

    def get_by_company(self, company):
        try:
            cursor = self.conn.cursor()
            query = '''SELECT * FROM POSTING where company = ?'''
            cursor.execute(query, [company])
            return cursor.fetchall()
        except Exception as e:
            print('Get By Company Exception: ' + str(e))

    def remove_by_company(self, company):
        try:
            cursor = self.conn.cursor()
            query = '''DELETE FROM POSTING where company = ?'''
            cursor.execute(query, [company])
            return cursor.fetchall()
        except Exception as e:
            print('Remove By Company Exception: ' + str(e))

    def get_count(self):
        try:
            cursor = self.conn.cursor()
            query = '''SELECT COUNT(*) FROM POSTING'''
            cursor.execute(query)
            return cursor.fetchone()[0]
        except Exception as e:
            print('Remove By Company Exception: ' + str(e))

    def search(self, text):
        try:
            cursor = self.conn.cursor()
            query = '''SELECT * FROM POSTING WHERE title like ? or location like ? or company like ?'''
            cursor.execute(query, ('%' + text + '%', '%' + text + '%', '%' + text + '%'))
            data = []
            for row in cursor.fetchall():
                data.append({})
                data[-1]['title'] = row[1]
                data[-1]['location'] = row[2]
                data[-1]['url'] = row[3]
                data[-1]['company'] = row[4]
                data[-1]['created_at'] = row[5]
            return data
        except Exception as e:
            print('Get All Exception: ' + str(e))
