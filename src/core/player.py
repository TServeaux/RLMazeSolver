"""
Author : Tao Serveaux
Date : 28/09/26
"""

class Player:
    
    def __int__(self, maze):
        
        super.__init__()
        
        self.__maze = maze
    
    def move(self, nextMove):
        
        if nextMove[0] == 0 or nextMove[0] == len(self.__maze) - 1:
            
            return "You can't go there, plz choose an another path"
        
        elif nextMove[1] == 0 or nextMove[1] == len(self.__maze[0]) - 1:
            
            return "You can't go there, plz choose an another path"
        
        elif self.__maze[nextMove[0]][nextMove[1]] == '#' :
            
            return "You can't go there, plz choose an another path"
        
        else :
            
            self.__maze[nextMove[0]][nextMove[1]] = 'P'
            self.__pos += nextMove
            

    def getPos(self):
        
        return self.__pos

    def setPos(self, pos):
        
        self.__pos = pos