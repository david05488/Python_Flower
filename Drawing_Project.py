import turtle

# -----------------------------------------------------------------------------------------------
        # - GLOBAL VARIABLES
# -----------------------------------------------------------------------------------------------
window = turtle.Screen()
window.bgcolor("#25214C")
#Brad definition
brad = turtle.Turtle()
#Angie definition
angie = turtle.Turtle()
#David definition
david = turtle.Turtle()



# -----------------------------------------------------------------------------------------------
        # - FUNCTION DECLARATIONS
# -----------------------------------------------------------------------------------------------
def draw_square():
    brad.shape("classic")
    brad.color("green")
    brad.speed(5)
    sqCount = 0
    tCount = 0
    while tCount < 72:
        while sqCount < 4:
            brad.forward(130)
            brad.right(90)
            sqCount = sqCount + 1
        brad.left(5)
        sqCount = 0
        tCount = tCount + 1


def draw_circle():
    angie.shape("circle")
    angie.color("yellow")
    angie.speed(2)
    angie.goto(0, -188)
    angie.circle(190)

def draw_triangle():
    david.shape("turtle")
    david.color("red")
    david.speed(1)
    position = david.pos()
    david.forward(190)
    david.left(135)
    david.forward(270)
    david.left(90)
    david.forward(270)
    david.left(45)
    david.goto(position)



#-------------------------------------------Main routine-----------------------------------------
draw_square()
draw_circle()
draw_triangle()
window.exitonclick()