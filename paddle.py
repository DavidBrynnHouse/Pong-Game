from turtle import Turtle
import c


class Paddle(Turtle):
    def __init__(self, player_multiplier):
        super().__init__()
        self.shape('square')
        self.setheading(90)
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.color("white")
        self.goto(c.STARTING_POSITION * player_multiplier, 0)
        self.score = 0

    def move_paddle_up(self):
        self.forward(c.MOVE_DISTANCE)

    def move_paddle_down(self):
        self.forward(-c.MOVE_DISTANCE)
