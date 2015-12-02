import numpy as np
from matplotlib import pyplot as plt
#이런거 비슷하게 시험문제 나올듯
mileposts = np.array([0,198,303,736,871,1175,1475,1544,1913,2448])
#new axis는 세로로 만드는 방법인듯?
distance_array = np.abs(mileposts - mileposts[:, np.newaxis])

#print(distance_array)

#x가 가로, y가 세로
x,y = np.arange(5), np.arange(5)[:, np.newaxis]
print(x)
print(y)

#x가 세로, y가 가로
x,y = np.ogrid[0:5,0:5]
print(x)
print(y)

#x가 세로숫자로5x5, y가 가로숫자로5x5
x,y = np.mgrid[0:5,0:5]
print(x)
print(y)

#5.5더하는것 각 위치에 대해서 덧셈
print(x+y)

distance = np.sqrt(x**2 + y**2)
print(distance)

plt.pcolor(distance)
plt.colorbar()
#plt.show()

a = np.array([[1,2,3],[4,5,6]])
#ravel 1차원으로 나옴
print(a.ravel())
print(a.T)
#traspost하고 ravel하면 순서가 다름
print(a.T.ravel())

#다시 원상복구할 수 있음
print(a.reshape((2,3)))

#newaxis개념에 대해 한번 봐야할듯
print(a[:,np.newaxis])
print(a[np.newaxis, :])

a = np.arange(4)
#사이즈가 늘어나서 뒤에 0이 채워짐
a.resize((8,))
print(a)

#일반 소팅
#axis가 행인가?
print(np.sort(a,axis=0))

a.sort(axis=0)
print(a)

#index로 소팅
print(np.argsort(a))
#index최고값
print(np.argmax(a))
#index최소값
print(np.argmin(a))

#1차 다항식이라 poly1d
#계수는 순서대로 입력
p = np.poly1d([3,2,-1])
#방정식에 x를 넣었을 때의 값
print(p(0))
#근
print(p.roots)

print(p.order)

#또는
#계수값이 거꾸로 간다.
p = np.polynomial.Polynomial([-1,2,3])


#x,y에 가장 걸맞는 3차식을 만든다.
x = np.linspace(0,1,20)
y = np.cos(x) + 0.3*np.random.rand(20)
p = np.poly1d(np.polyfit(x,y,3))
t = np.linspace(0,1,200)
plt.plot(x,y,'o',t,p(t),'-')
#지금 위에랑 겹쳐서 이렇게 나오는듯..
plt.show()

x = np.linspace(-1,1,2000)
y = np.cos(x) + 0.3*np.random.rand(2000)
p = np.polynomial.Chebyshev.fit(x,y,90)
t = np.linspace(-1,1,200)
plt.plot(x,y,'r.')
plt.plot(t,p(t),'k-',lw=3)
plt.show()

img = plt.imread('a.png')
#x,y, RGB + Alpha
print(img.shape,img.dtype)
#x축으로는 어떻게 크기 조정함?
plt.imshow(img[100:500])
plt.show()