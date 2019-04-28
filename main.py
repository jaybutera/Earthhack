import matplotlib.pyplot
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

X = np.arange(8*8).reshape((8,8))
source = [7,7]

s = Sim(X, source)
for i in range(0,5):
    s.step()
