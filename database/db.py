import sqlite3
import os

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Database:
    def __init__(self, db_name):
        self.db_name = db_name+'.db'
        self.db_path = os.path.join(path, self.db_name)
        self.databaseInitial()

    def databaseInitial(self):
        if not os.path.exists(self.db_path):
            conn = sqlite3.connect(self.db_path)
            cur = conn.cursor()
            cur.execute('''CREATE TABLE messages
                          (ID INTEGER PRIMARY KEY autoincrement ,
                          USER TEXT NOT NULL ,
                          CONTENT TEXT NOT NULL ,
                          TIMESTAMP TimeStamp NOT NULL DEFAULT (datetime('now','localtime')))''')
            cur.execute('''
                      CREATE TABLE friends
                      (ID INTEGER PRIMARY KEY AUTOINCREMENT ,
                      USER TEXT NOT NULL )''')
            conn.commit()
            conn.close()

    def fetchMessage(self, user):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        result = cur.execute("select user, content, timestamp from messages where user='{0}'".format(user)).fetchall()
        cur.close()
        conn.close()
        return result

    def fetchFriend(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        result = cur.execute("select user from friends").fetchall()
        cur.close()
        conn.close()
        return result

    def insertMessage(self, user, content):
        conn_local = sqlite3.connect(self.db_path)
        cur = conn_local.cursor()
        cur.execute("insert into messages(USER, CONTENT) VALUES ('{0}', '{1}');".format(user, content))
        conn_local.commit()
        cur.close()
        conn_local.close()
        return None

    def addFriend(self, user):
        conn_local = sqlite3.connect(self.db_path)
        cur = conn_local.cursor()
        cur.execute("insert into friends(USER) VALUES ('{0}');".format(user))
        conn_local.commit()
        cur.close()
        conn_local.close()
        return None

