# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 19:04:12 2022

@author: thoma
"""

from timeflux.core.node import Node
import matplotlib.pyplot as plt

class BarPlot(Node):
    
    def __init__(self,l=3):
        
        self.l = l # Length of the vector
        
    def update(self):
        
        vec = self.i.data
        
        plt.close()
        plt.bar([1,2,3],vec)
        plt.show()
        
        
