#Pygame documentation
#https://www.pygame.org/docs/

import pygame
import os
import inputbox

img_dir = os.path.join('images')

pygame.init()

#REMEMBER to make the 'workspace' big enough so you can see the entire game window, or else the player will be cut off.

#clock for setting fps later
clock = pygame.time.Clock()

#window size 500 by 500 for now

win = pygame.display.set_mode((800, 500))

class Game:
  def __init__(self):
    pass
    
class Map(pygame.sprite.Sprite):
    def __init__(self, img, x, y, width, height): 
      pygame.sprite.Sprite.__init__(self)
      self.x = x
      self.y = y
      self.width = width
      self.height = height
      #Level the player will play in
      self.level = 0
      self.image = pygame.transform.scale(img, (self.width, self.height))
      #Gets rectangle with the dimensions of the image 
      self.rect = self.image.get_rect()
      self.rect.x = self.x
      self.rect.y = self.y
      backgrounds.add(self)

    def update(self):
      pass
      
      


#pygame.sprite.Sprite just give the Unit class access to all the built in pygame functions for sprites
import pygame
import os

class Unit(pygame.sprite.Sprite):
  def __init__(self, img, x, y, scale):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))
    self.rect = self.image.get_rect()
    #The offset is just to get things to align better
    self.rect.center = (x + 2, y + 2)
    #Adding to groups
    all_sprites.add(self)
    units.add(self)
    
  def update(self):
    pass

class Player(Unit):
  def __init__(self, img, x, y, scale):
  	Unit.__init__(self, img, x, y, scale)

		
  def update(self):
    self.controller()
		pass
      
  def controller(self):
		input_box1 = InputBox(100, 100, 140, 32)
		#e.g console input could be like: "player.move(left, 3)"

		
  def move(self, direction, distance):
    if direction == "left":
			self.rect.x += distance * 25
		elif direction == "right":
			self.rect.x -= distance * 25
		elif direction == "down":
			self.rect.y += distance * 25
		elif direction == "up":
			self.rect.y -= distance * 25
			
  def attack(self):
    pass
		
    
class Enemy(Unit):
  def __init__(self):
    pass

    
class Obstacle:
  def __init__(self):
    all_sprites.add(self)
    obstacles.add(self)

def main():
  
  
  run = True
  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

    #redraw background
    win.fill((255, 255, 255))
  
    all_sprites.update()
    backgrounds.draw(win)
    all_sprites.draw(win)
    pygame.display.update()
    
  pygame.quit()

#GROUPS

backgrounds = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
units = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


player = pygame.image.load(os.path.join(img_dir, "player.png")).convert()
map = pygame.image.load(os.path.join(img_dir, "map.png")).convert()

#creating instance of player object
P1 = Player(player, 325, 25, 1)
map = Map(map, 300, 0, 500, 500)

#Run the mainloop
if __name__ == "__main__":
  main()
