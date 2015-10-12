import os
import sys
import pickle
import shutil
'''
os.system("python test.py a b c")
#print(sys.path.append("경로"))

class Student:
    def __init__(self, name, age) :
        self.name = name
        self.age = age
    def show(self) :
        print(self.name,":",self.age)

Y=Student("양수현",26)
Y.show()

f = open("My_Object.txt","wb")
pickle.dump(Y,f)
f.close()

f = open("My_Object.txt","rb")
Y = pickle.load(f)
print(Y)
Y.show()
f.close()
'''
#print(os.environ)
#print(list(os.walk(".")))

#os.mkdir("sample")
#os.chdir("sample")
#print(os.getcwd())
'''
fl = list(os.walk("."))
count = 0
for i in fl :
    for j in i :
        for c in j :
            if "txt" in c :
                print(c)
                shutil.copy(c,"des.txt")
'''

#dirname('c:/python34/python.exe')

#os.path.dirname('c:/python34/python.exe')
import glob
'''
os.chdir("C:/Python34")
print(glob.glob("*.exe"))
os.chdir("..")
print(os.getcwd())
print(glob.glob("*.py"))
'''
'''
import os.path
ndir = nfile = 0
def traverse(dir,depth) :
    global ndir, nfile
    for obj in glob.glob(dir + '/*'):
        if depth == 0 :
            prefix = "|--"
        else :
            prefix = "|" + " " * depth + "|--"
        if os.path.isdir(obj) :
            ndir += 1
            print(prefix + os.path.basename(obj))
            traverse(obj,depth+1)
        elif os.path.isfile(obj) :
            nfile += 1
            print(prefix + os.path.basename(obj))
        else :
            print(prefix + 'unknown object:',obj)

    if __name__ == '__main__' :
        traverse('..',0)
        print('\n',ndir,'directories', nfile, 'files' )

traverse("C:/Python34",0)
'''
'''
import tempfile
with tempfile.TemporaryFile('w+',delete=False) as fp:
    fp.write("Hello World")
    fp.seek(0)
    data3 = fp.name
    print(data3)
    data2 = fp.read()
'''  
'''
import time
time1 = time.ctime(999999999)
t = time.strptime(time1)
t3 =time.strftime("%Y %m %d %I %M",time.localtime())
print(t3)
print(time1)
print(t)

'''
'''
import calendar
#print(calendar.calendar(2000))
calendar.prcal(2000)
calendar.prmonth(2015,10)
'''
'''
import random
R = random.sample(range(101),10)
print(R)
random.shuffle(R)
print(R)
print(random.choice(R))
'''
import random
data = [('RED',3),('BLUE',1),('GREEN',4),('YELLOW',2)]
datalist = []
'''
for val, cnt in data:
    for i in range(cnt):
        datalist.append(val)
'''
datalist = [val for val, cnt in data for i in range(cnt)]


print(datalist)
random.shuffle(datalist)
print(random.choice(datalist))
