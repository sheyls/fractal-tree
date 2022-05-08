import turtle
import random


#Global variables
RDT_FACTOR_ANGLE1 = 1/2
RDT_FACTOR_ANGLE2 = 1/2
RDT_PORCENT_BRANCH1 = random.uniform(0.8, 0.9)
RDT_PORCENT_BRANCH2 = random.uniform(0.8, 0.9)

#Create a color with the rgb agreement
def pick_colors():
    color = [random.randrange(0, 256) for _ in range(3)]
    r, g, b = color
    if r == 0 and g == 0 and b == 0:
        pick_colors()
    else:
        return r, g, b

#Inicial settings to turtle module
window = turtle.Screen()
window.bgcolor("black")
turtle.colormode(255)
pen = turtle.Turtle()

#Personalization of the pen 
pen.speed(0)
pen.left(90)
pen.penup()
pen.setpos(0, -250)
pen.pendown()
pen.hideturtle()
pen.pensize(1)

#Painting tree algorithm
   # params: branch_lenght -> nicial lenght of a branch
   #         pen -> Turtle() to pain on the module
   #         min_branch_lenght -> stop condition for recurtion
   #         angle -> inicial angle of the branches

def pain_tree(branch_lenght: int, pen: turtle.Turtle, min_branch_lenght: int, angle: int):

    if (branch_lenght < min_branch_lenght):     
        return

    pen.color(pick_colors())
    pen.forward(branch_lenght)
    pen.left(angle * RDT_FACTOR_ANGLE1)
    pain_tree(branch_lenght * RDT_PORCENT_BRANCH1, pen, min_branch_lenght, angle)
    pen.right(angle)
    pain_tree(branch_lenght * RDT_PORCENT_BRANCH2, pen, min_branch_lenght, angle)
    pen.left(angle * RDT_FACTOR_ANGLE2)
    pen.backward(branch_lenght)


#Execute
pain_tree(100, pen, 40, 60)

window.exitonclick()
