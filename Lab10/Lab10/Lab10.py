import os
import sys
import pickle
import shutil

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

os.path.dirname('c:/python34/python.exe')