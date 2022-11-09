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
    instance.keyHandle.setRestriction("s")

    obstacles = []

    obst1 = Enemy(x = 150, y = 350, w = 400, h = 300, v = 0)
    obstacles.append(obst1)
    s.insertObj(obst1)

    class grav:

        def __init__(self):
            self.gravity = False

        def gravCol(self):
            for obs in obstacles:
                if obs.collide(p):
                    self.gravity = True
                    return
            self.gravity = False

        def gravRun(self):
            if not self.gravity and not jumpy.isJumping: p.updateY(4)

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
                self.jumpMax = p.getY() - 20

        def jumpLoop(self):
            if p.getY() > self.jumpMax and self.isJumping:
                p.updateY(-4)
            elif p.getY() <= self.jumpMax and self.isJumping:
                self.isJumping = False
            
    jumpy = jump()

    instance.keyHandle.setKey(K_SPACE, jumpy.jump)

    event.setEvent({"jumpy" : jumpy}, "jumpy.jumpLoop()")
    
    return {"scene" : s, "player" : p}