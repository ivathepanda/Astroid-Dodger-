# Import Libraries

import pygame 
import random 
import sys 
from pygame.locals import*
from ship import* 


pygame.init()

screen_info = pygame.display.Info()


size = (width, height) = (int(screen_info.current_w),  int(screen_info.current_h)) 

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

color = (36, 38, 50)
screen.fill(color)

level_total = 4
current_level = 1
astroid_count = 3
Player = Ship((20,200))


def main(): 
  global color, current_level, level_total
  while current_level<=level_total: 
    clock.tick(60) # refreshing gamepage 
    
    for event in pygame.event.get(): 
      if event.type == QUIT: 
        sys.exit()
      if event.type == pygame.KEYDOWN: 
        
        if event.key == pygame.K_RIGHT: 
          Player.speed[0]=10
        if event.key == pygame.K_LEFT: 
          Player.speed[0]=-10 
        if event.key == pygame.K_UP: 
          Player.speed[1]=-10
        if event.key == pygame.K_DOWN: 
          Player.speed[1]=10
      # Key release 
      if event.type == pygame.KEYUP: 
        
        if event.key == pygame.K_RIGHT: 
          Player.speed[0]=0
        if event.key == pygame.K_LEFT: 
          Player.speed[0]=0 
        if event.key == pygame.K_UP: 
          Player.speed[1]=0
        if event.key == pygame.K_DOWN: 
          Player.speed[1]=0
    Player.update()
    screen.fill(color)
    screen.blit(Player.image, Player.rect)
    pygame.display.flip()

if __name__ == "__main__": 
  main()

