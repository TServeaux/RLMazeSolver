"""
Author : Tao Serveaux
Date : 29/09/26
"""

from src.core.player import Player
from src.core.game import Game
from src.core.map import Map

if __name__ == "__main__":

    maze = Map().testMaze()
    plr = Player(maze).setPos()
    game = Game(maze,).play()