import random
from turtle import Turtle
import c


# generates a random 1 or -1 to determine which way the ball will go
def toss_coin():
    return 1 if random.random() < 0.5 else -1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.setheading(45)
        self.direction = toss_coin()

    def move_ball(self):
        self.forward(self.direction * c.MOVE_DISTANCE / 5)

    def bounce(self):
        self.setheading(self.heading() - 45)
