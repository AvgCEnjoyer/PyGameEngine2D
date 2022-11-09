import pygame

from Engine.WorldObjects.ECS.Texture import Texture, Animation

class Entity(Texture, Animation):

    def __init__(self, x : int = 5000, y : int = 5000, width : int = 50, height : int = 50, velocity : int = 0, texture : list or str = None) : 
        
        if type(texture) == list : Animation.__init__(texture)
        else : Texture.__init__(texture)
        self.__x = x
        self.__y = y
        self.__w = width
        self.__h = height
        self.__hittable = False
        self.__hitBox = [self.__x, self.__y, self.__w, self.__h]
        self.__velocity = velocity

    def getX(self)               -> int  : return self.__x
    def getY(self)               -> int  : return self.__y
    def getWidth(self)           -> int  : return self.__w
    def getHeight(self)          -> int  : return self.__h
    def getVelocity(self)        -> int  : return self.__velocity

    def isHittable(self)         -> bool : return self.__hittable
    def getHitbox(self)          -> list : return self.__hitBox

    def updateX(self, newX)      -> None : self.__x += newX
    def setX(self,newX)          -> None : self.__x  = newX
    def updateY(self, newY)      -> None : self.__y += newY
    def setY(self,newY)          -> None : self.__y  = newY
    def setWidth(self, newW)     -> None : self.__w  = newW
    def setHeight(self, newH)    -> None : self.__h  = newH
    def updateVelocity(self, V)  -> None : self.__velocity += V
    def setVeloctiy(self, V)     -> None : self.__velocity  = V