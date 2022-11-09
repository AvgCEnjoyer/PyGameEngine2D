from Engine.WorldObjects.Entity import Entity
import pygame

class Enemy(Entity):

    def __init__(self, x, y, w, h, v): 
        Entity.__init__(self, x = x, y = y, width = w, height = h, velocity=v)
        self.__hittable = True
        self.__customUpdateSet : str = [{}, []]

    def __del__(self) : pass

    def update(self): self.updateX(self.getVelocity())

    def updateCustom(self) : 

        for i in range(len(self.__customUpdateSet[1])):
            exec(self.__customUpdateSet[1][i], self.__customUpdateSet[0])

    def updateCustomClear(self) : self.__customUpdateSet = [{}, []]

    def updateCustomSet(self, events : list) : self.__customUpdateSet = events

    def collide(self, entity : Entity):

        rect = pygame.Rect(entity.getX(), entity.getY(), entity.getWidth(), entity.getHeight())
        rectOwn = pygame.Rect(self.getX(), self.getY(), self.getWidth(), self.getHeight())

        return rect.colliderect(rectOwn)