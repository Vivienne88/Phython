#from abc import ABCMeta, abstractmethod

#class Terran(metaclass=ABCMeta) :
#    def __init__(self,name) :
#        self.name = name
#    @abstractmethod
#    def attack(self) :
#        pass

#class Tank(Terran) :
#    def __init__(self, name, damage) :
#        super().__init__(name)
#        self.damage = damage
#    def attack(self) :
#        print(str(self.damage)+"탱크알 쏩니다.")

#class Marine(Terran) :
#    def __init__(self,name, hp) :
#        super().__init__(name)
#        self.hp = hp
#    def attack(self) :
#        print("총을 쏩니다.")

#def attack(terran):
#    terran.attack()

#t1 = Tank("tank",40)
#t2 = Marine("marine",6)

#tlist = [Tank("tank1",40),Tank("tank2",70),Tank("tank3",75),Tank("tank4",80),Tank("tank5",85)]

#for item in tlist :
#    attack(item)


class MyList(list):
    name = ""
    def __init__(self,name) :
        super().__init__([])
        self.name = name
    def __str__(self) :
        return self.name + ":" + super().__str__()


list1 = MyList("1번 리스트")
list1.append(10)
list1.append(20)
list1.append(30)
list1.append(40)
list1.append(50)
list1.append(60)
print(list1)

print(dir(list))
#print(dir(list1))

