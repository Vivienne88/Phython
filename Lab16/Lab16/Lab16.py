import sqlite3 as sqlite

def init_db():
    db = sqlite.connect("test.db")
    with open('schema.sql') as f:
          db.cursor().executescript(f.read())
          db.commit()
          db.close()

def get_db():
    db = sqlite.connect("test.db")
    return db

def register():
    print("**** 회원가입 ****\n")
    print("user id : ", end="")
    user_id = input()
    db = get_db()
    cur = db.cursor()
    cur.execute("select * from user where userid =?",[user_id])
    if(cur.fetchone() != None):
        print("아이디가 존재합니다.")
    #insert 
    #sql = "insert into user(userid) values(?);"
    #cur.execute(sql,[user_id])
    print("user name : ", end="")
    username = input()
    print("user passwd : ", end="")
    userpasswd = input()
    sql = "insert into user(userid, username, userpw) values(?,?,?)"
    cur.execute(sql, [ user_id, username, check_password_hash(userpasswd)])
    cur.execute("select * from user")
    print(cur.fetchall())
    db.commit()

def login():
    print("**** 로그인 ****\n")
    print("user id : ", end="")
    userid = input()
    pritn("user passwd : ", end="")
    userpasswd = input()

    db = get_db()
    cur = db.cursor()
    cur.exectue("select * from user where userid=?",[userid])
    temp = cur.fetchone()
    if(temp == None) :
         print("아이디가 존재합니다.")
         return
    elif(check_password_hash(temp[3],[userpasswd])):
         print("로그인 성공")
         return
    else:
         print("비밀번호 체크요함")
         return

init_db()
register()