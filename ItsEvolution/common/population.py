import random

REP_NORMALIZE = 0.5
INC_AGE = 0.25

class Human:

    def __init__(self,pop,parent1,parent2,age):
        self.id = pop.idControl
        self.name = 'xxx'
        self.sex = random.randrange(2)
        self.age = age
        self.cooldown = 0
        if parent1 == None or parent2 == None:
            self.father = None
            self.mother = None
        elif parent1.sex == 0:
            self.father = parent1
            self.mother = parent2
        else:
            self.father = parent2
            self.mother = parent1

        r = random.randrange(1000000)
        if (r == 0):
            self.rep = 0
        else:
            self.rep = random.random() + REP_NORMALIZE
            if(self.rep > 1):
                self.rep = 1

        pop.incIdControl()

    def incAge(self):
        self.age += INC_AGE

    def isDead(self,r,pops):
        if self.age > 199:
            return 1
        if self.sex == 0:
            return r <= pops[int(round(self.age))].m
        else:
            return r <= pops[int(round(self.age))].f

    def mayIFuck(self):
        if self.sex == 1:
            if self.cooldown > 0:
                self.decCoolDown()
                return 0
            if(self.age > 12 and self.age < 60):
                return 1
        else:
            if(self.age > 12):
                return 1
        return 0

    def potentialPartner(self,partner):
        if(self == partner):
            return 0
        if(self.sex == partner.sex):
            return 0
        if(not partner.mayIFuck()):
            return 0
        return 1

    def copulated(self,partner):
        p = (self.rep + partner.rep) / 2
        if random.random() <= p:
            self.cooldown = 3
            return 1

    def decCoolDown(self):
        self.cooldown -= 1
        return 0

    def printAll(self):
        print("Id: {}".format(self.id) )
        print('--------------')

        if (self.sex == 0):
            print("Sex: " + 'Homem')
        else:
            print("Sex: " + 'Mulher')
        print("Age: " + str(self.age))
        print("Reproductiveness: " + str(self.rep))

        print('\n')


class PopulationStats:
    def __init__(self):
        self.idControl = 0

    def incIdControl(self):
        self.idControl += 1