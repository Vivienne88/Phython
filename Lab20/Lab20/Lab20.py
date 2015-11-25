import numpy as np
from matplotlib import pyplot as plt
'''
data = np.array([[1,2,3],[4,5,6],[7,8,9]])
#data = np.array(['1','2','3'])
data.astype(np.float)
print()

print(np.eye((3)))
data2 = np.diag(np.array([1,2,3,4]))

print(np.arange(10).reshape(2,5))

print(np.linspace(1.,4., 6, endpoint=False))

print(np.random.rand(4))
print(np.random.randn(4))
'''
'''
data = np.loadtxt("data.txt")
year, hares, lynxes, carrots = data.T
print(data)
print('\n')
print(data[1:4:2, ::3])
'''
'''
x = np.arange(10,1,-1)
print(x)
print(x[np.array([[1,1],[2,3]])])

y = np.arange(35).reshape(5,7)
print(y)
print()
print(y[np.array([0,2,4])])
print()

b = y>20
print(y[b])
'''

data = np.arange(36).reshape(6,6)
print(data)
print()

mask = np.array(np.array([1,0,1,0,0,1],dtype=bool))
print(data[mask,2])

#mask1 = np.array([1,0,1,0,0,1],dtype=bool)
mask1 = np.array([0,2,5])
print()
print(data[3:,mask1])