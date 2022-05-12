from turtle import Turtle
import random
CORD1 = -260
CORD2 = 260
CORD3 = -430
MOVE_DISTANCE = 20
# COORD = [(0,-430), (-30,-400),(430,20),(430,20),(430,40)]
COORD = [(0,-230), (-40,-190),(-80,-150),(-100,-110),(-140,0)]
direction =[-1,1]


class Ball(Turtle):
    def __init__(self):
        self.all_ball = []
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len = 1, stretch_wid = 1)
        self.speed("fastest")
        self.pace= 0.1
        # self.ball_reset()

        self.x_move = 10
        self.y_move = 10

    def ball_reset(self):
        print("inside reset")
        self.goto(0, 0)
        self.x_move *= -1
        self.y_move *= random.choice(direction)
        self.pace = 0.1

    def ball_first_move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x,new_y)

    def ball_bounce(self):
        print("ball_bounce")
        self.y_move *= -1

    def ball_hit_move(self):
        print("opposite")
        self.x_move *= -1
        self.pace *= 0.9


