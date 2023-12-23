# Snake class for the Snake Game
from turtle import Turtle

# Constants
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    '''Snake class for the Snake Game'''
    
    def __init__(self):
        self.x, self.y = 0, 0
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        '''Create the snake'''
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        '''Add a segment to the snake'''
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        '''Extend the snake'''
        self.add_segment(self.segments[-1].pos())

    def move(self):
        '''Move the snake'''
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x, new_y = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        '''Move the snake up'''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        '''Move the snake down'''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        '''Move the snake left'''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        '''Move the snake right'''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
