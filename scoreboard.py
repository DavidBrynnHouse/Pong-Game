from turtle import Turtle
import c


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_1_score = 0
        self.player_2_score = 0
        self.refresh()

    def increase_p1_score(self):
        self.player_1_score += 1
        self.clear()
        self.refresh()

    def increase_p2_score(self):
        self.player_2_score += 1
        self.clear()
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", move=False, align=c.ALIGNMENT, font=c.FONT)

    def refresh(self):
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"{self.player_1_score}     {self.player_2_score}", move=False, align=c.ALIGNMENT, font=c.FONT)
        self.hideturtle()
