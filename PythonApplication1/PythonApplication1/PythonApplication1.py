'''
num = [1,2,3,4,6,7,8]
#print(dir(num))

List = list(enumerate("Apple"))
#print(List)

print(eval('1+2'))

def even(l) :
        return l%2 == 0;

print(list(filter(even,num)))
'''
'''
a=3
print(id(3))
print(id(a))
'''
'''
num = [1,2,3,4,6,7,8]
print(list(filter(lambda a : a % 2 == 0,num)))
'''
'''
a = [1,2,3]
b = list(a)
c = a
print(a)
print(b)
print(c)

print(id(a))
print(id(b))
print(id(c))
'''
'''
print(list(map(lambda a : a*2, [1,2,3,4])))
'''
'''
print(eval(repr("hi".upper())))
print(eval(str("hi".upper())))
'''
'''
list = [5,1,2,3,9,8,6,7]
print(sorted(list))
print(list)
list.sort()
print(list)
'''
'''
print(list(zip([1,2,3],[4,5,6],[7,8])))
'''

data = {'홍길동' : [80,70,60,92],
       '김길동' : [24,35,18,10],
       '고길동' : [10,20,8,5]}
data.get("홍길동").sort()
data.get("김길동").sort()
data.get("고길동").sort()
print(data["홍길동"])
print(data["김길동"])
print(data["고길동"])


