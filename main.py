"""Main - py"""
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


GAME_IS_ON = True

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG GAME")
screen.tracer(0)

r_pad = Paddle(pos_inic=(350, 0))
l_pad = Paddle(pos_inic=(-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_pad.go_up, "Up")
screen.onkey(r_pad.go_down, "Down")
screen.onkey(l_pad.go_up, "w")
screen.onkey(l_pad.go_down, "s")


while GAME_IS_ON:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    #Detect colision wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()


    #detect colision with r_paddle
    if ball.distance(r_pad) < 50 and ball.xcor() > 320 or ball.distance(l_pad) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    #detect pad miss
    if ball.xcor() > 400:
        ball.reset_ball()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.r_point()





screen.exitonclick()
