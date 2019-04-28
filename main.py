import matplotlib.pyplot
import numpy as np
from PIL import Image
from scipy.ndimage import maximum_filter

def get_maxima(bmp):
    mx   = maximum_filter(bmp, size=3)
    diff = np.where(mx == bmp, bmp, 0)
    res  = np.where(diff != 0)

    return np.array([ (res[0][i], res[1][i]) for i,_ in enumerate(res[0]) ])

bitmap = np.array( Image.open('./heightmap.png') )[:,:,0]
(N,M) = bitmap.shape
print(bitmap.shape)

print( get_maxima(bitmap) )
