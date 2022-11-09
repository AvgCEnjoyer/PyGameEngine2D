from pygame import *

class KeyHandle:

    def __init__(self, pawn : object = None) :
        self.pawn = pawn

        self.__restrictions : list     = []
        self.__cKeys        : list     = []
        self.__cEventFunc   : list     = []

    def run(self) -> None:
        
        keys=key.get_pressed()
        if keys[K_w]   and "w" not in self.__restrictions : self.pawn.updateY(-self.pawn.getVelocity())
            
        elif keys[K_s] and "s" not in self.__restrictions : self.pawn.updateY(self.pawn.getVelocity())
            
        if keys[K_a]   and "a" not in self.__restrictions : self.pawn.updateX(-self.pawn.getVelocity())

        elif keys[K_d] and "d" not in self.__restrictions : self.pawn.updateX(self.pawn.getVelocity())

        for i in range(len(self.__cKeys)):
            if(keys[self.__cKeys[i]]) and self.__cKeys[i] not in self.__restrictions : self.__cEventFunc[i]() 

    def setRestriction(self, button : str) : 
        if button not in self.__restrictions : self.__restrictions.append(button)

    def clearRestriction(self, button : str) : 
        if button in self.__restrictions : 
            self.__restrictions.remove(button)


    def clearAllRestrictions(self) : self.__restrictions.clear()

    def setKey(self, key : key , func) : 
        self.__cKeys.append(key)
        self.__cEventFunc.append(func)

    def clearAllContent(self) :
        self.__restrictions.clear()
        self.__cKeys.clear()
        self.__cEventFunc.clear()