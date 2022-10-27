import turtle
import random

def move(tur,x,y):
  tur.up()
  tur.goto(x,y)
  tur.down()

def drawcloud(tur,x,y,color="white",radius=15):
  move(tur,x,y)
  tur.color(color)
  for i in range (4):
    circlength=random.randint(45,180)
    tur.seth(0)
    tur.circle(radius,circlength)
  tur.goto(x,tur.position()[1])
  tur.goto(x,y)

def main():
  background="light blue"
  wavecolor="navy"
  waveradius=15
  suncolor="yellow"
  sunradius=15
  cloudcolor="white"
  cloudradius=15
  window=turtle.Screen()
  maxxcoord=window.screensize()[0]/2
  maxycoord=window.screensize()[1]/2
  turtboy=turtle.Turtle()
  #draw waves
  move(turtboy,-maxxcoord+1,-maxycoord+75)
  turtboy.color(wavecolor)
  window.bgcolor(background)
  while abs(turtboy.position()[0])<maxxcoord:
    turtboy.seth(270)
    turtboy.circle(waveradius,180)
  #draw sun
  move(turtboy,-maxxcoord+50,maxycoord-50)
  turtboy.color(suncolor)
  turtboy.circle(sunradius)
  window.exitonclick()
  #draw clouds
  drawcloud(turtboy,100,10)


main()
#things so far-- turtle seth, circle