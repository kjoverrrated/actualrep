

import pygame
import pgzrun
import numpy
WIDTH = 1000
HEIGHT = 600
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
loading = False
surface = pygame.display.set_mode((WIDTH,HEIGHT), pygame.SRCALPHA)
fadedone = False
tutorial = False
fades = 0
runfades = False
textfadedone = False
def on_mouse_down(pos): #button configuration 
  #calculates the distances for the mouse and the button
  global loading
  startdistancesx = pos[0] - 575 
  startdistancesy = pos[1]- 335
  
  if -190 < startdistancesx < 190 and  -40 < startdistancesy < 40: #if the user clicks the start button
    loading = True
  elif -190 < startdistancesx < 190 and  55 < startdistancesy < 130: #if the user clicks the settings
    print(str(startdistancesx) + " " + str(startdistancesy))

def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)




def loadingscreen():
  global fadedone, loading, tutorial
  if fadedone == False:
    for alpha in range(0, 1275):
          #pygame.draw.rect(surface, (0,0,0,0), pygame.Rect(0, 0, WIDTH, HEIGHT))
          draw_rect_alpha(surface, (0, 0, 0, (alpha/5)), (0, 0, WIDTH, HEIGHT))
          print(alpha)
          pygame.display.flip()
          if alpha >= 255:
            fadedone = True
          if alpha >= 1200:
            tutorial = True
  if fadedone == True:
    loading = False
    
    draw_rect_alpha(surface, (0, 0, 0, 255), (0, 0, WIDTH, HEIGHT))
    screen.draw.text("loading...", center = (WIDTH/2, HEIGHT/2), color = (255,255,255))



def fadess():
  global tutorial, fades, runfades, textfadedone
  runfades = True
  if tutorial == True:
    for alphas in range(0, 1275):
      draw_rect_alpha(surface, (0, 0, 255, (alphas/5)), (0, 500, WIDTH, HEIGHT))
      print(alphas)
      if alphas >= 1200:
        fades = 1
    if fades == 1:
      textfadedone = True






  
def draw():
  global loading, runfades, textfadedone
  if tutorial == False:
    screen.blit("hello.png", (0,0))
 
  if loading == True:
    clock.schedule_unique(loadingscreen, 1)
  if tutorial == True:
    screen.blit("pond.png", (0,0))
    if textfadedone == False:
      clock.schedule_unique(fadess, 3)
    if runfades == True and textfadedone == False:
      fadess()
    if textfadedone == True:
      draw_rect_alpha(surface, (0, 0, 255), (0, 500, WIDTH, HEIGHT))
      draw_rect_alpha(surface, (255,255,255), (0,485,WIDTH, 15))
    




pgzrun.go()



#todo list

#figure out how to fade to a tutorial and make it like a letter by letter appearance
#figure out how to make the math box pop up in random places
#figure out how to let the user control the fishing rod
#figure out how to catch fish
#figure out how to do time to see how long their average was to figure out each question
#is that it?
#figure out how to make the math problems more difficult
#make the math problems like a popup ad where its like a blue screen and then math and depending on the mode, they can click the number buttons? should they type it in?
#figure out how to show the sky getting like night time
#just make a tutorial ig
