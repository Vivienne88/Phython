import numpy 

#단순하게 연산 (1,1) * (1,1) 이런식
'''
data = numpy.array([[1,2,3,],[4,5,6],[7,8,9]])
print(data+2)
print(data-2)
print(data*data)
print(data/3)
print(data**2)
print(data**0.5)
print(data.dot(data))
'''

#각원소 마다 수행됨
'''
a = numpy.array([1,2,3,4])
b = numpy.array([4,2,2,4])
c = numpy.array([1,2,3,4])
print(a==b)
print(a>b)

print(numpy.array_equal(a,b))
print(numpy.array_equal(a,c))
'''

'''
a = numpy.array([1,1,0,0], dtype = bool)
b = numpy.array([1,0,1,0], dtype = bool)
print(numpy.logical_or(a,b))
print(numpy.logical_and(a,b))
#모두 True면 True 반환
print(numpy.all([True, True, False]))
#Any면 하나라도 True면 True 반환
print(numpy.any([True, True, False]))
'''

#초월함수
'''
a = numpy.arange(5)
print(a)
print(numpy.sin(a))
print(numpy.log(a))
print(numpy.exp(a))
'''

#전이행렬 Transpose
#대각선 index 0 : 대각선
#대각선 위에는 1 아래는 -1
#a = numpy.triu(numpy.ones((3,3)),0)
#print(a.T)

#x = numpy.array([1,2,3,4])
#print(numpy.sum(x))
#print(x.sum())

#x = numpy.array([[1,1],[2,2]])
##서로 더하기
#print(x.sum(axis=0))

##같은 곳 있는애들 끼리 더하고
#print(x.sum(axis=1))
##범위로 해서 더한 것 바로 위와 동일
#print(x[0,:].sum(),x[1,:].sum())

#x = numpy.array([1,3,2])
#print(x.min())
#print(x.max())
##min의 index
#print(x.argmin())
##max의 index
#print(x.argmax())

#a = numpy.zeros((100,100))
#print(numpy.any(a!=0))
#print(numpy.all(a==a))

#x = numpy.array([1,2,3,1])
#y = numpy.array([[1,2,3],[5,6,1]])
#print(x)
#print(y)
##평균
#print(x.mean())
##중간값
#print(numpy.median(x))

##각 행에 대한 중간값 -1은 무슨 뜻..?반대로 올라간다는 뜻?
#print(numpy.median(y,axis=-1))

#print(x.std())

#from matplotlib import pyplot as plt

#data = numpy.loadtxt('data.txt')
#year,hares,lynxes,carrots = data.T
#plt.plot(year,hares,year,lynxes,year,carrots)
#plt.show()

#각각의 연도별 평균을 구하라
#표준편차
#매년 가장 높은 인구를 갖는 종

data = numpy.loadtxt('data.txt')
print(data[1].mean(0))
print(data[2].mean(0))

#broadcasting연산
data = numpy.array([0,1,2,3,4,5])
#괄호 하나랑 두개랑 다른듯?
#하나는 Vector 두개는 배열
data2 = numpy.array([[0,10,20,30,40,50]]).T
print(data.shape)
print(data2.shape)
m_data = data2+data
print(m_data)