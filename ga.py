import random
from sim import *

def new_pop(heightmap, plantmap):
    (X,Y) = heightmap.shape

    pop = []

    for g in range(0, 10):
        new_plantmap = {}
        # A chance to randomly re-assign plant locations
        for k in plantmap.keys():
            if random.uniform(0,1) < .2:
                rx = random.randint(0,X-1)
                ry = random.randint(0,Y-1)
                new_plantmap[(rx,ry)] = plantmap[k]
            else:
                new_plantmap[k] = [plantmap[k][0],0]

        # Randomly add new coverage plants
        #

        pop.append(new_plantmap)

    return pop

def fitness(heightmap, plantmap):
    sim = Sim(heightmap, plantmap, [7,7])
    for i in range(0,20):
        sim.step()

    return -sum( [v[1] for v in sim.plantmap.values()] )
