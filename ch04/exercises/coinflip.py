import random
import turtle

window=turtle.Screen()
shellboy=turtle.Turtle()
shellboy.shape("turtle")
shellboy.color("green")
windowx=window.screensize()[0]
windowy=window.screensize()[1]


while abs(shellboy.xcor())<=windowx/2 and abs(shellboy.ycor())<=windowy/2:
  coin=random.randint(0,1)
  if coin==1:
    shellboy.right(90)
  else:
    shellboy.left(90)
  shellboy.forward(50)

window.exitonclick()