import pygame
import pgzrun
import numpy
WIDTH = 1000
HEIGHT = 600
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)


def draw():
  screen.blit("hello.png", (0,0))

def on_mouse_down(pos):

  distances = numpy.math.hypot(pos.x - 581,337 - 337)
  print(distances)
pgzrun.go()