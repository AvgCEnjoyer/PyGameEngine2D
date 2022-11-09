from Engine.StartUp.BootUp import bootUp
from Sandbox.AppDel import Game


def init(): 
    
    c = bootUp(1600, 900)
    game = Game(c["window"])
    game.runGame()