import scipy.ndimage as ndimage
import numpy as np
import copy
import plantDb as pb

class Sim(object):
    def __init__(self, bmp, plantmap, source):
        self.heightmap      = bmp
        self.watermap       = np.zeros(bmp.shape)
        self.virt_watermap  = np.zeros(bmp.shape)
        self.plantmap       = plantmap
        self.source         = source
        self.N              = bmp.shape[0]
        self.M              = bmp.shape[1]

        self.runoff_ratio = 0.8
        self.evap_rate    = 0.9
        self.min_eval     = 0.01

    def step_point(self, x, y):
        # Don't process if the amount is too small
        if self.virt_watermap[x,y] < self.min_eval:
            return

        # Some water evaporates
        if (x,y) in self.plantmap:
            p_id                    = self.plantmap[(x,y)][0]
            plant_ev                = pb.plantdb[p_id][3]
            possible_evap           = self.virt_watermap[x,y] - plant_ev
            self.virt_watermap[x,y] = possible_evap * self.evap_rate + plant_ev
        else:
            self.virt_watermap[x,y] *= self.evap_rate

        # Some is absorbed (if there is a plant)
        if (x,y) in self.plantmap:
            p_id = self.plantmap[(x,y)][0]
            diff = self.virt_watermap[x,y] - pb.plantdb[p_id][2]
            # Absorb by rate amount
            self.virt_watermap[x,y] = max(diff,0)
            # Adjust plant thirst
            self.plantmap[(x,y)][1] -= pb.plantdb[p_id][2]#diff #TODO: This is not correct

        # Some runs off
        runoff_amount = self.virt_watermap[x,y] * self.runoff_ratio
        lower_cells   = self._get_lower_cells(x,y)
        for i in lower_cells:
            self.virt_watermap[i[0],i[1]] += (runoff_amount / lower_cells.size)

        self.virt_watermap[x,y] -= runoff_amount

    def _get_lower_cells(self, x,y):
        # Get neighbor indices
        idxs  = np.empty(shape=[0,2], dtype=int)
        if x > 0:
            idxs=np.append(idxs, [[x-1,y]], axis=0)
        if y > 0:
            idxs=np.append(idxs, [[x,y-1]], axis=0)
        if x > 0 and y > 0:
            idxs=np.append(idxs, [[x-1,y-1]], axis=0)
        if y > 0 and x < self.N-1:
            idxs=np.append(idxs, [[x+1,y-1]], axis=0)
        if x < self.N-1:
            idxs=np.append(idxs, [[x+1,y]], axis=0)
        if x < self.N-1 and y < self.M-1:
            idxs=np.append(idxs, [[x+1,y+1]], axis=0)
        if y < self.M-1:
            idxs=np.append(idxs, [[x,y+1]], axis=0)
        if y < self.M-1 and x > 0:
            idxs=np.append(idxs, [[x-1,y+1]], axis=0)

        # Get height values of those indices
        heights = [self.heightmap[i[0],i[1]] for i in idxs]

        # Return indices with height < h
        h = self.heightmap[x,y]
        return np.array([i[1] for i in enumerate(idxs) if heights[i[0]] <= h])

    def update(self):
        self.watermap = copy.deepcopy(self.virt_watermap)

    def step(self):
        # Inject water at source
        (sx,sy) = self.source
        self.virt_watermap[sx,sy] += 10

        # Simulate each point
        for i in range(0,self.N):
            for j in range(0,self.M):
                self.step_point(i,j)

        self.update()
