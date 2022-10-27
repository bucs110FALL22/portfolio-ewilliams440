import turtle
import random

def move(tur,x=0,y=0):
  '''
  Moves the turtle to another location without leaving a trail.
  args:
    tur(turtle): the turtle object being moved
    x(int): the turtle's desired x location
    y(int): the turtle's desired y location
  returns:
    None
  '''
  tur.up()
  tur.goto(x,y)
  tur.down()

def drawcloud(tur,x=0,y=0,color="white",radius=10):
  '''
  Draws a randomly generated cloud with the bottom right corner at (x,y).
  args:
    tur(turtle): the turtle object being moved
    x(int): the cloud's rightmost coordinate
    y(int): the cloud's bottommost coordinate
    color(str or tuple): the cloud's color
    radius(int): the radius of the cloud's "puffs"
  returns:
    None
  '''
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
  cloudloc1=(0,60)
  cloudloc2=(-150,10)
  cloudloc3=(150,-10)
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
  drawcloud(turtboy,cloudloc1[0],cloudloc1[1],cloudcolor,cloudradius)
  drawcloud(turtboy,cloudloc2[0],cloudloc2[1],cloudcolor,cloudradius)
  drawcloud(turtboy,cloudloc3[0],cloudloc3[1],cloudcolor,cloudradius)
  window.exitonclick()

main()