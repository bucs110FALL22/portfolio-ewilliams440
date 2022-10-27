import turtle
import random

def move(tur,x,y):
  tur.up()
  tur.goto(x,y)
  tur.down()

def drawcloud(tur,x,y,color,radius):
  tur.up()
  tur.goto(x,y)
  tur.down()
  tur.color(color)
  cloudup=True
  while tur.position()[1]<(y+10) and cloudup:
    circlength=random.randint(10,179)
    tur.seth(90)
    tur.circle(radius,circlength)
  cloudup=False
  while tur.position()[1]>(y+radius+2):
    circlength=random.randint(180,255)
    tur.seth(90)
    tur.circle(radius,circlength)
  tur.seth(90)
  tur.circle(radius,180)
  tur.goto(tur.position()[0],y)
  tur.goto(x,y)

def main():
  background="light blue"
  wavecolor="navy"
  waveradius=15
  suncolor="yellow"
  sunradius=15
  cloudcolor="white"
  cloudradius=7
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
  #draw clouds
  drawcloud(turtboy,0,60,cloudcolor,cloudradius)
  drawcloud(turtboy,-150,10,cloudcolor,cloudradius)
  drawcloud(turtboy,150,-10,cloudcolor,cloudradius)
  window.exitonclick()

main()
#things so far-- turtle seth, circle