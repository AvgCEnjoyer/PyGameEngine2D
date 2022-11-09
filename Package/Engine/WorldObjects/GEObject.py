from Engine.WorldObjects.Entity import Entity
import pygame

pygame.init()

class GEObject (Entity) :

    def __init__(self, x : int = 800 , y : int = 200 , w : int = 100, h : int = 100, centered : bool = False, text : str = "", fontColor : tuple = (0,0,0), bgColor : tuple = (255,255,255), fontSize : int = 20 ):           
        Entity.__init__(self, x = x, y = y, width = w, height = h, velocity=5)
        self.__text : str = text
        self.__fontSize : int = fontSize
        self.__font = pygame.font.Font('freesansbold.ttf', self.__fontSize)
        self.__fontText = 0
        self.__textRect = 0
        self.__state : bool = False
        self.__fontColor : tuple = fontColor
        self.__backgroundColor : tuple = bgColor
        self.__centered : bool = centered
        self.time = 144
        
    def getText(self)                    -> str : return self.__text
    def getFunc(self)                        : return self.__func
    def getFontText(self)                           : return self.__fontText
    def getTextRect(self)                           : return self.__textRect
    def getState(self)                   -> bool     : return self.__state
    def getFontColor(self)               -> tuple    : return self.__fontColor
    def getBgColor(self)                 -> tuple     : return self.__backgroundColor
    def getFontSize(self)                -> int       : return self.__fontSize
    def getCentered(self)                -> bool      : return self.__centered

    def setText(self, text : str)             -> None : self.__text = text
    def setFunc(self, func )        -> None : self.__func = func
    def setState(self, state : bool)          -> None : self.__state = state
    def setFontColor(self, fontColor : tuple) -> None : self.__fontColor = fontColor
    def setBgColor(self, bgColor : tuple)     -> None : self.__bgColor = bgColor
    def setFontSize(self, fontSize : int)     -> None : self.__fontSize = fontSize
    def setCentered(self, centerState : bool) -> None : self.__centered = centerState

    def onClick(self) -> bool:
        pos : list = pygame.mouse.get_pos()
        if self.time != 0:
            self.time = self.time - 1
        #print(self.time)
         
        ev = pygame.event.get()
        if pygame.mouse.get_pressed()[0] :
            if pos[0] > self.getX() - self.getWidth() // 2 and pos[0] < self.getX() + self.getWidth() // 2:
                if  pos[1] > self.getY() - self.getHeight() // 2 and pos[1] < self.getY() + self.getHeight() // 2:
                    if pygame.mouse.get_pressed() == (1,0,0) and self.time == 0:
                        self.time = 144
                        return True
        
        
    def setFont(self) -> None:
        self.__fontText = self.__font.render(self.__text , True, self.getFontColor(), self.getBgColor())
        self.__textRect = self.__fontText.get_rect(center=(self.getX() ,self.getY()))

    def drawRect(self, display) -> None:
        if self.getCentered():
            pygame.draw.rect(display, self.getBgColor(), (self.getX() - (self.getWidth() // 2), self.getY() - (self.getHeight() // 2), self.getWidth(), self.getHeight()))
        elif not self.getCentered(): 
            pygame.draw.rect(display, self.getBgColor(), (self.getX(), self.getY(), self.getWidth(), self.getHeight()))