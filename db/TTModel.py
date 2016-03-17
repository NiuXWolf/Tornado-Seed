from db import Model
import consts

def create_table():
    db=Model.sqlite()
    db.execute('''CREATE TABLE COMPANY
    (ID INT PRIMARY KEY     NOT NULL,
    NAME           TEXT    NOT NULL,
    AGE            INT     NOT NULL,
    ADDRESS        CHAR(50),
    SALARY         REAL);''')

def add():
    Model.sqlite().execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )")
    Model.sqlite().execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")
    Model.sqlite().commit()

    # def get_subscribers(self, limit=200, offset=0):
    #     return self.sqlite.query("select * from subscribers where status='on'")
