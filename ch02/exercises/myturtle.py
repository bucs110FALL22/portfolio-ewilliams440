import turtle

sides=4

tutrle=turtle.Turtle()
tutrle.shape("turtle")
tutrle.color("purple")
length=50
angle=360/sides
for i in [angle]*sides:
  tutrle.forward(length)
  tutrle.left(angle)

movingangle=135
movinglength=25
tutrle.color("red")
tutrle.up()
tutrle.right(movingangle)
tutrle.forward(movinglength)
tutrle.down()

length=30
angle=360/sides
for i in [angle]*sides:
  tutrle.forward(length)
  tutrle.left(angle)

window = turtle.Screen()
window.exitonclick()