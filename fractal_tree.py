import turtle
import random

window = turtle.Screen()
window.bgcolor("black")

def pick_colors():
    color = [random.randrange(0, 256) for _ in range(3)]
    r, g, b = color
    if r == 0 and g == 0 and b == 0:
        pick_colors()
    else:
        return r, g, b

turtle.colormode(255)
pen = turtle.Turtle()
pen.speed(0)
pen.left(90)
pen.penup()
pen.setpos(0, -250)
pen.pendown()
pen.hideturtle()
pen.pensize(2)

window.exitonclick()

def pain_tree(branch_lenght: int, pen: turtle.Turtle, min_branch_lenght: int, angle: int):

    if (branch_lenght < min_branch_lenght):     
        return

    turtle.colormode(255)
    pen.color(pick_colors())
    pen.forward(branch_lenght)
    pen.left(angle/2)
    pain_tree(branch_lenght/2, pen, min_branch_lenght, angle)
    pen.right(angle)
    pain_tree(branch_lenght/2, pen, min_branch_lenght, angle)
    pen.left(angle/2)
    pen.backward(branch_lenght)

def main():
   pain_tree(300, pen, 1, 60)

