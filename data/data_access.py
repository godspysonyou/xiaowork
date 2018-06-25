import pymysql
import time
import datetime


class DataAccess():
    def __init__(self, host='localhost', user='root', password='hdu417', db='test', port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.port = port
        self.conn = None
        self.cursor = None

    def open_conn(self):
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, port=self.port,
                                    charset='utf8')
        self.cursor = self.conn.cursor()

    def select_(self, sql):
        try:
            self.open_conn()
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            raise e
        finally:
            self.conn.close()
            self.cursor.close()

    def update_(self, sql):
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
        return self.select(sql='SELECT VERSION()')[0][0]

    def insert_action(self, DZ, FLAG='start'):
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = 'insert into DZ(SJC,GRGH,LJGH,DZ,FLAG) values("%s","%s","%s","%s","%s")' % (
        current_time, '1A', '0A', DZ, FLAG)
        self.update_(sql)


# 耗材分时监控表
class MaterialData(DataAccess):
    def __init__(self):
        super(MaterialData, self).__init__()

    def select(self):
        sql = ''
        result = self.select_(sql)
        return result

    def update(self, sql):
        sql = ''
        self.update_(sql)


# OEE效能日推表
class OEEData(DataAccess):
    def __init__(self):
        super(OEEData, self).__init__()

    def select(self):
        sql = 'Select * from oee_date'
        result = self.select_(sql)
        return result

    def update(self, sql):
        sql = ''
        self.update_(sql)



# 设备工作损失时间统计表
class EquipmentTimeData(DataAccess):
    def __init__(self):
        super(EquipmentTimeData, self).__init__()

    def select(self):
        sql = 'Select * from loss'
        result = self.select_(sql)
        return result

    def update(self, sql):
        sql = ''
        self.update_(sql)


# 设备工作损失时间占比表
class EquipmentData(DataAccess):
    def __init__(self):
        super(EquipmentData, self).__init__()

    def select(self):
        sql = 'Select * from loss'
        result = self.select_(sql)
        return result

    def update(self, sql):
        sql = ''
        self.update_(sql)


if __name__ == "__main__":
    da = EquipmentData()
    result=da.select()
    print(result[-1])
