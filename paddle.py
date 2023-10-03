"""Paddle Class"""
from turtle import  Turtle

class Paddle(Turtle):
    """Paddle"""
    def __init__(self, pos_inic):
        super().__init__()
        self.pu()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid = 5, stretch_len =1 )
        self.goto(pos_inic)

    def go_up(self):
        """go_up"""
        new_y = self.ycor() + 20
        self.goto(x=self.xcor() ,y=new_y)
    def go_down(self):
        """go_down"""
        new_y = self.ycor() - 20
        self.goto(x=self.xcor() ,y=new_y)
        