#This Displays double Spiraling Circle
from turtle import *
import turtle # importing turtle module
turtle.title("Spiraling Circle Animation") #custom name for window
bgcolor("black")#Background Color
speed(0)
hideturtle()
for i in range(150):
    color("blue") #Outer circle color
    circle(i)
    color("white") #inner circle color
    circle(i*0.8) #Radius of circle
    right(3)
    forward(3)
done()