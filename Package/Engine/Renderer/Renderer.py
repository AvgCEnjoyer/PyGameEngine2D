
from msilib.schema import Error
from pygame import display
from pygame import draw
from Engine.Renderer.Color import *
from Engine.Scene.Scene import Scene


class Renderer:

    def __init__(self, screen : display = None) -> None : 
        self.display = screen


    def render(self, scene : Scene) -> None:

        for entity in scene.getTextEntities():
            entity.drawRect(self.display)
            entity.setFont()
            self.display.blit(entity.getFontText(),entity.getTextRect())

        for entity in scene.getEntities():
            try : 
                self.display.blit(entity.getTexture(), (entity.getX(), entity.getY(), entity.getWidth(), entity.getHeight()))
            except BaseException: 
                draw.rect(self.display, red, (entity.getX(), entity.getY(), entity.getWidth(), entity.getHeight()), 1)