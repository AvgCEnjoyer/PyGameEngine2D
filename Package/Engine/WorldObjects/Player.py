from Engine.WorldObjects.Entity import Entity


class Player (Entity) :

    def __init__(self, x : int = 100, y : int = 100, h : int = 50, w : int = 50):
        Entity.__init__(self, x = x, y = y, width = w, height = h, velocity=5)
        self.__hittable = True