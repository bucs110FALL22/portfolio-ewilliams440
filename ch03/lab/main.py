import turtle #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)





## 5. Your PART A code goes here
michelangelo.forward(random.randint(1,100))
leonardo.forward(random.randint(1,100))

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
for i in range(10):
  michelangelo.forward(random.randint(0,10))
  leonardo.forward(random.randint(0,10))

window.exitonclick()



  
# PART B - complete part B here
pygame.init()
window = pygame.display.set_mode()

coords=[]
num_sides=3
side_length=50
offset=100
backcolor=(0,100,100)
shapecolor=(0,150,200)

for num_sides in [3,4,6,9,360]:
  for i in range(num_sides):
    theta=2*math.pi*i/num_sides
    x=side_length*math.cos(theta)+offset
    y=side_length*math.sin(theta)+offset
    coords.append([x,y])
  window.fill(backcolor)
  pygame.draw.polygon(window,shapecolor,coords)
  coords.clear()
  pygame.display.flip()
  pygame.time.wait(1000)