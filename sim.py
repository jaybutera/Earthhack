class Sim(object):
    def __init__(self, bmp):
        self.heightmap = bmp
        self.watermap  = np.empty(bmp.shape)

        self.runoff_ratio = 0.6

    def step_point(self, idx):
        runoff_amount = self.watermap[idx] * self.runoff_ratio
        lower_cells = 
