
"""
    A simple Pong game in Python.
    by guiltylogik
"""

import turtle as ttl
import os


win =  ttl.Screen()
win.title("Pong By Guiltylogik")
win.bgcolor("blue")
win.setup(width=800, height=600)
win.tracer(0)

score_a = 0
score_b = 0

#Paddle A
pad_a = ttl.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("white")
pad_a.shapesize(stretch_wid=5, stretch_len=.7)
pad_a.penup()
pad_a.goto(-350, 0)

#Paddle B
pad_b = ttl.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("white")
pad_b.shapesize(stretch_wid=5, stretch_len=.7)
pad_b.penup()
pad_b.goto(350, 0)

#Ball
ball = ttl.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .15
ball.dy = .15

#ScoreBoard
board = ttl.Turtle()
board.speed(0)
board.color("white")
board.penup()
board.hideturtle()
board.goto(0, 260)
board.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

#Object controls
def pad_a_up():
    y = pad_a.ycor()
    y += 20
    pad_a.sety(y)

def pad_a_down():
    y = pad_a.ycor()
    y -= 20
    pad_a.sety(y)

def pad_b_up():
    y = pad_b.ycor()
    y += 20
    pad_b.sety(y)

def pad_b_down():
    y = pad_b.ycor()
    y -= 20
    pad_b.sety(y)

#key Binding
win.listen()
win.onkeypress(pad_a_up, 'w')
win.onkeypress(pad_a_down, 'z')
win.onkeypress(pad_b_up, 'Up')
win.onkeypress(pad_b_down, 'Down')


# Main game loop
while True:
    win.update()

    #Movin the ball
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    #Adding border
    #Top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay assets/bar.wav&")

    #Bottom
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay assets/bar.wav&")

    #Right
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        board.clear()
        board.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
        os.system("aplay assets/over.wav&")

    #Left
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        board.clear()
        board.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
        os.system("aplay assets/over.wav&")

    #Pad and Ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pad_b.ycor() + 40 and ball.ycor() > pad_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        os.system("aplay assets/pad.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < pad_a.ycor() + 40 and ball.ycor() > pad_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("aplay assets/pad.wav&")