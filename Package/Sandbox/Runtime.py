from pygame import display
from Engine.Renderer.Renderer import Renderer
from Engine.Scene.Scene import Scene
from Sandbox.Level.Level1 import *
from Engine.KeyHandle.KeyHandle import KeyHandle
from Engine.Event.EventHandle import EventHandle


class RunTime:
    def __init__(self):

        self.event : EventHandle   = EventHandle()
        self.renderer  : Renderer  = Renderer()
        self.keyHandle : KeyHandle = KeyHandle()
        self.mainScene : Scene     = mainMenu(self.event, self)["scene"]

    def run(self) : 

        self.__render()
        self.__runKeyHandle()
        self.__runEvent()

    def updateLevel(self, func) -> None: 
        
        self.keyHandle.clearAllContent()
        data : dict         = func(self.event, self)
        self.mainScene      = data["scene"]
        self.keyHandle.pawn = data["player"]

    def __render(self)      -> None : self.renderer.render(self.mainScene)
    def __runKeyHandle(self)-> None : self.keyHandle.run()
    def __runEvent(self)    -> None : self.event.run()

    
rt = RunTime()

def initRuntime(display) -> None:

    rt.renderer.display = display
    rt.keyHandle.pawn = rt.mainScene.getPlayer()

def runtime():

    rt.run()