
"""
    A simple Pong game in Python.
    by guiltylogik
"""

import turtle as ttl

win =  ttl.Screen()
win.title("Pong By Guiltylogik")
win.bgcolor("blue")
win.setup(width=800, height=600)
win.tracer(0)

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