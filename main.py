"""Project 22:Pong"""

from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")

screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
r_scoreboard = Scoreboard((100, 210))
l_scoreboard = Scoreboard((-100, 210))

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(ball.pace)
    ball.move()
    # Detect collision wth the wall

    if ball.ycor() > 285 or ball.ycor() < -270:
        ball.y_bounce()

    # Detect collision with paddle:
    if ball.distance(r_paddle) < 50 and 330 < ball.xcor() < 350 or ball.distance(
            l_paddle) < 50 and -330 > ball.xcor() > -350:
        ball.x_bounce()

    # Detect if the ball goes out of bounds
    if ball.xcor() > 400:
        ball.out_of_bounds()
        r_scoreboard.update_score()

    if ball.xcor() < -400:
        ball.out_of_bounds()
        l_scoreboard.update_score()

screen.exitonclick()
