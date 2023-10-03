"""Main - py"""
import time
from turtle import Screen
from paddle import Paddle

GAME_IS_ON = True

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG GAME")
screen.tracer(0)

r_pad = Paddle(pos_inic=(350, 0))
l_pad = Paddle(pos_inic=(-350, 0))

screen.listen()
screen.onkey(l_pad.go_up, "Up")
screen.onkey(l_pad.go_down, "Down")


while GAME_IS_ON:

    screen.update()

    time.sleep(0.08)


screen.exitonclick()
