"""Ball Class"""
from turtle import Turtle



class Ball(Turtle):
    """ball"""
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape('circle')
        self.color('white')
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """move"""
        ball_ypos = self.ycor() + self.y_move
        ball_xpos = self.xcor() + self.x_move
        self.goto(x=ball_xpos, y=ball_ypos)


    def bounce_wall(self):
        """bounce the ball"""
        self.y_move *= -1

    def bounce_paddle(self):
        """bounce in the paddle"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_ball(self):
        """reset the ball"""
        self.goto(x=0,y=0)
        self.bounce_paddle()
        self.move_speed = 0.1
