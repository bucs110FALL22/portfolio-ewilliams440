import turtle

sides=int(input("Number of sides:"))
length=float(input("Length of sides:"))
tortle=turtle.Turtle()
tortle.shape("turtle")
tortle.color("navy")

angle=360/sides
for i in [angle]*sides:
  tortle.forward(length)
  tortle.left(angle)

window = turtle.Screen()
window.exitonclick()