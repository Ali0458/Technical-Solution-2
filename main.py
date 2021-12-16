import pygame,random,sys,math
from fruit import *
#from pygame.locals import *
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
    self.xRand = random.randint(0,display_width)
    self.yRand = random.randint(0, display_height)
    self.speed = 1

  def Draw(self):
        screen.blit(self.fruitImg,(self.xRand,self.yRand)) #(self.X,self.Y))
        print(self.xRand,self.yRand)


  def move(self):
      self.xRand += self.speed

#Projectile motion

#window
display_width= 800
display_height = 533
screen = pygame.display.set_mode((display_width,display_height))


#all_sprites = pygame.sprite.Group()
x = fruit('strawberry.png',50,50)
p = fruit('strawberry.png',50,50)
q = fruit('strawberry.png',50,50)
#all_sprites.add(x)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    x.Draw()
    p.Draw()
    q.Draw()
    q.move()
    #all_sprites.draw(screen)
    # Drawing all sprites
    #for entity in all_sprites:
        #screen.blit(entity.fruitImg, entity.rect_Img)

    pygame.display.update()
