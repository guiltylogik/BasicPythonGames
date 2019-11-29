# Space Invaders

import turtle

pen = turtle.Turtle()

pen.color('red')
pen.pendown()
for s in range(3):
    pen.forward(200)
    pen.right(90)
pen.forward(200)

player = turtle.Turtle()
player.penup()

def move_right():
    x = player.xcor()
    x += 10
    player.setx(x)

def move_left():
    x = player.xcor()
    x -= 10
    player.setx(x)

def move_forward():
    y = player.ycor()
    y += 10
    player.sety(y)

def move_backward():
    y = player.ycor()
    y -= 10
    player.sety(y)

win = turtle.Screen()
win.listen()

win.onkey(move_right, 'd')
win.onkey(move_left, 'a')
win.onkey(move_forward, 'w')
win.onkey(move_backward, 's')
