import turtle
from typing import Tuple
import random

 #random.uniform(0.8, 0.9)

def pick_color() -> Tuple[int, int, int]:
    """Create a color with the rgb agreement"""
    color = (0, 0, 0)
    while color == (0, 0, 0):
        color = tuple(random.randint(0, 255) for _ in range(3))
    return color


def pain_tree(
    branch_lenght: float, pen: turtle.Turtle, min_branch_lenght: float, angle: float, 
    rdt_factor_angle1=1 / 2, rdt_factor_angle2= 1 / 2, rdt_factor_branch1= 1 / 2, rdt_factor_branch2= 1 / 2
) -> None:
    """
    Paints the fractral tree

    Parameters
    ----------
    branch_lengh : float
        Lenght of the branch
    pen : turtle.Turtle
        Pen to paint
    min_branch_lenght : int
        Minimal lenght of the branch
    angle : int
        Angle of the branch
    """

    if branch_lenght < min_branch_lenght:
        return

    pen.color(pick_color())
    pen.forward(branch_lenght)
    pen.left(angle * rdt_factor_angle1)
    pain_tree(branch_lenght * rdt_factor_branch1, pen, min_branch_lenght, angle)
    pen.right(angle)
    pain_tree(branch_lenght * rdt_factor_angle2, pen, min_branch_lenght, angle)
    pen.left(angle * rdt_factor_branch2)
    pen.backward(branch_lenght)


# Initial settings to turtle module
window = turtle.Screen()
window.bgcolor("black")
turtle.colormode(255)

# Pen setup
my_pen = turtle.Turtle()
my_pen.speed(0)
my_pen.left(90)
my_pen.penup()
my_pen.setpos(0, -250)
my_pen.pendown()
my_pen.hideturtle()
my_pen.pensize(2)

pain_tree(300, my_pen, 1, 90)
window.exitonclick()