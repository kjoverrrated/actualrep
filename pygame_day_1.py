

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
tutorialtextline = 1
tutorialtexts = ""
tutorial_file = open("tutorial.txt", "r")
listoflines = tutorial_file.readlines()
line = 0
characterpos = 50
stupidscreen = Actor("stupid.png", pos = (0,700))
linecasted = False
mathisinsession = False

#do i use actors for everything???maybe i make the math thing a class
#various actor creations
#cannot figure out how to make it simplified to ignore this
base = Actor("base.png", pos = (750,200))
one = Actor("1.png", pos = (600,220))
two = Actor("2.png", pos = (650,220))
three = Actor("3.png", pos = (700, 220))
four = Actor("4.png", pos = (750,220))
five = Actor("5.png", pos = (800,220))
six = Actor("6.png", pos = (600,260))
seven = Actor("7.png", pos = (650,260))
eight = Actor("8.png", pos = (700,260))
nine = Actor("9.png", pos = (750,260))
zero = Actor("0.png", pos = (800,260))
backspace = Actor("back.png", pos = (675, 300))
submit = Actor("submit.png", pos = (725, 300))

def on_mouse_down(pos, button): #button configuration 
  #calculates the distances for the mouse and the button
  global loading, tutorial, line, tutorialtexts, mathisinsession, linecasted
  startdistancesx = pos[0] - 575 
  startdistancesy = pos[1]- 335
  if tutorial == False and button == mouse.LEFT:
    if -190 < startdistancesx < 190 and  -40 < startdistancesy < 40: #if the user clicks the start button
      loading = True
    elif -190 < startdistancesx < 190 and  55 < startdistancesy < 130: #if the user clicks the settings
      print(str(startdistancesx) + " " + str(startdistancesy))
  if tutorial == True and button == mouse.LEFT and line < 8:
    
    if line == 2:
      linecasted = True
      line = 7
      clock.schedule_unique(mathzzzz,5)
    tutorialtext()
  if mathisinsession == True and button == mouse.RIGHT:
    tutorialtext()
  if 10 <= line <= 12:
    tutorialtext()
    




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
      





      
#----------------
def tutorialtext():
  global line, listoflines, tutorialtexts
  
  tutorialtexts = listoflines[line]
  line += 1





#--------------------------  
def draw():
  global loading, runfades, textfadedone, linecasted, mathisinsession
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
      screen.blit("fish.png", (-100,350))
      if line >= 1:
        draw_rect_alpha(surface, (0, 0, 255), (0, 500, WIDTH, HEIGHT))
        draw_rect_alpha(surface, (255,255,255), (0,485,WIDTH, 15))
        screen.draw.text(tutorialtexts, topleft = (40,500), color = (255,255,255), fontsize = 35)
      if linecasted == True:
        screen.blit("bobber.png", (WIDTH/2,375))
        if mathisinsession == True:
          screen.blit("exclamation.png", (500,200))
      if line >= 8:
        draw_rect_alpha(surface, (0, 0, 255), (0, 500, WIDTH, HEIGHT))
        draw_rect_alpha(surface, (255,255,255), (0,485,WIDTH, 15))
        screen.draw.text(tutorialtexts, topleft = (40,500), color = (255,255,255), fontsize = 35)
      
    
def mathzzzz():
  global mathisinsession, line
  mathisinsession = True
  line = 8
  tutorialtext()

def drawmaths():
    base.draw()
    one.draw()
    two.draw()
    three.draw()
    four.draw()
    five.draw()
    six.draw()
    seven.draw()
    eight.draw()
    nine.draw()
    zero.draw()
    backspace.draw()
    submit.draw()
pgzrun.go()



#todo list


#figure out how to make the math box pop up in random places

#figure out how to catch fish
#figure out how to do time to see how long their average was to figure out each question

#figure out how to make the math problems more difficult
#make the math problems like a popup ad where its like a blue screen and then math and depending on the mode, they can click the number buttons? should they type it in?

#just make a tutorial ig



#todo


#math popup...make the buttons
#make the fish graphic
#6 minute timer
#make a new function for fishing recreate tutorial
#do the display screen
#DONE
