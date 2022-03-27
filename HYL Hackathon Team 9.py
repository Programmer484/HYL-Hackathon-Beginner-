#Pygame documentation
#https://www.pygame.org/docs/

import pygame
import os
import inputbox as ib

global total

from tkinter import *
from tkinter import ttk
n = ttk.Notebook()
f1= ttk.Frame(n)
f2= ttk.Frame(n)
f3= ttk.Frame(n)
f4= ttk.Frame(n)


window= ttk.Frame(n)


def main1(n):
    global total
    n.add(f1, text="1")
    n.add(f2, text="2")
    n.add(f3, text="3")
    n.add(f4, text="4")


    total= ttk.Label(window, text="0")


    Label(f2, text='''Move character to green square using move commands.\n E.g. self.move("right", 3) will move character 3 squares right''').grid(row=2,column=2)
    Button(f2, text="Placeholder",command=incorrect2).grid(row=3,column=1)
    Button(f2, text="Placeholder", command=correct2).grid(row=3,column=2)
    Button(f2, text="Placeholder", command=incorrect2).grid(row=3,column=3)

    Label(f3, text="Placeholder").grid(row=2,column=2)
    Button(f3, text="Placeholder",command=incorrect3).grid(row=3,column=1)
    Button(f3, text="Placeholder", command=correct3).grid(row=3,column=2)
    Button(f3, text="Placeholder", command=incorrect3).grid(row=3,column=3)

    Label(f4, text="Placeholder").grid(row=2,column=2)
    Button(f4, text="Placeholder",command=correct4).grid(row=3,column=1)
    Button(f4, text="Placeholder", command=incorrect4).grid(row=3,column=2)
    Button(f4, text="Placeholder", command=incorrect4).grid(row=3,column=3)


    return total



def correct():
    global total
    Label(f1, text="Correct").grid(row=1,column=2)
    counter()
def incorrect():
    Label(f1, text="Incorrect").grid(row=1,column=2)

def correct2():
    global total
    Label(f2, text="Correct").grid(row=1,column=2)
    counter()

def incorrect2():
    Label(f2, text="Incorrect").grid(row=1,column=2)

def correct3():
    global total
    Label(f3, text="Correct").grid(row=1,column=2)
    counter()

def incorrect3():
    Label(f3, text="Incorrect").grid(row=1,column=2)

def correct4():
    global total
    Label(f4, text="Correct").grid(row=1,column=2)
    counter()

def incorrect4():
    Label(f4, text="Incorrect").grid(row=1,column=2)


def counter():
    global total
    total['text'] = str(int(total['text']) + 1)


main1(n)

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
  def __init__(self, img, x, y, scale, input):
    Unit.__init__(self, img, x, y, scale)
    self.input = input

		
  def update(self):
    pass
      
  def controller(self, event):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RETURN:
        exec(self.input.text)
      elif event.key == pygame.K_1:

        n.pack()
        n.mainloop()
    #e.g console input could be like: "player.move(left, 3)"

		
  def move(self, direction, distance):
    if direction == "left":
      self.rect.x -= distance * 50
    elif direction == "right":
      self.rect.x += distance * 50
    elif direction == "up":
      self.rect.y -= distance * 50
    elif direction == "down":
      self.rect.y += distance * 50
   
    			
  def attack(self):
    print("attack!")
		
    
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
      for box in input_boxes:
          box.handle_event(event)
      P1.controller(event)

      
    win.fill((255, 255, 255))
  
    all_sprites.update()
    backgrounds.draw(win)
    all_sprites.draw(win)

    for box in input_boxes:
        box.update()
    for box in input_boxes:
        box.draw(win)

    pygame.display.flip()
    
  pygame.quit()

#GROUPS

backgrounds = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
units = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


player = pygame.image.load(os.path.join(img_dir, "player.png")).convert()
map = pygame.image.load(os.path.join(img_dir, "map.png")).convert()

#creating instance of player object
input_box1 = ib.InputBox(0, 0, 0, 32)
input_boxes = [input_box1]
P1 = Player(player, 325, 25, 1, input_box1)
map = Map(map, 300, 0, 500, 500)

#Run the mainloop
if __name__ == "__main__":
  main()
  
