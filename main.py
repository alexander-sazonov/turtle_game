from turtle import Turtle, Screen
import random
import math
#Создаем экран
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('light green')
turtle = Turtle()
turtle.hideturtle()
turtle.pensize(2)
turtle.speed(0)
turtle.penup()
turtle.goto(-250,250)
turtle.pendown()
for _ in range(4):
    turtle.forward(500)
    turtle.right(90)
#Создаем игрока
player = Turtle(shape='arrow')
player.shapesize(2)
player.speed(0)
speed = 1
#Функции для управления
def turn_left():
    player.left(30)
def turn_right():
    player.right(30)
def increase_speed():
    global speed
    speed += 1
#навешиваем функции на кнопки
screen.listen()
screen.onkey(turn_left,'Left')
screen.onkey(turn_right,'Right')
screen.onkey(increase_speed,'Up')

while True:
    player.forward(speed)
screen.mainloop()
