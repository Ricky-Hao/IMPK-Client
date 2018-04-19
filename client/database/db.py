import sqlite3
import os
from ..core.logger import logging

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Database:
    def __init__(self, db_name):
        self.db_name = db_name+'.db'
        self.db_path = os.path.join(path, self.db_name)
        self.log = logging.getLogger('Database')
        self.databaseInitial()

    def databaseInitial(self):
        if not os.path.exists(self.db_path):
            conn = sqlite3.connect(self.db_path)
            cur = conn.cursor()
            cur.execute('''CREATE TABLE messages
                          (ID INTEGER PRIMARY KEY autoincrement ,
                          USERNAME TEXT NOT NULL ,
                          CONTENT TEXT NOT NULL ,
                          SENDER TEXT NOT NULL ,
                          TIMESTAMP TimeStamp NOT NULL DEFAULT (datetime('now','localtime')))''')
            cur.execute('''
                      CREATE TABLE friends
                      (ID INTEGER PRIMARY KEY AUTOINCREMENT ,
                      USERNAME TEXT NOT NULL )''')
            conn.commit()
            conn.close()

    def quote(self, data_list):
        for i in range(len(data_list)):
            data_list[i] = "'{0}'".format(data_list[i])
        return ", ".join(data_list)

    def and_where(self, data_dict):
        temp_list = []
        for key in data_dict.keys():
            temp_list.append("{0}='{1}'".format(key, data_dict[key]))

        if len(temp_list) == 1:
            return temp_list[0]
        else:
            return ' and '.join(temp_list)

    def deleteOne(self, table, where='1=1'):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        result = cur.execute('delete from {0} where {1}'.format(table, where))
        cur.close()
        conn.commit()
        conn.close()
        return result

    def fetchOne(self, column, table, where='1=1'):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        result = cur.execute("select {0} from {1} where {2}".format(column, table, where)).fetchone()
        cur.close()
        conn.close()
        return result

    def fetchAll(self, column, table, where='1=1'):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        result = cur.execute("select {0} from {1} where {2}".format(column, table, where)).fetchall()
        cur.close()
        conn.close()
        return result

    def insertOne(self, table, field_list, value_list):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        result = cur.execute("insert into {0}({1}) values({2})".format(table, field_list, self.quote(value_list)))
        self.log.debug("insert into {0}({1}) values({2})".format(table, field_list, self.quote(value_list)))
        cur.close()
        conn.commit()
        conn.close()
        return result

    def fetchMessage(self, user):
        return self.fetchAll('sender, content, timestamp', 'messages', self.and_where({'username':user}))

    def fetchFriend(self):
        return self.fetchAll('username', 'friends')

    def insertMessage(self, user, content, sender):
        return self.insertOne('messages', 'USERNAME, CONTENT, SENDER', [user, content, sender])

    def addFriend(self, user):
        if self.fetchOne('*', 'friends', self.and_where({'username':user})) is None:
            return self.insertOne('friends', 'USERNAME', [user])
        return True

    def clearTable(self, table):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("DELETE FROM {0}".format(table))
        cur.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = '{0}'".format(table))
        cur.close()
        conn.commit()
        conn.close()
        self.log.debug('Clear table {0}'.format(table))

