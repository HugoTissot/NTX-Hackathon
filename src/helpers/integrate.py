from timeflux.core.node import Node
import numpy as np


class Integrate(Node):
    
    def __init__(self):
        pass
    
    def update(self):
        
        if not self.i.ready():
            return

        print(self.i)
        data = (self.i.data)**2

        self.o = self.i
        print('before integral')
        print(self.o.data)
        # inter = data.apply(np.sum,axis=1)
        # self.o.data = inter/sum(inter)
        data.o.data = (lambda x: x/sum(x))(data.apply(np.sum,axis=1))
        print('after integral')
        print(self.o.data)