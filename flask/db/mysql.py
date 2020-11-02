import pymysql


class Testdb:
    def __init__(self):
        self.db = pymysql.connect(host='127.0.0.1',
                     port=3306, user='root', passwd='link#1234',
                     db='test', charset='utf8')

    def select_all(self):
        cursor = self.db.cursor()
        sql = 'select * from test.table1'
        cursor.execute(sql)
        result = cursor.fetchone()
        return result

