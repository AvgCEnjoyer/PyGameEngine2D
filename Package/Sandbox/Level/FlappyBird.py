from math import factorial
from Engine.Scene.Scene import Scene
from Engine.WorldObjects.Enemy import Enemy
from Engine.WorldObjects.Entity import Entity
from Engine.WorldObjects.GEObject import GEObject
from Engine.WorldObjects.Player import Player
from Engine.KeyHandle.KeyHandle import KeyHandle
from random import randint, random, choice
from pygame import *
import os


def level(event, instance):

    s = Scene()

    p = Player(x = 300, y = 300, w = 50, h = 50)

    s.insertObj(p)

    instance.keyHandle.setRestriction("w")
    instance.keyHandle.setRestriction("a")
    instance.keyHandle.setRestriction("s")
    instance.keyHandle.setRestriction("d")

    class scoreVar : 

        def __init__(self) : 
            self.val = 0
            self.paused = False
            self.text = "Score : " + str(self.val)
            self.label = GEObject(550, 100, 100, 50, "Score : 0")
        def incr(self) :
            if not self.paused: 
                self.val += 1
                self.text = "Score : " + str(self.val)
                self.label.setText(self.text)

    score = scoreVar()
    score.label.setFont()
    score.label.setText(score.text)
    s.insertGE(score.label)


    obstacles = []

    for i in range(100):

        randomVal = randint(0,200)
        factor = choice([-1,1])

        randomVal *= factor

        obst1 = Enemy(x = 850 + i * 600, y = 0 , w = 100, h = 400 + randomVal, v = 0)
        obstacles.append(obst1)
        s.insertObj(obst1)
        event.setEvent({"e" : obst1}, "e.updateX(-2)")
        event.setEvent({"e" : obst1, "score" : score}, "if e.getX() == 200 : score.incr()")
        #event.setEvent({"e" : obst1, "o" : obstacles}, "if e.getX() < -200 : o.remove(e)")

        obst2 = Enemy(x = 850 + i * 600, y = 400 + 350 + randomVal, w = 100, h = 900, v = 0)
        obstacles.append(obst2)
        s.insertObj(obst2)
        event.setEvent({"e" : obst2}, "e.updateX(-2)")
        #event.setEvent({"e" : obst2, "o" : obstacles}, "if e.getX() < -200 : o.remove(e)")


    def gameOver():
        gameover = GEObject(700, 400, 200, 100,centered=True,  text= "GAME OVER", fontSize=50)
        if gameover not in s.getTextEntities(): s.insertGE(gameover)

        instance.keyHandle.setRestriction("w")
        instance.keyHandle.setRestriction("a")
        instance.keyHandle.setRestriction("s")
        instance.keyHandle.setRestriction("d")
        instance.keyHandle.setRestriction(K_SPACE)

        if not score.paused : score.paused = True


    class grav:

        def __init__(self):
            self.gravity = False

        def gravCol(self):
            for obs in obstacles:
                if obs.collide(p):

                    gameOver()

                    self.gravity = True
                    return
            self.gravity = False

        def gravRun(self):
            if not self.gravity and not jumpy.isJumping: p.updateY(5)

        def gravityLoop(self):
            self.gravCol()
            self.gravRun()

    gravity = grav()

    event.setEvent({"grav" : gravity}, "grav.gravityLoop()")


    class jump:

        def __init__(self):
            self.isJumping = False
            self.jumpMax = 0

        def jump(self):
            if not self.isJumping : 
                self.isJumping = True
                self.jumpMax = p.getY() - 200
                instance.keyHandle.setRestriction(K_SPACE)

        def jumpLoop(self):
            if p.getY() > self.jumpMax and self.isJumping:
                p.updateY(-5)
            elif p.getY() <= self.jumpMax and self.isJumping:
                self.isJumping = False
                instance.keyHandle.clearRestriction(K_SPACE)
            
    jumpy = jump()

    instance.keyHandle.setKey(K_SPACE, jumpy.jump)

    event.setEvent({"jumpy" : jumpy}, "jumpy.jumpLoop()")


    event.setEvent({"p" : p, "go" : gameOver}, "if p.getY() > 900 or p.getY() < -50 : go()")

    
    return {"scene" : s, "player" : p}