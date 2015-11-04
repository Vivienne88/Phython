import sqlite3
con = sqlite3.connect("test.db")

cur = con.cursor()
#con.commit()
con.isolation_level = None
dropsql = "drop table if exists phonebook;"
cur.execute(dropsql)
sql = '''create table if not exists
            phonebook(name text, phoneNum text);'''
cur.execute(sql)
insertsql = '''insert into phonebook
                values("greenjoa1","010-1111-2222");'''
cur.execute(insertsql)
insertsql = '''insert into phonebook
                values(?,?);'''
cur.execute(insertsql, ("hihi","010-9999-XXXX"))
insertsql = '''insert into phonebook
                values(:MyName, :MyNum);'''
cur.execute(insertsql, {"MyNum":"010-XXXX-YYYY", "MyName":"dede"})
insertsql = '''insert into phonebook values(?,?);'''
datalist = (('nini','011-PASO-PASO'),
            ('Gaga','012-ABCD-EFGH'))
cur.executemany(insertsql,datalist)
def dataGenerator():
    datalist = (("GEN1","010-9999-9999"),("GEN2","010-8888-8888"))
    for item in datalist:
        yield item
cur.executemany(insertsql,dataGenerator())
showsql = '''select *
             from phonebook order by name;'''
cur.execute(showsql)
cur.execute("insert into phonebook(phoneNum) values('010-XYXY-ABAB');")
cur.execute("select count(*) from phoneBook;")
print(cur.fetchone()[0])
cur.execute("select count(name) from phoneBook;")
print(cur.fetchone()[0])
#대문자로 정렬할 경우 ASCII로 받아서, 대문자가 먼저 나온다.
def OrderFunc(str1,str2):
    s1 = str1.upper()
    s2 = str2.upper()
    return (s1>s2) - (s1<s2)
con.create_collation("myordering",OrderFunc)
cur.execute("select * from phonebook order by name collate myordering;")
for row in cur:
    print(row)
sql = '''create table if not exists
        user(name text, age int)'''
cur.execute(sql)
insertsql = '''insert into user
                values(?,?)'''
datalist = (("U1",10),("U2",50),("U3",90),("U4",30),("U5",40),("U6",60),("U7",70))
cur.executemany(insertsql,datalist)
cur.execute("select MAX(age) from user")
print(cur.fetchone()[0])
cur.execute("select SUM(age) from user")
print(cur.fetchone()[0])
class Average:
    def __init__(self):
        self.sum = 0
        self.cnt = 0

    def step(self,value):
        self.sum += value
        self.cnt += 1

    def finalize(self):
        return self.sum/self.cnt

#사용할 명령어, 인자 갯수, 함수 이름
con.create_aggregate("AVG", 1, Average)
cur.execute("select AVG(age) from user;")
print(cur.fetchone()[0])
#cur.execute("select * from user")
#for row in cur:
#    print(row)
#print(cur.fetchall())
#print(cur.fetchone())
#print(cur.fetchmany(2))
