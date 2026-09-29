"""
Author : Tao Serveaux
Date : 28/09/26
"""

class Game:
    
    def __int__(self, maze, player):
        
        self.__victory = False
        
        self.__finishLine = self.getSpecificCase('G')
        
        self.__maze = maze
        self.__player = player
    
    def victory(self):
        
        if self.__player.getPos() == self.__finishLine :
            self.__victory = True
        
    def getSpecificCase(self, letter):
        
        for i in range(len(self.__maze)):
            for j in range(len(self.__maze)):
                if self.__maze[i][j] == letter :
                    return [i,j]
    
    def play(self):
        
        self.__player.setPos(self.getSpecificCase('S'))
        
        while not self.__victory :
            
            for i in self.__maze:
                print(i)
            
            self.victory()
            
            move = input("Which direction")
            
            if move == "d" :
                move = [1,0]
            elif move == "q" :
                move = [-1,0]
            elif move == "s":
                move = [0,1]
            elif move == "z":
                move = [0,-1]
            
            self.__player.nextMove(move)