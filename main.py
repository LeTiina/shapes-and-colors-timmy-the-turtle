from turtle import Turtle, Screen
import random

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    timmy.color(R, G, B)

def shape(lenght, angle):
    change_color()
    for a in range(lenght):
        timmy.right(angle)
        timmy.forward(100)

timmy = Turtle()
timmy.shape("turtle")

shape(3,120)
shape(4,90)
shape(5,72)
shape(6,60)
shape(7,51.4285714)
shape(8,45)
shape(9,40)

screen = Screen()
screen.exitonclick()



#timmy_the_turtle = Turtle()
#image = 'cat.gif'


#screen = Screen()
#screen.addshape(image)
#timmy_the_turtle.shape(image)

#screen.exitonclick()