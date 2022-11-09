from struct import pack
from Engine.Scene.Scene import Scene
from Engine.WorldObjects.Enemy import Enemy
from Engine.WorldObjects.Entity import Entity
from Engine.WorldObjects.GEObject import GEObject
from Engine.WorldObjects.Player import Player
from Engine.KeyHandle.KeyHandle import KeyHandle
from random import randint, random, choice
from pygame import *
import os
#from CrackMania2.Level.hookTest import level
from Sandbox.Level.FlappyBird import level

class Level:

    def __init__(self):
        self.active = 1

def level1(event, instance) -> dict: 

    event.clear()

    s = Scene()

    p = Player()
    p.setX(150)

    p.setWidth(120)
    p.setHeight(70)
    #p.setTexture(os.path.join('CrackMania2/Level/Sprites', 'Player_Dragon_Normal_1.png'))

    event.setEvent({"p" : p}, "if p.getY() < 150 : p.setY(600)")
    event.setEvent({"p" : p}, "if p.getY() > 650 : p.setY(200)")

    instance.keyHandle.setRestriction("a")
    instance.keyHandle.setRestriction("d")

    s.insertObj(p)

    shot = Enemy(-200,-200, 30,30, 10)
    s.insertObj(shot)
    event.setEvent({"shot" : shot}, "shot.update()")

    class scoreVar : 
        def __init__(self) : 
            self.val = 0
            self.text = "Score : " + str(self.val)
        def incr(self) : 
            self.val += 1
            self.text = "Score : " + str(self.val)

    var = scoreVar()

    def goToMainMenu():
        instance.updateLevel(mainMenu)

    borderUp = GEObject(0,0,1600,150, False)
    borderLow = GEObject(0,750,1600,150, False)
    s.insertGE(borderUp)
    s.insertGE(borderLow)

    score = GEObject(550, 100, 0, 0, text="Score : 0", bgColor=(0,0,0), fontColor=(255,255,255), fontSize=40)
    score.setFont()
    s.insertGE(score)

    hearts = [Entity(30,30, 50, 50), Entity(130,30, 50, 50), Entity(230,30, 50, 50)]
    for i in range(3): s.insertObj(hearts[i])
    
    def removeHeart() :
        hearts[len(hearts)-1].setY(-1200) 
        hearts.remove(hearts[len(hearts)-1])

    event.setEvent({"h" : hearts, "gtMm" : goToMainMenu}, "if len(h) == 0 : gtMm()")

    def shoot():
        shot.setX(p.getX())
        shot.setY(p.getY())
        instance.keyHandle.setRestriction(K_RIGHT)
    def reset(obj = None):
        if obj != None : 
            obj.setY(-1600)
            var.incr()
            score.setText(var.text)
        shot.setY(-200)
        instance.keyHandle.clearRestriction(K_RIGHT) 
    

    instance.keyHandle.setKey(K_RIGHT, shoot)
    instance.keyHandle.setKey(K_ESCAPE, goToMainMenu)

    for _ in range(20):
        e = Enemy(randint(2000,10000), randint(250,500), 50, 50, -2)
        s.insertObj(e)
        event.setEvent({"e" : e}, "e.update()")
        event.setEvent({"e" : e, "randint" : randint}, "if e.getX() < -60 : e.setX(randint(2000,3000))")
        event.setEvent({"e" : e, "randint" : randint}, "if e.getX() < -60 : e.setY(randint(150,600))")
        event.setEvent({"e" : e, "p" : p, "rH" : removeHeart}, "if e.collide(p) : rH()")
        event.setEvent({"e" : e, "p" : p, "rH" : removeHeart}, "if e.collide(p) : e.setX(-1200)")
        event.setEvent({"e" : e, "shot" : shot, "reset" : reset}, "if e.collide(shot) : reset(e)")
        event.setEvent({"shot" : shot, "reset" : reset}, "if shot.getX() > 1620 : reset()")

    return {"scene" : s, "player" : p}


def level2(event, instance) -> dict: 

    event.clear()

    s = Scene()

    p = Player()
    p.setX(100)
    p.setWidth(120)
    p.setHeight(70)
    p.setTexture(os.path.join('CrackMania2/Level/Sprites', 'Player_Dragon_Normal_1.png'))
    event.setEvent({"p" : p}, "if p.getY() < 150 : p.setY(600)")
    event.setEvent({"p" : p}, "if p.getY() > 650 : p.setY(200)")

    s.insertObj(p)

    instance.keyHandle.setRestriction("a")
    instance.keyHandle.setRestriction("d")

    score = GEObject(550, 100, 50, 100, "Score : 0")
    score.font((0,0,0), (0,0,0))

    class scoreVar : 
        def __init__(self) : 
            self.val = 0
            self.text = "Score : " + str(self.val)
        def incr(self) : 
            self.val += 1
            self.text = "Score : " + str(self.val)

    var = scoreVar()

    s.insertGE(score)

    for i in range(100):
        ranVar = randint(150,600)
        e = Enemy(1000 + i * 600, ranVar, 100, 100, 0)

        partialEvents = []
        if ranVar < 375 : partialEvents.append("if e.getY() < 600 and e.getX() - p.getX() < 300 : e.updateY(2)")
        if ranVar >= 375 : partialEvents.append("if e.getY() > 150 and e.getX() - p.getX() < 300 : e.updateY(-2)")
        partialEvents.append("e.updateX(-2)")
        e.updateCustomSet([{"e" : e, "p" : p}, partialEvents])

        event.setEvent({"e" : e}, "e.updateCustom()")
        event.setEvent({"e" : e, "p" : p, "i" : instance, "level2" : level2}, "if e.collide(p) : i.updateLevel(level2)")
        event.setEvent({"s" : var, "e" : e, "p" : p}, "if p.getX() == e.getX() + e.getWidth() : s.incr()")
        event.setEvent({"score" : score, "scoreVar" : var, "e" : e, "p" : p}, "if p.getX() == e.getX() + e.getWidth() : score.setText(scoreVar.text)")
        s.insertObj(e)



    return {"scene" : s, "player" : p}


def level3(event, instance) -> dict:

    s = Scene()

    p = Player()
    p.setX(750)
    p.setY(400)
    p.setWidth(100)
    p.setHeight(100)
    p.setVeloctiy(10)

    s.insertObj(p)

    instance.keyHandle.setRestriction("w")
    instance.keyHandle.setRestriction("a")
    instance.keyHandle.setRestriction("s")
    instance.keyHandle.setRestriction("d")

    
    class Timer:

        def __init__(self):
            self.t = 0
            self.interval = 3
            self.stamp = 144 * self.interval
            self.state = 0
        def incr(self):
            self.t += 1
            if self.t == self.interval * 144 - 100:
                self.state = 2
        def getActive(self):
            if self.stamp - self.t <= 0:
                self.t = 0
                if self.interval == 1 : 
                    self.interval = 3
                    self.state = 0

                    var.incr()
                    score.setText(var.text) 

                else : 
                    self.interval = 1
                    self.state = 1
                self.stamp = 144 * self.interval 
                return True
            return False

    class currentKey:

        def __init__(self):
            self.key = 1

        def generateKey(self):
            self.key = choice([0,1])

    class scoreVar : 

        def __init__(self) : 
            self.val = 0
            self.text = "Score : " + str(self.val)
        def incr(self) : 
            self.val += 1
            self.text = "Score : " + str(self.val)

    var = scoreVar()

    score = GEObject(550, 100, 100, 50, "Score : 0")
    score.setFont()
    score.setText(var.text)
    s.insertGE(score)

    def updateE(obj, timer):
        if timer.getActive() :
            if key.key == 0:
                if e.getHeight() < 890: e.setHeight(900)
                else :
                    e.setHeight(50)
                    key.generateKey()

            elif key.key == 1:
                if w.getWidth() < 1590: w.setWidth(1600)
                else : 
                    w.setWidth(50)
                    key.generateKey()

    def updateQE(timer, label, y, _key, rest):
        if timer.state == 2:
            if key.key == _key : 
                label.setY(y)
                instance.keyHandle.clearRestriction(rest)
            else:
                instance.keyHandle.setRestriction(rest)

        if timer.state == 0:
            p.setX(750)
            p.setY(400)
            label.setY(-1200)
            
            

    timer = Timer()
    key = currentKey()

    e = Enemy(799, 0, 2, 100, 0)
    w = Enemy(0, 449, 50, 2, 0)

    labelLeft = Enemy(300, -1200, 50, 50, 0)
    labelRight = Enemy(1250, -1200, 50, 50, 0)
    labelUp = Enemy(775, -1200, 50, 50, 0)
    labelLow = Enemy(775, -1200, 50, 50, 0)

    s.insertObj(e)
    s.insertObj(w)
    s.insertObj(labelLeft)
    s.insertObj(labelRight)
    s.insertObj(labelUp)
    s.insertObj(labelLow)

    event.setEvent({"timer" : timer, "e" : e, "update" : updateE}, "update(e, timer)")

    event.setEvent({"e" : e, "p" : p, "instance" : instance, "mainMenu" : mainMenu}, "if e.collide(p) : instance.updateLevel(mainMenu)")
    event.setEvent({"e" : w, "p" : p, "instance" : instance, "mainMenu" : mainMenu}, "if e.collide(p) : instance.updateLevel(mainMenu)")
    
    event.setEvent({"timer" : timer}, "timer.incr()")
    event.setEvent({"L" : labelLeft, "func" : updateQE, "timer" : timer, "key" : key}, "func(timer, L, 450, 0, 'a')")
    event.setEvent({"L" : labelRight, "func" : updateQE, "timer" : timer, "key" : key}, "func(timer, L, 450, 0, 'd')")
    event.setEvent({"L" : labelUp, "func" : updateQE, "timer" : timer, "key" : key}, "func(timer, L, 200, 1, 'w')")
    event.setEvent({"L" : labelLow, "func" : updateQE, "timer" : timer, "key" : key}, "func(timer, L, 700, 1, 's')")


    return {"scene" : s, "player" : p}


def mainMenu(event, instance) -> dict:

    event.clear() 

    s = Scene()

    p = Player()
    
    p.setX(-1000)

    s.insertObj(p)

    instance.keyHandle.setRestriction("w")
    instance.keyHandle.setRestriction("a")
    instance.keyHandle.setRestriction("s")
    instance.keyHandle.setRestriction("d")
    
    newGame = GEObject(800,200,100,50,True,"Neues Spiel")
    options = GEObject(800,300,100,50,True,"Optionen")
    score = GEObject(800,400,100,50,True,"Bestenliste")

    s.insertGE(newGame)
    s.insertGE(options)
    s.insertGE(score)

    event.setEvent({"newGame" : newGame, "instance" : instance, "level1" : level}, "if newGame.onClick() : instance.updateLevel(level1) ")
    event.setEvent({"options" : options }, "if options.onClick() : print(options.getText()) ")
    event.setEvent({"score" : score }, "if score.onClick() : print(score.getText()) ")

    return {"scene" : s, "player" : p}