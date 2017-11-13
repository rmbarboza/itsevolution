import random
from common.population import human
from common.utils import popstats,startpops

YEARS = 8
INITIAL_POP = 100
SEX_RAND = 0.01
NUMBER_SEX_TRIES = int(round(SEX_RAND * INITIAL_POP))


hlist = []
men = 0
women = 0

pops = startpops()

for i in range(INITIAL_POP):
    h = human(random.randrange(0,100))
    hlist.append(h)
    #if h.rep == 0:
    #   h.printAll()
    if h.sex == 0:
        men += 1
    else:
        women += 1

new_hlist = []

deaths_men = deaths_women = 0
born_men = born_women = 0

for k in range(YEARS*4):
    for h in hlist:
        if (h.sex == 1 and h.age < 60) or h.age > 12: #condição transante
            for i in range(NUMBER_SEX_TRIES): #loop de tentativas com n indivíduos
                n = random.randrange(hlist.__len__())
                s = hlist[n]
                if s.age < 12 or s == h or s.sex == h.sex:
                    continue

                if s.age >= 60 and s.sex == 1:
                    continue

                p = (s.rep + h.rep)/2
                if random.random() <= p:
                    n = human(0)
                    new_hlist.append(n)
                    if n.sex == 0:
                        born_men += 1
                    else:
                        born_women += 1

        if h.isDead(random.random(),pops): #verifica se morreu
            #h.printAll()
            hlist.remove(h)
            if h.sex == 0:
                deaths_men += 1
            else:
                deaths_women += 1
        else:
            h.incAge()
    hlist = hlist + new_hlist

men = men + born_men - deaths_men
women = women + born_women - deaths_women

print("Hlist: " + str(hlist.__len__()))
print("Men: " + str(men))
print("Women: " + str(women))
print("Births: M -> " + str(born_men) + " F -> " + str(born_women))
print("Deaths: M -> " + str(deaths_men) + " F -> " + str(deaths_women))

print(pops[0].m)
