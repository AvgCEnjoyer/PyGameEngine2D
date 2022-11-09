

class EventHandle:

    def __init__(self):

        self.__blocked      : bool = False
        self.__types        : dict = {}
        self.__activeEvents : list = []     #Schema : [{Benutzte FremdObjekte}, StringFunktion]

    def requestEvent(type : str) : pass

    def clear(self): self.__activeEvents.clear()

    def setEvent(self, actors : list, restriction : str) : 

        self.__activeEvents.append([actors, restriction])

    def clearEvent(self, event) : self.__activeEvents.remove(event)

    def run(self):

        for event in self.__activeEvents:
            exec(event[1], event[0])