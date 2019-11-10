
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

# Main game loop

while True:
    win.update()