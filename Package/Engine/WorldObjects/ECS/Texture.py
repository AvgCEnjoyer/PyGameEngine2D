from pygame.image import load


class Texture: 

    def __init__(self, texturePath = None): 
        if texturePath != None : self.__texture = load(texturePath)

    def setTexture(self, texturePath : str) -> None: self.__texture = load(texturePath)

    def getTexture(self) : return self.__texture
    


class Animation: pass

