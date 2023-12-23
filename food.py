from turtle import Turtle
from random import randint

class Food(Turtle):
    '''Food class for the Snake Game'''
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        '''Refresh the food'''
        random_pos = (randint(-280, 280), randint(-280, 260))
        self.goto(random_pos)
