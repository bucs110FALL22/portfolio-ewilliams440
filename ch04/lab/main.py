import random
import pygame
import math
pygame.init()

#setup
backcolor=("navy")
circlecolor=(0,0,200)
hitcolor=(0,255,0)
misscolor=(255,0,0)
player1color=("white")
player2color=("black")
chosenplayer=0
buttonsize=75
buttondistance=10
player1score=0
player2score=0

print("Choose Player White or Player Black")

window=pygame.display.set_mode()
windowx,windowy=pygame.display.get_window_size()
center=int(windowx)/2,int(windowy)/2
window.fill(backcolor)
pygame.draw.circle(window,circlecolor,center,center[1])

player1button=pygame.Rect(buttondistance,buttondistance,buttonsize,buttonsize)
drawing1button=pygame.draw.rect(window,player1color,player1button)
player2button=pygame.Rect(windowx-buttonsize-buttondistance,buttondistance,buttonsize,buttonsize)
drawing2button=pygame.draw.rect(window,player2color,player2button)
pygame.display.flip()

user_has_chosen=False

#Choosing Player White (1) or Player Black (2)
while not user_has_chosen:
  for event in pygame.event.get():
    if event.type==pygame.MOUSEBUTTONDOWN:
      clickposition=event.pos
      if player1button.collidepoint(clickposition):
        print("Chosen Player White")
        user_has_chosen=True
        chosenplayer=1
      elif player2button.collidepoint(clickposition):
        print("Chosen Player Black")
        user_has_chosen=True
        chosenplayer=2

#Players are throwing
for i in range(10):
  throwx=random.randrange(0,windowx)
  throwy=random.randrange(0,windowy)
  farfromcenter=math.hypot(center[0]-throwx,center[1]-throwy)
  is_in_circle=farfromcenter<=center[1]
  if is_in_circle:
    dartcolor=player1color
    player1score=player1score+1
  else:
    dartcolor=misscolor
  pygame.draw.circle(window,dartcolor,(throwx,throwy),2)
  pygame.time.wait(1000)
  pygame.display.flip()
  #player 2 turn starts here
  throwx=random.randrange(0,windowx)
  throwy=random.randrange(0,windowy)
  farfromcenter=math.hypot(center[0]-throwx,center[1]-throwy)
  is_in_circle=farfromcenter<=center[1]
  if is_in_circle:
    dartcolor=player2color
    player2score=player2score+1
  else:
    dartcolor=misscolor
  pygame.draw.circle(window,dartcolor,(throwx,throwy),2)
  pygame.time.wait(1000)
  pygame.display.flip()

#results
if player1score==player2score:
  print("Tie!")
elif player2score>player1score:
  print("Player Black won!")
  if chosenplayer==2:
    print("You chose correctly")
  elif chosenplayer==0:
    print("Something is wrong here")
  else:
    print("You chose incorrectly")
elif player1score>player2score:
  print("Player White won!")
  if chosenplayer==1:
    print("You chose correctly")
  elif chosenplayer==0:
    print("Something is wrong here")
  else:
    print("You chose incorrectly")