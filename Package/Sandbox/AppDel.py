import pygame
from pygame import display, event
from pygame import QUIT
from pygame import time
from pygame.display import update

from Sandbox.Runtime import initRuntime, runtime

class Game():
    
    #Do not change __init__
    def __init__(self, window : display) :

        self.window = window        
        self.gameState = 0
        self.run = True
        self.clock = time.Clock()

    def runGame(self) -> None:
        
        initRuntime(self.window)
        while self.run:

            events = event.get()
            for e in events:
                if e.type == QUIT:
                    self.run = False
            
            self.window.fill((0,0,0))

            runtime()


            self.clock.tick(144)
            update()
