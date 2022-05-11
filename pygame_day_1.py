#i swear to god if this doesn't work in the morning
#replit is a liar it shouldve been working the whole time

import pygame
import pgzrun
import numpy
import time

#--------Necessities--------
WIDTH = 1000
HEIGHT = 600
pygame.font.init()
surface = pygame.display.set_mode((WIDTH,HEIGHT), pygame.SRCALPHA)


#--------PreGame--------
loading = False #if game is about to start
fadedone = False #if the lake is in view
tutorial = False #tutorial?
fades = 0 #stops the fade
runfades = False #runs the fades
textfadedone = False #if the fade is done

#--------Tutorial Text--------
tutorialtexts = "" #stores the text we're on
tutorial_file = open("tutorial.txt", "r") #opens the tutorial script
listoflines = tutorial_file.readlines() #reads the lines
line = 0 #gets the line we need from the file



#--------The Game--------
linecasted = False #user fishing
mathisinsession = False #is there math
mathtime = False #time to do math
value = "" #user input value
whichmath = 0 #which equation we're using
equation = "" #gets the equation from the array
answer = "" #gets the answer from the array
mathproblems = ["2 + 2 = ", "342 + 356 = ", "2 + 9 ", " 6 * 5 * 2 = ", "6^4 * 2 + 5 = ", "fifty-four plus five equals: ", "-1 + 2 = ", "9 * 45 = ", "4 * 9 + 3 * 6 + 2 / 4 - 4 + 2 = ", "3 + 1 + 2 / 1 + 2 * 6 = "]
mathanswers = ["4", "698", "11", "60", "2597" , "59", "1", "405", "53", "18"] #the arrays
mathcorrect = False #are they correct
mathtimestart = 0 #starts the timer
mathtimeend = 0 #ends the timer
mathtimetotal = 0 #how long did it take
howmanyfish = 0 #how many fish did the user catch
fishtime = False #is the fish on the screen
fishanim = 0 #supposed to be rotation


#--------Between the Modes--------
tutorialdone = False #is the tutorial done
bufferperiod = False #doesn't go straight into the actual game 


#--------Settings--------
settings = False #did the user open settings
skiptutorial = False #tutorial or no
timeleft = 10 #how much time is left 
usertime = 10 #a constant that changes in the settings

#--------End Game--------
stupidscreen = Actor("stupid.png", pos = (WIDTH/2,-HEIGHT/2)) #a black screen because I can't figure out how to make an image move down
endgame = False #is the game over
anime = -500 #screen position
finaletext = 0 #which text are we on
finaletextchecker = 0 #which text are we supposed to be on



#do i use actors for everything???maybe i make the math thing a class
#various actor creations
#cannot figure out how to make it simplified to ignore this
#--------The Math Actors--------
base = Actor("base.png", pos = (750,220)) #the base of the math thing
#---Buttons---
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
#Fish
darealfish = Actor("fishh.png", pos = (WIDTH/2, HEIGHT/2))


def on_mouse_down(pos, button): #button configuration 
  #function carried mvp right here
  #i mean look at all of these variables
  #straight carried thanks pygame gods
  global loading, tutorial, line, tutorialtexts, mathisinsession, linecasted, mathtime, value, equation, answer, mathcorrect, mathtimestart, mathtimeend, mathtimetotal, fishtime, tutorialdone, howmanyfish, anime, finaletext, settings, usertime, timeleft, bufferperiod, skiptutorial


  #--------Button Configurations--------
  #calculates the distances for the mouse and the button
  startdistancesx = pos[0] - 575 
  startdistancesy = pos[1]- 335
  minusposx = pos[0] - WIDTH/2
  minusposy = pos[1] - HEIGHT/2


  
  if tutorial == False and button == mouse.LEFT and tutorialdone == False: #if user is on the start screen
    if -190 < startdistancesx < 190 and  -40 < startdistancesy < 40 and settings == False: #if the user clicks the start button
      loading = True #set the settings and start game
      timeleft = usertime
    elif -190 < startdistancesx < 190 and  55 < startdistancesy < 130 and loading == False: #if the user clicks the settings
      settings = True
  if settings == True: #if the settings screen is open
    if -250 < minusposx < -150 and -50 < minusposy < 50: #if user wants to not have more time
      if usertime != 10:
        usertime -= 10
    if 150 < minusposx < 250 and -50 < minusposy < 50: #if user wants to add more time
      usertime += 10
    if -500 < minusposx < -400 and 270 < minusposy < 300: #if the user closes settings
      settings = False
    if 348 < minusposx < 374 and 272 < minusposy < 297: #if the user doesn't want the tutorial
      if skiptutorial == False:
        skiptutorial = True
      else:
        skiptutorial = False



#--------Game Start--------
      #The Tutorial
  if tutorial == True and tutorialdone == False: #if the tutorial is in session
    
    if button == mouse.LEFT and line < 8: #if the user clicks with the left mouse button
      
      if line == 2: #if the line is 2
        linecasted = True #cast the line and set the line to 7
        line = 7
        clock.schedule_unique(mathzzzz,5) #run math in 5 seconds
        
      tutorialtext() #update tutorial text on screen

      
    if mathisinsession == True and button == mouse.RIGHT and mathtime == False: #if its math time
      tutorialtext() #run tutorial text and set mathtime to true
      mathtime = True
      
    if 10 <= line <= 12: #don't proceed after line 12, also figured out you can do this
      tutorialtext() #tutorial text
      
    #here we go the various math problems
    #math
    if line == 13: #start the math
      mathtimestart =  time.time()
      tutorialtext() #tutorial text
      
    if line == 21: #okay we're done with math and now the fish is on screen
      tutorialtext()
      fishtime = True
      
    if mathtime == True: #basically configures math
      if line >= 13:
        if len(value) < 8: #doesn't let them input more than 8 numbers
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
        if backspace.collidepoint(pos): #delete the value
            value = ""
          
        if submit.collidepoint(pos): 
          if(answer == value):#is it correct
            mathcorrect = True #good job
            line = 20 #move the tutorial along
            tutorialtext() #tutorial text
            mathtimeend = time.time() #stop the timer
            mathtimetotal = (round(mathtimeend - mathtimestart)) #how long did it take
          else:
            line = 16 #you failed 
            tutorialtext()
            value = "" #delete value


    
    if fishtime == True and line != 28: #if it's fish time and the tutorial isn't done
      tutorialtext() #tutorial text
      if line == 28: #if the line is 28 then the tutorial is done and it's time to move on
        tutorialdone = True
        tutorial = False
        resetmath()



#--------The Actual Game--------
  #finally out of the tutorial
 
  if tutorialdone == True: #if the user is done with tutorial

    #okay it was 3 am when I wrote the next 5 lines of code but if it works it works
    
    if bufferperiod == True: #if the buffer period is done, 
      
      if linecasted == False: #if line hasn't been casted
        linecasted = True #cast the line
        clock.schedule_unique(mathzzzz, numpy.random.randint(5,15)) #run math
    bufferperiod = True #ugh took me ages to do this 
    
    if mathisinsession == True and button == mouse.RIGHT and mathtime == False: #alright if the user picks up the fish
      mathtime = True #time for math
      line = 34 #using this variable to cause the math to not show up...
      
    if line == 34: #if the line is now 34
      mathtimestart = time.time() #start the timer
      tutorialtext() #make the line 35
      
    if fishtime == True: #if the fish has been caught then reset the game
      resetmath()
      
    if mathtime == True: #if it's time for math
      #everything like before
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
            howmanyfish += 1 #except we add on the fish
            value = "" #and reset the value
          else:
            value = ""   #no try again sad
    
    
      
#--------The Randoms/Fillers--------

def draw_rect_alpha(surface, color, rect): #I totally didn't copy and paste this...why would I
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA) #gives me a surface that allows a fade
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect()) #draws a rectange
    surface.blit(shape_surf, rect) #actually draws the rectange




def loadingscreen(): #alright if we're loading in
  global fadedone, loading, tutorial, skiptutorial, tutorialdone #variables 
  if fadedone == False: #if the fade isn't done
    for alpha in range(0, 1275): #lets fade
          draw_rect_alpha(surface, (0, 0, 0, (alpha/5)), (0, 0, WIDTH, HEIGHT)) #fade rectangle using that handy dandy function that I totally came up with
          pygame.display.flip() #updates the display. I have never used it before but it worked when I put it in so
          if alpha >= 255: #if the alpha is 255
            fadedone = True #we are done dont run again
          if alpha >= 1200: #if the alpha is 1200
            tutorial = True #time for tutorial
            if skiptutorial: #if the tutorial was skipped
              tutorialdone = True #fade out but don't start tutorial
              
  if fadedone == True: #if we're done fading
    loading = False #no more loading
    draw_rect_alpha(surface, (0, 0, 0, 255), (0, 0, WIDTH, HEIGHT)) #I think this is for when the fade thing stops and the rectangle disappears...idk I was tired




def fadess(): #more fades??? that doesn't work??? but it's okay because the game still runs and you can't tell
  global tutorial, fades, runfades, textfadedone #more variables
  runfades = True #runnin the fades
  if tutorial == True: #if the tutorial is in session
    for alphas in range(0, 1275): #we fadin
      draw_rect_alpha(surface, (0, 0, 255, (alphas/5)), (0, 500, WIDTH, HEIGHT))
      if alphas >= 1200: #if alpha is 1200
        fades = 1 #we not fading any more
    if fades == 1: #it is done
      textfadedone = True
      




def timerbecauseimlazy(): #making a timer because i can't figure out how to get a real one... if it works it works, plus i was angry
  global timeleft, endgame #variables
  if timeleft > 0: #if the time hasn't ran out
    timeleft -= 1 #subtract
  if timeleft <= 0: #if the time is over
    endgame = True #done with the game


      
#--------My Most Important Function--------
def tutorialtext():
  global line, listoflines, tutorialtexts, mathtime
  tutorialtexts = listoflines[line] #set the tutorial text variable to whichever line we're on
  line += 1 #add one



#--------The Classics--------
def draw():
  global loading, runfades, textfadedone, linecasted, mathisinsession, fishtime, mathtimetotal, finaletextchecker
  
  
  if tutorial == False and settings == False: #if the user literally just started the game
    screen.blit("hello.png", (0,0)) #draw the title
    
  if settings == True: #if the user opened settings
    screen.fill((255,0,128)) #fill with hot pink

    #draws the circles to add and subtract the amount of time is left
    pygame.draw.circle(surface, (0), (300,HEIGHT/2), 50, 2)
    pygame.draw.circle(surface, (0), (700,HEIGHT/2), 50, 2)
    #draws the + and - to designate the buttons
    screen.draw.text("-", topleft = (292, HEIGHT/2-25), color = (0), fontsize = 70)
    screen.draw.text("+", topleft = (688, HEIGHT/2-27), color = (0), fontsize = 70)
    #tells the user what it's for
    screen.draw.text("Amount of time \n increments of 10", center = (WIDTH/2, 170), color = (0), fontsize = 65)
    #lets the user leave
    screen.draw.text("Back", topleft = (15, 575), color = (0), fontsize = 35)
    #Prints out how much time they currently have selected
    screen.draw.text(str(usertime), center = (WIDTH/2,HEIGHT/2), color = (0), fontsize = 55)
    #do they want to enable the tutorial
    screen.draw.text("Tutorial?", topright = (1000-15, 575), color = (0), fontsize = 35)
    
    if skiptutorial == False: #fills the box or emptys the box
      pygame.draw.rect(surface, (0), (845, 570, 30,30 ), 2)
    if skiptutorial == True:
      pygame.draw.rect(surface, (0), (845, 570, 30,30 ))


      
  if loading == True: #if loading is a go
    clock.schedule_unique(loadingscreen, 1) #run this function once
    
  if tutorial == True: #if the tutorial is running
    screen.blit("pond.png", (0,0)) #draws the pond
    if textfadedone == False: #if the text hasn't even showed up
      clock.schedule_unique(fadess, 3) #lets make it show up
    if runfades == True and textfadedone == False: #even more fades???
      fadess()
      
    if textfadedone == True: #if the game has fr started
      screen.blit("fish.png", (-100,350)) #draw the fishing rod
      
      if line >= 1: #if the tutorial text is a go
        draw_rect_alpha(surface, (0, 0, 255), (0, 500, WIDTH, HEIGHT)) #draw where they're[the text] gonna be
        draw_rect_alpha(surface, (255,255,255), (0,485,WIDTH, 15))
        screen.draw.text(tutorialtexts, topleft = (40,520), color = (255,255,255), fontsize = 30) #this actually draws the lines...most important code for the tutorial to  me
        
      if linecasted == True: #if the line is casted
        screen.blit("bobber.png", (WIDTH/2,375)) #draw the bobber thing
        if mathisinsession == True: #if it's time to solve math and bring the fish in
          screen.blit("exclamation.png", (500,200)) #tell the user
          
      if line >= 8: #if the line is 8 or more
        draw_rect_alpha(surface, (0, 0, 255), (0, 500, WIDTH, HEIGHT)) #draw the box at the bottom again
        draw_rect_alpha(surface, (255,255,255), (0,485,WIDTH, 15))
        screen.draw.text(tutorialtexts, topleft = (40,520), color = (255,255,255), fontsize = 30) #again an important piece of code fr
        
      if mathtime == True and fishtime == False: #if it's math time then draw everything
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
        
        #shows the user which equation is there and what they've inputted
        screen.draw.text(value, topleft = (580, 150), fontsize = 50)
        screen.draw.text(equation, topleft = (580, 100), fontsize = 65)

        
        if line == 21: #if the user is done solving math
          screen.draw.text("Good job. You're one math wizard even though it took you " + str(mathtimetotal) + " seconds to answer.", topleft = (40,520), color = (255,255,255), fontsize = 30) #tells the user how bad they are. gotta keep them humbled
          
    if fishtime == True: #if it's time to show the one and only fish
      linecasted = False #bring the bobber back in
      #clock.schedule_interval(fishanime, 0.25) supposed to be animation that I decided to take out
      darealfish.draw() #draw the fish
      mathtimetotal = 0 #reset the math time total


      #yes on to the real game
  if tutorialdone == True: #if the tutorial is over
      screen.blit("pond.png", (0,0)) #draws the pond and the fishing rod
      screen.blit("fish.png", (-100,350))

    
      pygame.draw.circle(surface, (0), (885,75), 50) #draws the base of the timer
    
      pygame.draw.arc(surface, (255), (840,30, 90,90), 0, numpy.radians(timeleft * (360 / usertime)), 45) #draws the timer using a translater for radians to degrees
      clock.schedule_unique(timerbecauseimlazy, 1.0) #run the timer 
      
      if linecasted == True and fishtime == False: #if the user has casted the line
        screen.blit("bobber.png", (WIDTH/2,375)) #draw the bobber
        
        if mathisinsession == True: #if it's time to do math
          screen.blit("exclamation.png", (500,200)) #tell the user
          
      if mathtime == True and fishtime == False: #draw every actor cause we're solving math
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
        
      if fishtime == True:  #if it's time to show the fish
        linecasted = False #bring in the line and draw the fish
        #clock.schedule_interval(fishanime, 0.25)   once again fish animation that I took out
        darealfish.draw()
        
      if endgame == True and fishtime == False and mathtime == False and linecasted == False: #if it's time for the end game
        stupidscreen.draw() #draw the screen
        screen.draw.text("Time to head home...", center = (WIDTH/2, HEIGHT/2), color = (255), fontsize = 50 ) #tell the user that it's time to stop
        if finaletext == 0: #if the text hasn't showed up yet
          clock.schedule(finalscreenyay, 0.01) #run the final screen so the screen goes down
          
        if 0 < finaletext: #draws the text after every 2 seconds
          screen.draw.text("Day 1", center = (WIDTH/2, 150), color = (255,255,255), fontsize = 75)
          finaletextchecker = 1.1 #sets the limit for the text to this
          clock.schedule_interval(magictrick, 2) #run the function
          
        if 1 < finaletext: #repeat the first function
          screen.draw.text("complete", center = (WIDTH/2, 200), color = (255,255,255), fontsize = 50)
          finaletextchecker = 2.1
          
        if 2 < finaletext: #repeat
          screen.draw.text("Total Fish Caught: " + str(howmanyfish), center = (WIDTH/2, 250), color = (255,255,255), fontsize = 45)
          finaletextchecker = 3.1
          
        if 3 < finaletext: #repreat
          screen.draw.text("Total time it took for you to do math: " + str(mathtimetotal), center = (WIDTH/2, 300), color = (255,255,255), fontsize = 45)
          finaletextchecker = 4.1

          #now if we're done
          
        if 4 < finaletext:
          if mathtimetotal == 0 or howmanyfish == 0: #grades the user based on their average and how much fish they caught
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


#--------Math--------  
def mathzzzz(): #math is started and assigns a problem
  global mathisinsession, line, tutorialdone
  mathisinsession = True
  
  mathproblem()
  
  if tutorialdone == False: #set the line to 8 and then run tutorial texts too
    line = 8
    tutorialtext()
    
def resetmath(): #reset the game
  global linecasted, mathisinsession, mathtime, value, whichmath, equation, answer, mathcorrect, fishtime, mathtimestart, mathtimeend, endgame

  linecasted = False
  mathisinsession = False
  mathtime = False
  value = ""
  whichmath = 0
  equation = ""
  answer = ""
  mathcorrect = False
  fishtime = False
  mathtimestart = 0
  mathtimeend = 0



def mathproblem(): #assigns a math problem and answer to variables
  global whichmath, mathproblems, equation, answer, mathanswers
  whichmath = numpy.random.randint(0,(len(mathproblems)))
  equation = mathproblems[whichmath]
  answer = mathanswers[whichmath]



def fishanime(): #fish animation
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
