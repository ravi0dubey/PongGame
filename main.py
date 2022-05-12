from turtle import Screen
from pong import  Pong1
from ball import Ball
from scoreboard import Scoreboard
import random
import time
YCORD1 = 280
YCORD2 = -280
XCORD1 = 380
XCORD2 = -380

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("My pong Game")
screen.tracer(0)
pong1 = Pong1((-350,0))
pong2 = Pong1((350,0))

ball = Ball()
score = Scoreboard()

screen.listen()

screen.onkey(pong1.upa,"A")
screen.onkey(pong1.downd,"D")

screen.onkey(pong2.up2,"Up")
screen.onkey(pong2.down2,"Down")

game_continues = True
while game_continues:
    screen.update()
    time.sleep(ball.pace)
    ball.ball_first_move()
    print(ball.xcor(),ball.ycor())

#Detect collision with wall on top or bottom.
    if ball.ycor() < YCORD2 or ball.ycor() > YCORD1:
        ball.ball_bounce()

#Detect collision with pong.
    if ball.distance(pong1) < 50 and ball.xcor() < -320 or ball.distance(pong2) < 50 and ball.xcor() > 320 :
        print("hit")
        ball.ball_hit_move()

#Detect collision with wall.
    if  ball.xcor() < -380 :
        print("wall hit -340")
        ball.ball_reset()
        score.pong2_add_points()

    if  ball.xcor() > 380 :
        print("wall hit + 340")
        ball.ball_reset()
        score.pong1_add_points()

screen.exitonclick()

