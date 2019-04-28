import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from PIL import Image
from ga import *

# Returns a plantmap
def constraint2config(constraints, shape):
    #TODO: This is wrong
    (n,m) = shape
    plantmap = {}
    for k in constraints.keys():
        for _ in range(0, constraints[k]):
            rx = random.randint(0,n-1)
            ry = random.randint(0,m-1)
            plantmap[ (rx,ry) ] = [k,0]

    return plantmap
    #return { ( (random.randint(0,n-1),random.randint(0,m-1)), [k,0] ) for k in constraints.keys() } 

def pm2arr(plantmap):
    print(plantmap)
    return (np.array([k[0] for k in plantmap.keys()]), np.array([k[1] for k in plantmap.keys()]))


def get_source(heightmap):
    maxims = np.where(heightmap == heightmap.max())
    return (maxims[0][0], maxims[1][0])

'''
im = Image.open('./tmp.png')
b = np.array(im)
bmp = b[:,:,0]
print(b.shape)
'''

shape = (8,8)
X = np.empty(shape)
for i in range(0,8):
    for j in range(0,8):
        X[i,j] = i*j
print(X)

# plant-id : quantity
constraints = { 0:10, 3:5, 6:1 }

pop = new_pop(X, constraint2config(constraints, X.shape))

# Track some history
fitness_history  = []
alltime_best_fit = -10000
alltime_best_g   = None

for i in range(0,10):
    fits     = [fitness(X,a) for a in pop]
    most_fit = np.argmax( np.array(fits) )
    top_g    = pop[most_fit]

    # Regenerate population
    pop = new_pop(X, top_g)
    pop.append(top_g)

    top_fit = fits[most_fit]
    fitness_history.append(top_fit)
    print(top_fit)

    if top_fit > alltime_best_fit:
        alltime_best_fit = top_fit
        alltime_best_g   = top_g


# Plot shit
#plt.plot(fitness_history)
#plt.show()
#plt.imshow(X, norm=plt.Normalize(vmin=0, vmax=np.max(X)), cmap='gray')

plt.contourf(X, \
        cmap=cm.PRGn, \
        norm=cm.colors.Normalize(vmax=X.max(), vmin=X.min()))
l = pm2arr(alltime_best_g)
plt.scatter(l[0],l[1])
plt.show()
