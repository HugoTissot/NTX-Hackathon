import matplotlib.pyplot as plt
import numpy as np
from timeflux.core.node import Node
from timeflux.nodes.random import Random
#from mpl_toolkits.mplot3d import Axes3D



class ThreeDplot(Node):

    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot( 111, projection='3d' )
    
    def update(self):
        if not self.i.ready():
            return

        # fig = plt.figure()
        # ax = fig.add_subplot(111, projection='3d')

        # for k in xrange(0,X_range):
        #     ax.plot(x_input, y_input, z_input)
        #     plt.draw()
        #     plt.pause(0.02)
        #     ax.cla()


        y=self.i.data.values[0]
        xs=y[0]
        ys=y[1]
        zs=y[2]

        # fig=plt.figure()
        # ax=fig.add_subplot(projection='3d')

        self.ax.scatter(xs,ys,zs,c='r',alpha=1,s=100)
        self.ax.scatter(0,ys,zs,c='r',alpha=0.2,s=100)
        self.ax.scatter(xs,9,zs,c='r',alpha=0.2,s=100)
        self.ax.scatter(xs,ys,0,c='r',alpha=0.2,s=100)
        self.ax.set_xlabel('PC1')
        self.ax.set_ylabel('PC2')
        self.ax.set_zlabel('PC3')
        self.ax.set_xlim([0,9])
        self.ax.set_ylim([0,9])
        self.ax.set_zlim([0,9])
        plt.draw()
        plt.pause(0.001)
        self.ax.cla()

# random = Random(columns=3, rows_max=1, rows_min=1, names=['1','2','3'])
# random.update()
# threeD_plot = ThreeDplot()
# threeD_plot.i.data = pd.DataFrame( np.random.random_sample((1, 3)), columns=['1','2','3'])
# threeD_plot.update()
