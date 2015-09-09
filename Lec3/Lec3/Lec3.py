#dic = {"홍길동":{"코난":5.0,"고질라":4.5},
#       "고길동":{"타잔":2.0,"뮬란":1.0}}
#print(dic.get("홍길동"))
#print(dic.get("홍길동").get('코난'))
#print(dic["홍길동"]["코난"])

#answer = input("선배 밥 사주세요.")
#answer = answer.lower()
#if answer == "no" :
#    print("짠돌이세요?")
#elif answer == "yes" :
#    print("멋있는 선배")

#for i in range(2,10) :
#    for j in range(1,9) :
#        print("%d * %d = %d" % (i,j,i*j),end = " ")
#        print(i*j, end= " ")
#    print("")

import turtle
turtle = turtle.Turtle()
#for steps in range(4) :
#    turtle.forward(100)
#    turtle.right(90)

#for steps in range(4) :
#    turtle.forward(100)
#    turtle.right(90)
#    for moresteps in range(4) :
#        turtle.forward(50)
#        turtle.right(90)

nSides = 8
for steps in range(nSides) :
    turtle.forward(100)
    turtle.right(360/nSides)
    for moresteps in range(nSides) :
        turtle.forward(50)
        turtle.right(360/nSides)
