from turtle import Turtle, Screen
import random
import math

# Создаем экран
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('light green')
turtle = Turtle()
turtle.hideturtle()
turtle.pensize(2)
turtle.speed(0)
turtle.penup()
turtle.goto(-250, 250)
turtle.pendown()
for _ in range(4):
    turtle.forward(500)
    turtle.right(90)
# Создаем игрока
player = Turtle(shape='arrow')
player.penup()
player.shapesize(2)
player.speed(0)
# Создаем еду
food = Turtle(shape='circle')
food.speed(0)
food.color('Red')
food.penup()
food.goto(random.randint(-250, 250), random.randint(-250, 250))
#Создаем счет
score_turtle = Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(0,275)
score_turtle.pendown()
speed = 1
score = 0


def print_score():
    score_turtle.clear()
    score_turtle.write(f'Sore: {score}',font=('Serif',24,'bold'))


# Функции для управления
def turn_left():
    player.left(30)


def turn_right():
    player.right(30)


def increase_speed():
    global speed
    speed += 1


# навешиваем функции на кнопки
screen.listen()
screen.onkey(turn_left, 'Left')
screen.onkey(turn_right, 'Right')
screen.onkey(increase_speed, 'Up')

while True:
    player.forward(speed)
    if (player.xcor() < -250) or (player.xcor() > 250):
        player.left(180)
    if (player.ycor() < -250) or (player.ycor() > 250):
        player.left(180)
    if (food.xcor() - 15 < player.xcor() < food.xcor() + 15) and (food.ycor() - 15 < player.ycor() < food.ycor() + 15):
        food.goto(random.randint(-250, 250), random.randint(-250, 250))
        score += 1
        print_score()
screen.mainloop()
