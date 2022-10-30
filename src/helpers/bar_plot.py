from timeflux.core.node import Node
from timeflux.nodes.random import Random
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class BarPlot(Node):

    def __init__(self,l=3):
        plt.ion()

    def update(self):
        if not self.i.ready():
            return 
        y = self.i.data.values[0]
        plt.bar([1, 2, 3], y)
        plt.draw()
        plt.pause(0.00000000001)
        plt.clf()


#random = Random(columns=3, rows_max=1, rows_min=1, names=['1','2','3'])
#random.update()
#bar_plot = BarPlot()
#bar_plot.i.data = pd.DataFrame( np.random.random_sample((1, 3)), columns=['1','2','3'])
#bar_plot.update()
