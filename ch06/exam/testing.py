import turtle
import random
tur=turtle.Turtle()
x=10
y=0
color="black"
radius=5

window=turtle.Screen()

def cloud(tur,x,y,color,radius):
  tur.up()
  tur.goto(x,y)
  tur.down()
  tur.color(color)
  for i in range (10):
    if tur.position()[1]<(y+6):
      circlength=random.randint(10,90)
    elif tur.position()[1]>(y+30):
      circlength=random.randint(180,270)
    tur.seth(90)
    tur.circle(radius,circlength)
  tur.seth(90)
  tur.circle(radius,180)
  tur.goto(tur.position()[0],y)
  tur.goto(x,y)

cloud(tur,x,y,color,radius)
window.exitonclick()