#This display single spiraling circle
import turtle  # importing turtle
# initialise the turtle instance
turtle.title("Spiraling Circle Animation")
t = turtle.Turtle()
# changes speed of turtle
t.speed(0)
t.hideturtle() # hiding turtle
t.getscreen().bgcolor("black")#background color
t.color("blue")#Circle Color
for i in range(150):
    t.circle(i) # by passing radius i
    t._rotate(5)
turtle.done()