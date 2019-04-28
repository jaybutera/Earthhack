import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from ga import *

# Returns a plantmap
def constraint2config(constraints, shape):
    #TODO: This is wrong
    (n,m) = shape
    plantmap = {}
    for k in constraints.keys():
        rx = random.randint(0,n-1)
        ry = random.randint(0,m-1)
        plantmap[ (rx,ry) ] = [k,0]

    return plantmap
    #return { ( (random.randint(0,n-1),random.randint(0,m-1)), [k,0] ) for k in constraints.keys() } 

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

source = [7,7]

# plant-id : quantity
constraints = { 0:1, 3:1, 6:1 }

pop = new_pop(X, constraint2config(constraints, X.shape))
for i in range(0,10):
    fits = [fitness(X,a) for a in pop]
    most_fit = np.argmax( np.array(fits) )
    pop = new_pop(X, pop[most_fit])
    print(fits)

'''
plantmap = { (6,7):[1,0],(5,7):[3,0] }

s = Sim(X, plantmap, source)
for i in range(0,6):
    s.step()
    print(s.watermap)
    plt.imshow(s.watermap, norm=plt.Normalize(vmin=0, vmax=np.max(s.watermap)), cmap='gray')
    plt.show()
'''
