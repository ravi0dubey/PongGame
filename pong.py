from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Pong1(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def upa(self):
        new_y= self.ycor()+MOVE_DISTANCE
        self.goto(self.xcor(),new_y)

    def downd(self):
        new_y= self.ycor()-MOVE_DISTANCE
        self.goto(self.xcor(),new_y)

    def up2(self):
        new_y= self.ycor()+ MOVE_DISTANCE
        self.goto(self.xcor(),new_y)

    def down2(self):
        new_y= self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(),new_y)

# class Pong2:
#     def __init__(self,position):
#         self.new_pong2 = Turtle("square")
#         self.new_pong2.color("white")
#         self.new_pong2.shapesize(stretch_wid=5, stretch_len=1)
#         self.new_pong2.penup()
#         self.new_pong2.goto(position)
#
#     def move2(self):
#         self.new_pong2.forward(MOVE_DISTANCE)
#
#     def up2(self):
#         new_y= self.new_pong2.ycor()+ 20
#         self.new_pong2.goto(self.new_pong2.xcor(),new_y)
#
#     def down2(self):
#         new_y= self.new_pong2.ycor() - 20
#         self.new_pong2.goto(self.new_pong2.xcor(),new_y)

