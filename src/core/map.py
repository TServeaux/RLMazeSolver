"""
Author : Tao Serveaux
Date : 28/09/26
"""

import numpy as np

class Map:
    
    def __int__(self, width, height, nbObstacles):
        
        self.__width = width
        self.__height = height
        self.__nbObsctacles = nbObstacles
    
    def createRandomMaze(self):
        return
    
    def createStartEnd(self):
        return
    
    def testMaze(self):
        
        maze = [['S',0,0,'#',0,0,0,0,0,0,0],
                [0,'#',0,'#',0,'#','#','#',0,'#',0],
                [0,0,0,0,'#','#',0,0,0,'#',0],
                [0,'#','#','#','#','#',0,'#',0,'#',0],
                [0,0,0,0,0,0,0,'#',0,0,'G']]
        
        return maze