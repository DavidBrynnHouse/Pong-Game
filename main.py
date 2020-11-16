from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title('Pong')
screen.tracer(0)

player_1 = Paddle(1)
player_2 = Paddle(-1)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player_1.move_paddle_up, "a")
screen.onkey(player_1.move_paddle_down, "s")

screen.onkey(player_2.move_paddle_up, "Up")
screen.onkey(player_2.move_paddle_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move_ball()

    # Bounce off wall
    if ball.ycor() < -270 or ball.ycor() > 270:
        ball.bounce()

    # Bounce off paddle
    if ball.distance(player_2) < 50 and ball.xcor() > 340 or ball.distance(player_1) < 50 and ball.xcor() < -340:
        ball.bounce()

    if ball.xcor() > 400:
        scoreboard.increase_p1_score()
        del ball
        ball = Ball()
        ball.move_ball()

    if ball.xcor() < -440:
        scoreboard.increase_p2_score()
        del ball
        ball = Ball()
        ball.move_ball()

screen.exitonclick()
