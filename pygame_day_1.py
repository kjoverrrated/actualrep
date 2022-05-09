#i swear to god if this doesn't work in the morning
#replit is a liar it shouldve been working the whole time

import pygame
import pgzrun
import numpy
import time
#too tired but basically, you create a start and end time. the start time is set as soon as the math problem appears and te end time is when the math problem finishes.
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
stupidscreen = Actor("stupid.png", pos = (WIDTH/2,-HEIGHT/2))
linecasted = False
mathisinsession = False
mathtime = False
value = ""
whichmath = 0
equation = ""
answer = ""
mathcorrect = False
ifpopupvisible = False
mathtimestart = 0
mathtimeend = 0
mathtimetotal = 0
howmanyfish = 0
fishtime = False
fishanim = 0
tutorialdone = False
skiptutorial = False
bufferperiod = False

settings = False

timeleft = 10
endgame = False
usertime = 10
anime = -500
finaletext = 0
finaletextchecker = 0



#do i use actors for everything???maybe i make the math thing a class
#various actor creations
#cannot figure out how to make it simplified to ignore this
base = Actor("base.png", pos = (750,220))
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
darealfish = Actor("fishh.png", pos = (WIDTH/2, HEIGHT/2))
mathproblems = ["2 + 2 = ", "342 + 356 = ", "2 + 9 ", " 6 * 5 * 2 = ", "6^4 * 2 + 5 = ", "fifty-four plus five equals: ", "-1 + 2 = ", "9 * 45 = ", "4 * 9 + 3 * 6 + 2 / 4 - 4 + 2 = ", "3 + 1 + 2 / 1 + 2 * 6 = "]
mathanswers = ["4", "698", "11", "60", "2597" , "59", "1", "405", "53", "18"]




#average math time and fish caught

def on_mouse_down(pos, button): #button configuration 
  #calculates the distances for the mouse and the button
  global loading, tutorial, line, tutorialtexts, mathisinsession, linecasted, mathtime, value, equation, answer, mathcorrect, mathtimestart, mathtimeend, mathtimetotal, fishtime, tutorialdone, howmanyfish, ifpopupvisible, anime, finaletext, settings, usertime, timeleft, bufferperiod, skiptutorial
  
  startdistancesx = pos[0] - 575 
  startdistancesy = pos[1]- 335
  minusposx = pos[0] - WIDTH/2
  minusposy = pos[1] - HEIGHT/2
  
  if tutorial == False and button == mouse.LEFT and tutorialdone == False:
    if -190 < startdistancesx < 190 and  -40 < startdistancesy < 40 and settings == False: #if the user clicks the start button
      loading = True
      timeleft = usertime
    elif -190 < startdistancesx < 190 and  55 < startdistancesy < 130 and loading == False: #if the user clicks the settings
      settings = True
  if settings == True:
    if -250 < minusposx < -150 and -50 < minusposy < 50:
      if usertime != 10:
        usertime -= 10
    if 150 < minusposx < 250 and -50 < minusposy < 50:
      usertime += 10
    if -500 < minusposx < -400 and 270 < minusposy < 300:
      settings = False
    if 348 < minusposx < 374 and 272 < minusposy < 297:
      if skiptutorial == False:
        skiptutorial = True
      else:
        skiptutorial = False




      
  if tutorial == True and tutorialdone == False:
    if button == mouse.LEFT and line < 8:
      if line == 2:
        linecasted = True
        line = 7
        clock.schedule_unique(mathzzzz,5)
      tutorialtext()
    if mathisinsession == True and button == mouse.RIGHT and mathtime == False:#CHANGE THIS CHANGE CHANGE CHANGE CHANGE CHANGE CHANGE CHANGE CHANGE CHANGE CHANGE CHANGE CHANGE CHANGE CANGE
      tutorialtext()
      mathtime = True
    if 10 <= line <= 12:
      tutorialtext()
    #here we go the various math problems
    #math
    if line == 13:
      mathtimestart =  time.time()
      tutorialtext()
    if line == 21:
      tutorialtext()
      fishtime = True
    if mathtime == True:
      if line >= 13:
        if len(value) < 8:
          if one.collidepoint(pos):
            value += "1"
          if two.collidepoint(pos):
            value += "2"
          if three.collidepoint(pos):
            value += "3"
          if four.collidepoint(pos):
            value += "4"
          if five.collidepoint(pos):
            value += "5"
          if six.collidepoint(pos):
            value += "6"
          if seven.collidepoint(pos):
            value += "7"
          if eight.collidepoint(pos):
            value += "8"
          if nine.collidepoint(pos):
            value += "9"
          if zero.collidepoint(pos):
            value += "0"
        if backspace.collidepoint(pos):
            value = ""
        if submit.collidepoint(pos):
          if(answer == value):
            mathcorrect = True
            line = 20
            tutorialtext()
            mathtimeend = time.time()
            mathtimetotal = (round(mathtimeend - mathtimestart))
          else:
            line = 16
            tutorialtext()
            value = ""

    if fishtime == True and line != 28:
      tutorialtext()
      if line == 28:
        tutorialdone = True
        tutorial = False
        resetmath()
    
  #finally out of the tutorial
 
  if tutorialdone == True:
    if bufferperiod == True:
      if linecasted == False:
        linecasted = True
        clock.schedule_unique(mathzzzz, numpy.random.randint(5,15))
    bufferperiod = True
    if mathisinsession == True and button == mouse.RIGHT and mathtime == False:
      mathtime = True
      line = 34
    if line == 34:
      mathtimestart = time.time()
      tutorialtext()
    if fishtime == True:
      resetmath()
    if mathtime == True:
        if len(value) < 8:
          if one.collidepoint(pos):
            value += "1"
          if two.collidepoint(pos):
            value += "2"
          if three.collidepoint(pos):
            value += "3"
          if four.collidepoint(pos):
            value += "4"
          if five.collidepoint(pos):
            value += "5"
          if six.collidepoint(pos):
            value += "6"
          if seven.collidepoint(pos):
            value += "7"
          if eight.collidepoint(pos):
            value += "8"
          if nine.collidepoint(pos):
            value += "9"
          if zero.collidepoint(pos):
            value += "0"
        if backspace.collidepoint(pos):
            value = ""
        if submit.collidepoint(pos):
          if(answer == value):
            mathcorrect = True
            fishtime = True
            mathtimeend = time.time()
            mathtimetotal += (round(mathtimeend - mathtimestart))
            howmanyfish += 1
            value = ""
          else:
            value = ""  
    
    
      


def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)




def loadingscreen():
  global fadedone, loading, tutorial, skiptutorial, tutorialdone
  if fadedone == False:
    for alpha in range(0, 1275):
          #pygame.draw.rect(surface, (0,0,0,0), pygame.Rect(0, 0, WIDTH, HEIGHT))
          draw_rect_alpha(surface, (0, 0, 0, (alpha/5)), (0, 0, WIDTH, HEIGHT))
          pygame.display.flip()
          if alpha >= 255:
            fadedone = True
          if alpha >= 1200:
            tutorial = True
            if skiptutorial:
              tutorialdone = True
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
      if alphas >= 1200:
        fades = 1
    if fades == 1:
      textfadedone = True
      




def timerbecauseimlazy():
  global timeleft, endgame
  if timeleft > 0:
    timeleft -= 1
  if timeleft <= 0:
    endgame = True


      
#----------------
def tutorialtext():
  global line, listoflines, tutorialtexts, mathtime
  
  tutorialtexts = listoflines[line]
  line += 1



#--------------------------  
def draw():
  global loading, runfades, textfadedone, linecasted, mathisinsession, fishtime, ifpopupvisible, mathtimetotal, finaletextchecker
  
  
  if tutorial == False and settings == False:
    screen.blit("hello.png", (0,0))
  if settings == True:
    screen.fill((255,0,128))
    pygame.draw.circle(surface, (0), (300,HEIGHT/2), 50, 2)
    pygame.draw.circle(surface, (0), (700,HEIGHT/2), 50, 2)
    screen.draw.text("-", topleft = (292, HEIGHT/2-25), color = (0), fontsize = 70)
    screen.draw.text("+", topleft = (688, HEIGHT/2-27), color = (0), fontsize = 70)
    screen.draw.text("Amount of time \n increments of 10", center = (WIDTH/2, 170), color = (0), fontsize = 65)
    screen.draw.text("Back", topleft = (15, 575), color = (0), fontsize = 35)
    screen.draw.text(str(usertime), center = (WIDTH/2,HEIGHT/2), color = (0), fontsize = 55)
    screen.draw.text("Tutorial?", topright = (1000-15, 575), color = (0), fontsize = 35)
    if skiptutorial == False:
      pygame.draw.rect(surface, (0), (845, 570, 30,30 ), 2)
    if skiptutorial == True:
      pygame.draw.rect(surface, (0), (845, 570, 30,30 ))


      
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
        screen.draw.text(tutorialtexts, topleft = (40,520), color = (255,255,255), fontsize = 30)
      if linecasted == True:
        screen.blit("bobber.png", (WIDTH/2,375))
        if mathisinsession == True:
          screen.blit("exclamation.png", (500,200))
      if line >= 8:
        draw_rect_alpha(surface, (0, 0, 255), (0, 500, WIDTH, HEIGHT))
        draw_rect_alpha(surface, (255,255,255), (0,485,WIDTH, 15))
        screen.draw.text(tutorialtexts, topleft = (40,520), color = (255,255,255), fontsize = 30)
      if mathtime == True and fishtime == False:
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
        screen.draw.text(value, topleft = (580, 150), fontsize = 50)
        screen.draw.text(equation, topleft = (580, 100), fontsize = 65)

        
        if line == 21:
          screen.draw.text("Good job. You're one math wizard even though it took you " + str(mathtimetotal) + " seconds to answer.", topleft = (40,520), color = (255,255,255), fontsize = 30)
    if fishtime == True: 
      linecasted = False
      #clock.schedule_interval(fishanime, 0.25)
      darealfish.draw()
      mathtimetotal = 0


      
  if tutorialdone == True:
      screen.blit("pond.png", (0,0))
      screen.blit("fish.png", (-100,350))
      pygame.draw.circle(surface, (0), (885,75), 50)
      pygame.draw.arc(surface, (255), (840,30, 90,90), 0, numpy.radians(timeleft * (360 / usertime)), 45)
      clock.schedule_unique(timerbecauseimlazy, 1.0)
      
      if linecasted == True and fishtime == False:
        screen.blit("bobber.png", (WIDTH/2,375))
        
        if mathisinsession == True:
          screen.blit("exclamation.png", (500,200))
      if mathtime == True and fishtime == False:
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
        screen.draw.text(value, topleft = (580, 150), fontsize = 50)
        screen.draw.text(equation, topleft = (580, 100), fontsize = 65)
        ifpopupvisible = True
      if fishtime == True: 
        linecasted = False
        #clock.schedule_interval(fishanime, 0.25)
        darealfish.draw()
      if endgame == True and fishtime == False and mathtime == False and linecasted == False:
        stupidscreen.draw()
        screen.draw.text("Time to head home...", center = (WIDTH/2, HEIGHT/2), color = (255), fontsize = 50 )
        if finaletext == 0:
          clock.schedule(finalscreenyay, 0.01)
        if 0 < finaletext:
          screen.draw.text("Day 1", center = (WIDTH/2, 150), color = (255,255,255), fontsize = 75)
          finaletextchecker = 1.1
          clock.schedule_interval(magictrick, 2)
        if 1 < finaletext:
          screen.draw.text("complete", center = (WIDTH/2, 200), color = (255,255,255), fontsize = 50)
          finaletextchecker = 2.1
        if 2 < finaletext:
          screen.draw.text("Total Fish Caught: " + str(howmanyfish), center = (WIDTH/2, 250), color = (255,255,255), fontsize = 45)
          finaletextchecker = 3.1
        if 3 < finaletext:
          screen.draw.text("Total time it took for you to do math: " + str(mathtimetotal), center = (WIDTH/2, 300), color = (255,255,255), fontsize = 45)
          finaletextchecker = 4.1
        if 4 < finaletext:
          if mathtimetotal == 0 or howmanyfish == 0:
            screen.draw.text("What were you even doing? \n I can't even show your score because it gives me an error??", center = (WIDTH/2, 450), color = (255,255,255), fontsize = 40)
          elif (mathtimetotal / howmanyfish) < 5:
            screen.draw.text("You're either really good...or really bad \n Average time: " + str(mathtimetotal / howmanyfish), center = (WIDTH/2, 450), color = (255,255,255), fontsize = 40)
          elif (mathtimetotal / howmanyfish) < 10:
            screen.draw.text("Pretty good. \n Average time: " + str(mathtimetotal / howmanyfish), center = (WIDTH/2, 450), color = (255,255,255), fontsize = 40)
          elif (mathtimetotal / howmanyfish) < 15:
            screen.draw.text("meh. \n Average time: " + str(mathtimetotal / howmanyfish), center = (WIDTH/2, 450), color = (255,255,255), fontsize = 40)
          elif (mathtimetotal / howmanyfish) < 20:
            screen.draw.text("Not the best but... not the worst? \n Average time: " + str(mathtimetotal / howmanyfish), center = (WIDTH/2, 450), color = (255,255,255), fontsize = 40)
          elif (mathtimetotal / howmanyfish) > 30:
            screen.draw.text("Your math teachers have failed you. \n Average time: " + str(mathtimetotal / howmanyfish), center = (WIDTH/2, 450), color = (255,255,255), fontsize = 40)
      
          
        
        
def finalscreenyay():
  global anime, finaletext 
  if anime <= 295:
    anime += 5
    stupidscreen.y = anime
  else:
    finaletext = 1

def magictrick():
  global finaletext, finaletextchecker
  if finaletext != finaletextchecker:
    if finaletext <= finaletextchecker:
      finaletext += 0.1
  
def mathzzzz():
  global mathisinsession, line, tutorialdone
  mathisinsession = True
  
  mathproblem()
  
  if tutorialdone == False:
    line = 8
    tutorialtext()
    
def resetmath():
  global linecasted, mathisinsession, mathtime, value, whichmath, equation, answer, mathcorrect, ifpopupvisible, fishtime, mathtimestart, mathtimeend, endgame

  linecasted = False
  mathisinsession = False
  mathtime = False
  value = ""
  whichmath = 0
  equation = ""
  answer = ""
  mathcorrect = False
  ifpopupvisible = False
  fishtime = False
  mathtimestart = 0
  mathtimeend = 0



def mathproblem():
  global whichmath, mathproblems, equation, answer, mathanswers
  whichmath = numpy.random.randint(0,(len(mathproblems)))
  equation = mathproblems[whichmath]
  answer = mathanswers[whichmath]



def fishanime():
  global fishanim
  
  if fishanim == 0:
    darealfish.angle = -20
    fishanim = 1
  elif fishanim == 1:
    darealfish.angle = 20
    fishanim = 0



pgzrun.go()



#todo list


#figure out how to make the math box pop up in random places

#figure out how to catch fish
#figure out how to do time to see how long their average was to figure out each question

#figure out how to make the math problems more difficult
#make the math problems like a popup ad where its like a blue screen and then math and depending on the mode, they can click the number buttons? should they type it in?

#just make a tutorial ig



#todo
#SETTINGS TIME LEFT
#FADE OUT DISPLAY SCREEN

#math popup...make the buttons
#make the fish graphic
#6 minute timer
#make a new function for fishing recreate tutorial
#do the display screen
#DONE
