import random
from sim import *

def randpoint(n,m):
    rx = random.randint(0,n-1)
    ry = random.randint(0,m-1)
    return (rx,ry)

def uniquepoint(n,m,plantmap):
    while True:
        r = randpoint(n,m)
        if r not in plantmap:
            return r

def new_pop(heightmap, plantmap):
    (X,Y) = heightmap.shape

    pop = []

    for g in range(0, 10):
        new_plantmap = {}
        # A chance to randomly re-assign plant locations
        for k in plantmap.keys():
            if random.uniform(0,1) < .2:
                r               = uniquepoint(X,Y,plantmap)
                new_plantmap[r] = plantmap[k]
            else:
                new_plantmap[k] = [plantmap[k][0],0]

        # Randomly add new coverage plants
        #
        if random.uniform(0,1) < .1:
            r               = uniquepoint(X,Y,plantmap)
            new_plantmap[r] = [np.random.choice([9,10,11,12]), 0]

        pop.append(new_plantmap)

    return pop

def get_source(heightmap):
    maxims = np.where(heightmap == heightmap.max())
    return (maxims[0][0], maxims[1][0])

def fitness(heightmap, plantmap):
    sim = Sim(heightmap, plantmap, get_source(heightmap))
    for i in range(0,20):
        sim.step()

    return -sum( [v[1] for v in sim.plantmap.values()] )
