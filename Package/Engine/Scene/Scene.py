
class Scene:

    def __init__(self) -> None:

        self.__Entities : list = []
        self.__GEObjects : list = []

    def loadScene(self, content : list) -> None : 
        for e in content : self.__Entities.append(e)

    def insertObj(self, obj : object) -> None : self.__Entities.append(obj)

    def insertGE(self, obj : object) -> None : self.__GEObjects.append(obj)

    def insertList(self, arr : list) -> None :
        for e in arr : self.__Entities.append(e)

    def getPlayer(self)   -> object : return self.__Entities[0]
    def getEntities(self) -> list   : return self.__Entities
    def getTextEntities(self)   -> list   : return self.__GEObjects