#def sum_and_mul(A,B) :
#    return A+B, A*B

#sum, mul = sum_and_mul(10,20)
#print(sum,mul)

#def print_data (data, level=0):
#    for item in data:
#        if isinstance(item, list):
#            print_data(item, level+1)
#        else:
#            for i in range(level):
#                print("\t",end="")
#            print(item)

#import print_data

#data = ["홍길동",["암살",["황정민","뀨뀨"]],"고길동",["암살"]]
#print_data.print_data(data)

import os

print(os.getcwd())
#os.mkdir("sample")
os.chdir(".//sample")
print(os.getcwd())
os.system("setup.py sdist")
os.system("setup.py install")