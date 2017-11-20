import random
from itsevolution.common.population import Human,PopulationStats
from itsevolution.common.utils import Popcontrol,startpops

YEARS = 10
INITIAL_POP = 100
SEX_RAND = 0.01
NUMBER_SEX_TRIES = int(round(SEX_RAND * INITIAL_POP))


hlist = []
men = 0
women = 0
men_fuckable = 0
women_fuckable = 0

pops = startpops()

popSt = PopulationStats()

for i in range(INITIAL_POP):
    h = Human(popSt, None, None, random.randrange(0, 100))
    hlist.append(h)
    #if h.rep == 0:
    #   h.printAll()
    if h.sex == 0:
        men += 1
        men_fuckable += h.mayIFuck()
    else:
        women += 1
        women_fuckable += h.mayIFuck()

print("Initial population:")
print("-------------------")
print("Men: {} Fuckbable: {} ({}%)".format(men,men_fuckable,round((men_fuckable/men)*100,2)))
print("Women: {} Fuckbable: {} ({}%)".format(women,women_fuckable,round((women_fuckable/women)*100,2)))
print("-------------------\n")


new_hlist = []

deaths_men = deaths_women = 0
born_men = born_women = 0

for k in range(YEARS*4):
    for h in hlist:
        if h.mayIFuck(): #condição transante
            for i in range(NUMBER_SEX_TRIES): #loop de tentativas com n indivíduos
                n = random.randrange(hlist.__len__())
                s = hlist[n]

                if(not h.potentialPartner(s)):
                    continue

                if h.copulated(s):
                    n = Human(popSt, h, s, 0)
                    new_hlist.append(n)
                    if n.sex == 0:
                        born_men += 1
                    else:
                        born_women += 1

                    break


        if h.isDead(random.random(),pops): #verifica se morreu
            h.printAll()
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


