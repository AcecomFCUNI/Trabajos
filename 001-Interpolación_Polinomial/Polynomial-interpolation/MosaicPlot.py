import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sn

# Setting seaborn look for pyplot
#sn.set()

class MosaicPlot:
    def __init__(self, mat_data):
        self.fig, self.axs = plt.subplots(1, 1)
        self.axs.imshow(mat_data)
        self.axs.set_aspect(1)        
        
    def show(self):
        plt.show(self.fig)
