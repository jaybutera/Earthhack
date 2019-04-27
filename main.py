import matplotlib.pyplot
import numpy as np
from PIL import Image

im = Image.open('./heightmap.png')
b = np.array(im)
print(b.shape)
print(b[:,:,0])
