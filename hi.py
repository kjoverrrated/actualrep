import pygame
import pgzrun
import numpy
WIDTH = 1000
HEIGHT = 600
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)


def draw():
  screen.blit("hello.png", (0,0))
  

def on_mouse_down(pos): #button configuration 
  #calculates the distances for the mouse and the button
  startdistancesx = pos[0] - 575 
  startdistancesy = pos[1]- 335
  
  if -190 < startdistancesx < 190 and  -40 < startdistancesy < 40: #if the user clicks the start button
    print(str(startdistancesx) + " " + str(startdistancesy))
  elif -190 < startdistancesx < 190 and  55 < startdistancesy < 130: #if the user clicks the settings
    print(str(startdistancesx) + " " + str(startdistancesy))


    
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
