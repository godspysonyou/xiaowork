import pymysql


class DataAccess():
    def __init__(self, host='localhost', user='root', password='123456', db='test', port=3306):
        self.host = host
        self.user = user
        self.password = '123456'
        self.db = db
        self.port = port
        self.conn = None
        self.cursor = None

    def open_conn(self):
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, port=self.port,
                                    charset='utf8')
        self.cursor = self.conn.cursor()

    def select(self, sql):
        try:
            self.open_conn()
            self.cursor.execute(sql)
            results = self.cursor.fetchone()
            return results
        except Exception as e:
            raise e
        finally:
            self.conn.close()
            self.cursor.close()

    def update(self, sql):
        try:
            self.open_conn()
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
        finally:
            self.conn.close()
            self.cursor.close()

    def select_version(self):
        # import functools
        # s = functools.partial(self.select, sql='SELECT VERSION()')
        # return s()[0]
        return self.select(sql='SELECT VERSION()')[0]


if __name__ == "__main__":
    da = DataAccess()
    print(da.select_version())
