import pygame,random,sys
from pygame.locals import *

class fruit (pygame.sprite.Sprite):
  def __init__(self,fruitImg,x,y):
    self.fruitImg = pygame.image.load(fruitImg).convert()
    self.fruitImg.set_colorkey((0,0,0))
    self.X = x
    self.Y = y
    self.weight = 0
    self.transparent = (0,0,0,0)
    self.moving = False
    self.score = 0
    self.rect_Img = self.fruitImg.get_rect()
    self.numberOfFruits = 3

  def Draw(self):
    for i in range(0,self.numberOfFruits):
      #define numberOfFruits as something that changes depending on the level and this loop should work
      x = random.randint(0,800)
      y = random.randint(0,533)
      screen.blit(self.fruitImg,(x,y) )#(self.X,self.Y))

