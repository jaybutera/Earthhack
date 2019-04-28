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

X = np.empty((8,8))
for i in range(0,8):
    for j in range(0,8):
        X[i,j] = i*j
print(X)
#X = np.arange(8*8).reshape((8,8))
source = [3,7]

s = Sim(X, source)
for i in range(0,3):
    s.step()
    print(s.watermap)
    plt.imshow(s.watermap, norm=plt.Normalize(vmin=0, vmax=np.max(s.watermap)), cmap='gray')
    plt.show()
