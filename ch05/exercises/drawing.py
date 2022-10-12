import turtle

def drawEqShape(bob,num_sides,side_length):
  angle=360/num_sides
  for i in [angle]*num_sides:
    bob.forward(side_length)
    bob.left(angle)

bob=turtle.Turtle()
bob.shape("turtle")
bob.color("green")
num_sides=int(input("Number of sides:"))
side_length=float(input("Side length:"))
drawEqShape(bob,num_sides,side_length)

window = turtle.Screen()
window.exitonclick()