# beer_anim = pyganim.PygAnimation([('beer_pour0000.png', 100),
import sys
import pygame
from pygame.locals import *
import pyganim

pygame.init()
windowSurface = pygame.display.set_mode((427, 240), 0, 32)
pygame.display.set_caption("This is the beer you've been waiting for")

beer_animation = pyganim.PygAnimation(
    [(r"C:\Users\User\Downloads\bar-sim-main(1)\bar-sim-main\beer_prize\beer_pour0000.png", 100),
     (r"C:\Users\User\Downloads\bar-sim-main(1)\bar-sim-main\beer_prize\beer_pour0001.png", 100),
     (r"C:\Users\User\Downloads\bar-sim-main(1)\bar-sim-main\beer_prize\beer_pour0002.png", 100),
     (r"C:\Users\User\Downloads\bar-sim-main(1)\bar-sim-main\beer_prize\beer_pour0003.png", 100),
     (r"C:\Users\User\Downloads\bar-sim-main(1)\bar-sim-main\beer_prize\beer_pour0004.png", 100),
     (r"C:\Users\User\Downloads\bar-sim-main(1)\bar-sim-main\beer_prize\beer_pour0005.png", 100),
     (r"C:\Users\User\Downloads\bar-sim-main(1)\bar-sim-main\beer_prize\beer_pour0006.png", 100),
     (r"C:\Users\User\Downloads\bar-sim-main(1)\bar-sim-main\beer_prize\beer_pour0007.png", 100),
     (r"C:\Users\User\Downloads\bar-sim-main(1)\bar-sim-main\beer_prize\beer_pour0008.png", 100),
     (r"C:\Users\User\Downloads\bar-sim-main(1)\bar-sim-main\beer_prize\beer_pour0009.png", 100),
     (r"C:\Users\User\Downloads\bar-sim-main(1)\bar-sim-main\beer_prize\beer_pour0010.png", 100),
     (r"C:\Users\User\Downloads\bar-sim-main(1)\bar-sim-main\beer_prize\beer_pour0011.png", 100),
     (r"C:\Users\User\Downloads\bar-sim-main(1)\bar-sim-main\beer_prize\beer_pour0012.png", 100),
     (r"C:\Users\User\Downloads\bar-sim-main(1)\bar-sim-main\beer_prize\beer_pour0013.png", 100),
     (r"C:\Users\User\Downloads\bar-sim-main(1)\bar-sim-main\beer_prize\beer_pour0014.png", 100),
     (r"C:\Users\User\Downloads\bar-sim-main(1)\bar-sim-main\beer_prize\beer_pour0015.png", 100),
     (r"C:\Users\User\Downloads\bar-sim-main(1)\bar-sim-main\beer_prize\beer_pour0016.png", 100),
     (r"C:\Users\User\Downloads\bar-sim-main(1)\bar-sim-main\beer_prize\beer_pour0017.png", 100),
     (r"C:\Users\User\Downloads\bar-sim-main(1)\bar-sim-main\beer_prize\beer_pour0018.png", 100),
     (r"C:\Users\User\Downloads\bar-sim-main(1)\bar-sim-main\beer_prize\beer_pour0019.png", 100),
     (r"C:\Users\User\Downloads\bar-sim-main(1)\bar-sim-main\beer_prize\beer_pour0020.png", 100),
     (r"C:\Users\User\Downloads\bar-sim-main(1)\bar-sim-main\beer_prize\beer_pour0021.png", 100),
     (r"C:\Users\User\Downloads\bar-sim-main(1)\bar-sim-main\beer_prize\beer_pour0022.png", 100),
     (r"C:\Users\User\Downloads\bar-sim-main(1)\bar-sim-main\beer_prize\beer_pour0023.png", 100),
     (r"C:\Users\User\Downloads\bar-sim-main(1)\bar-sim-main\beer_prize\beer_pour0024.png", 100),
     (r"C:\Users\User\Downloads\bar-sim-main(1)\bar-sim-main\beer_prize\beer_pour0025.png", 100)])

beer_animation.play()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    beer_animation.blit(windowSurface, (0, 0))
    pygame.display.update()
