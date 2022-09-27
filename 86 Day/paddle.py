from turtle import Turtle

MOVE_DIST = 70

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color('steel blue')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.goto(x=0, y=-280)

    def move_left(self):
        self.backward(MOVE_DIST)

    def move_right(self):
        self.forward(MOVE_DIST)

