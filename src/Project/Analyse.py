from timeflux.core.node import Node
import numpy as np
import pandas as pd


class Power_Compute(Node) :
    def __init__(self) :
        pass
    
    def update(self) :
        
        if not self.i.ready():
            return
        
        print(self.i)
        
        self.o = self.i
        self.o.data = self.o.data**2

