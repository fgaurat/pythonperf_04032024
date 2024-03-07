import sqlite3
from Customer import Customer

class CustomerDAO:


    def __init__(self,db_file):
        self.__con = sqlite3.connect(db_file)

    def findAll(self):
        sql = "SELECT * FROM `customers_tbl`"
        cur = self.__con.cursor()
        res = cur.execute(sql)
        for row in res.fetchall():
            c = Customer(*row)
            yield c

    def __del__(self):
        self.__con.close()