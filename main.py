import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from sim import *

'''
def evaluate():

def _fitness(x):
    sim = Sim(bmp)
    for i in range(0,20):
        sim.update()
'''

'''
im = Image.open('./heightmap.png')
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
#X = np.arange(8*8).reshape((8,8))
source = [7,7]

plantmap = { (6,7):[1,0] }

s = Sim(X, plantmap, source)
for i in range(0,6):
    s.step()
    print(s.watermap)
    plt.imshow(s.watermap, norm=plt.Normalize(vmin=0, vmax=np.max(s.watermap)), cmap='gray')
    plt.show()
