import random

REP_NORMALIZE = 0.5
INC_AGE = 0.25

class human:
    def __init__(self,age):
        self.name = 'xxx'
        self.sex = random.randrange(2)
        self.age = age

        r = random.randrange(1000000)
        if (r == 0):
            self.rep = 0
        else:
            self.rep = random.random() + REP_NORMALIZE
            if(self.rep > 1):
                self.rep = 1

    def incAge(self):
        self.age += INC_AGE

    def isDead(self,r,pops):
        if self.age > 199:
            return 1
        if self.sex == 0:
            '''if r <= pops[int(round(self.age))].m:
                print(int(round(self.age)))
                print(r, pops[int(round(self.age))].m)
                return 1'''
            return r <= pops[int(round(self.age))].m
        else:
            return r <= pops[int(round(self.age))].f

    def printAll(self):
        print(self.name )
        print('--------------')

        if (self.sex == 0):
            print("Sex: " + 'Homem')
        else:
            print("Sex: " + 'Mulher')
        print("Age: " + str(self.age))
        print("Reproductiveness: " + str(self.rep))

        print('\n')